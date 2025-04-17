from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True, max_length=30, verbose_name="Email")
    phone_number = models.CharField(
        max_length=30,
        verbose_name="Номер телефона",
        blank=True,
        null=True,
        help_text="Введите номер телефона",
    )
    country = models.CharField(
        max_length=30,
        verbose_name="Страна",
        blank=True,
        null=True,
        help_text="Введите страну",
    )
    image = models.ImageField(
        upload_to="users/",
        verbose_name="Заставка",
        blank=True,
        null=True,
        help_text="Загрузите заставку",
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(
        "auth.Group", related_name="customuser_set", blank=True
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="customuser_set", blank=True
    )
