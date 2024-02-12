from io import BytesIO
from smtplib import SMTPException
from typing import Dict

from celery import shared_task
from django.conf import settings
from django.core.files import File
from django.core.mail import EmailMessage
from django.template.loader import get_template
from PIL import Image
from xhtml2pdf import pisa

from app.enums import MailTypeChoice
from app.models import MailLogs, Recipe, User
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
def send_email_task(
    user_id: int, recipient: str, content: Dict, mail_type: str, context=None
) -> Dict:
    username = User.objects.get(pk=user_id).username
    template = EmailTemplate(mail_type)
    subject = template.get_full_subject(
        [
            username,
        ]
    )
    content = template.get_full_content(content)
    email = EmailMessage(
        subject=subject,
        body=content,
        from_email=settings.FROM_EMAIL,
        to=[
            recipient,
        ],
    )
    recipe_id = None
    if mail_type == MailTypeChoice.RECIPE_SHARING.value:
        pdf = render_to_pdf_task(PDF_TEMPLATE, context)
        pdf_name = f"{context['recipe']['name']}.pdf"
        email.attach(pdf_name, pdf, "application/pdf")
        recipe_id = context["recipe"]["pk"]
    sent = False
    try:
        sent = email.send()
    except SMTPException:
        pass
    except Exception as e:
        raise send_email_task.retry(exc=e)
    finally:
        return {
            "user_id": user_id,
            "recipient": recipient,
            "recipe_id": recipe_id,
            "sent": sent,
            "mail_type": mail_type,
        }


@shared_task
def log_email_task(data):
    MailLogs.objects.create(
        user_id=data["user_id"],
        recipient=data["recipient"],
        recipe_id=data["recipe_id"],
        sent=data["sent"],
        type=data["mail_type"],
    )


@shared_task
def create_thumbnail(recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    with Image.open(recipe.image) as img:
        thumbnail_size = 300
        left, top, right, bottom = 0, 0, thumbnail_size, thumbnail_size
        if img.width > img.height:
            output_size = (img.width, thumbnail_size)
            img.thumbnail(output_size, Image.ANTIALIAS)
            left_right_crop = int((img.width - thumbnail_size) / 2)
            left = left_right_crop
            right = img.width - left_right_crop
            img = img.crop((left, top, right, bottom))
        elif img.width < img.height:
            output_size = (thumbnail_size, img.height)
            img.thumbnail(output_size, Image.ANTIALIAS)
            top_bottom_crop = int((img.height - thumbnail_size) / 2)
            top = top_bottom_crop
            bottom = img.height - top_bottom_crop
            img = img.crop((left, top, right, bottom))
        else:
            output_size = (thumbnail_size, thumbnail_size)
            img.thumbnail(output_size, Image.ANTIALIAS)
        buffer = BytesIO()
        img.save(buffer, format="JPEG")
        img = File(buffer, name=recipe.image.name)
        recipe.thumbnail = img
        recipe.save(update_fields=["thumbnail"])
        return f"Thumbnail generated and saved for recipe: {recipe}"
