from django.contrib.auth import login
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegistrationForm
from users.models import CustomUser


class UserCreateView(CreateView):
    model = CustomUser
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = "Добро пожаловать на сайт дикой природы"
        message = "Спасибо, что зарегистрировались в нашем сервисе на нашем сайте!"
        recipient_list = [user_email]
        send_mail(
            subject, message, from_email=EMAIL_HOST_USER, recipient_list=recipient_list
        )
