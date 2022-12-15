from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMessage

from app.properties import PDF_TEMPLATE
from app.utils import render_to_pdf, EmailTemplate


@shared_task(autoretry_for=(Exception,), default_retry_delay=30, max_retries=3)
def send_email_task(username, recipient, content, context):
    pdf = render_to_pdf(PDF_TEMPLATE, context)
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
