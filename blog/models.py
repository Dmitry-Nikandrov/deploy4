from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание")
    image = models.ImageField(
        upload_to="blog/", blank=True, null=True, verbose_name="Изображение"
    )
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField()
    count_watches = models.IntegerField(verbose_name="Число просмотров", default=0)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"
