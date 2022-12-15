from celery import shared_task
from django.core.mail import EmailMessage

from app.properties import PDF_TEMPLATE
from app.utils import render_to_pdf


@shared_task(autoretry_for=(Exception,), default_retry_delay=30, max_retries=3)
def send_email_task(username, recipient, content, context):
    pdf = render_to_pdf(PDF_TEMPLATE, context)
    pdf_name = f"{context['recipe']['name']}.pdf"
    subject = f"{username} shared a recipe with you!"
    separator = 40 * "-"
    base_content = f"\n\n{separator}\nPlease find the recipe in attachment"
    content = content + base_content
    email = EmailMessage(
        subject=subject,
        body=content,
        from_email="n.destrieux@gmail.com",
        to=[
            recipient,
        ],
    )
    email.attach(pdf_name, pdf, "application/pdf")
    email.send()
