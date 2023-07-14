from typing import Dict, List

from django.template.loader import render_to_string

from app.enums import MailTypeChoice


class EmailTemplate:
    BASE_TEMPLATE = {
        MailTypeChoice.PASSWORD_RESET.value: {
            "base_subject": "Password Reset Requested",
            "base_content": "users/email/password_reset_email.txt",
        },
        MailTypeChoice.RECIPE_SHARING.value: {
            "base_subject": "{} shared a recipe with you",
            "base_content": "users/email/recipe_sharing_email.txt",
        },
    }

    def __init__(self, mail_type):
        self.mail_type = mail_type
        self.base_subject = self.get_base_subject
        self.base_content = self.get_base_content

    @property
    def get_base_subject(self):
        return self.BASE_TEMPLATE[self.mail_type]["base_subject"]

    @property
    def get_base_content(self):
        return self.BASE_TEMPLATE[self.mail_type]["base_content"]

    def get_full_subject(self, subject_data: List) -> str:
        return self.base_subject.format(*subject_data)

    def get_full_content(self, content_data: Dict) -> str:
        return render_to_string(self.base_content, content_data)
