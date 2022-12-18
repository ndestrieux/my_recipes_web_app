import binascii
from io import BytesIO

from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import get_template
from xhtml2pdf import pisa

from app.properties import PDF_TEMPLATE
from app.utils import EmailTemplate

@shared_task
def render_to_pdf_task(template_src, context_dict=None):
    if context_dict is None:
        context_dict = {}
    template = get_template(template_src)
    html = template.render(context_dict)
    buffer = BytesIO()
    status = pisa.pisaDocument(BytesIO(html.encode("utf-8")), buffer)
    buffer.seek(0)
    pdf_file = buffer.read()
    print(type(pdf_file))
    if not status.err:
        return pdf_file.decode("ISO8859-1")
    return None


@shared_task(autoretry_for=(Exception,), default_retry_delay=30, max_retries=3)
def send_email_task(username, recipient, content, context):
    pdf = render_to_pdf_task(PDF_TEMPLATE, context)
    pdf_name = f"{context['recipe']['name']}.pdf"
    template = EmailTemplate()
    subject = template.get_full_subject(username)
    content = template.get_full_content(content)
    email = EmailMessage(
        subject=subject,
        body=content,
        from_email=settings.FROM_EMAIL,
        to=[
            recipient,
        ],
    )
    email.attach(pdf_name, pdf, "application/pdf")
    email.send()
