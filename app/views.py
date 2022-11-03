from django.urls import reverse_lazy
from django.views.generic import CreateView

from app.forms import UserRegistrationForm


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = "users/registration.html"
    success_url = reverse_lazy("register")
