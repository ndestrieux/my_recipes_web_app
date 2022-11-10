from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, ButtonHolder, HTML


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["email"].required = True
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            Row(
                Column("first_name", css_class="form-group col-md-6"),
                Column("last_name", css_class="form-group col-md-6"),
                css_class="row",
            ),
            "username",
            "email",
            Row(
                Column("password1", css_class="form-group col-md-6"),
                Column("password2", css_class="form-group col-md-6"),
                css_class="row",
            ),
            ButtonHolder(
                Submit("submit", "register"),
                HTML("<a href='#' class='btn btn-primary'>Cancel</a>"),
            ),
        )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "POST"
        self.helper.layout = Layout(
            "username",
            "password",
            ButtonHolder(
                Submit("submit", "login"),
                HTML("<a href='#' class='btn btn-primary'>Cancel</a>"),
            ),
        )

        class Meta:
            model = User
            fields = ["username", "password"]
