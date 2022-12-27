from io import BytesIO
from smtplib import SMTPException

from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import get_template
from xhtml2pdf import pisa

from app.models import MailLogs, User
from app.properties import PDF_TEMPLATE
from app.utils.mail_templates import EmailTemplate


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
    if not status.err:
        return pdf_file.decode("ISO8859-1")
    return None


@shared_task(autoretry_for=(Exception,), default_retry_delay=30, max_retries=3)
def send_email_task(user_id, recipient, content, context):
    pdf = render_to_pdf_task(PDF_TEMPLATE, context)
    pdf_name = f"{context['recipe']['name']}.pdf"
    template = EmailTemplate()
    username = User.objects.get(pk=user_id).username
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
    sent = False
    try:
        sent = email.send()
    except SMTPException:
        pass
    except Exception as e:
        raise send_email_task.retry(exc=e)
    finally:
        return {
            "from_user_id": user_id,
            "recipient": recipient,
            "recipe_id": context["recipe"]["pk"],
            "sent": sent,
        }


@shared_task
def log_email_task(data):
    MailLogs.objects.create(
        from_user_id=data["from_user_id"],
        recipient=data["recipient"],
        recipe_id=data["recipe_id"],
        sent=data["sent"],
    )
