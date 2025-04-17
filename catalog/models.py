from django.db import models

from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="наименование")
    description = models.CharField(max_length=150, verbose_name="описание")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="наименование")
    description = models.CharField(max_length=150, verbose_name="описание")
    image = models.ImageField(
        upload_to="catalog/", blank=True, null=True, verbose_name="изображение"
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category"
    )
    price = models.IntegerField(verbose_name="цена за покупку")
    created_at = models.DateField(auto_now_add=True, verbose_name="дата создания")
    updated_at = models.DateField(
        auto_now=True, verbose_name="дата последнего изменения"
    )
    is_published = models.BooleanField(default=False, blank=True, null=True)
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="owner",
        verbose_name="Владелец",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["price"]
        permissions = [("can_unpublish_product", "can unpublish product")]
