from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="наименование")),
                (
                    "description",
                    models.CharField(max_length=150, verbose_name="описание"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="наименование")),
                (
                    "description",
                    models.CharField(max_length=150, verbose_name="описание"),
                ),
                (
                    "image",
                    models.ImageField(upload_to="photos/", verbose_name="изображение"),
                ),
                (
                    "category",
                    models.CharField(max_length=150, verbose_name="категория"),
                ),
                ("price", models.IntegerField(verbose_name="цена за покупку")),
                (
                    "created_at",
                    models.DateField(auto_now_add=True, verbose_name="дата создания"),
                ),
                (
                    "updated_at",
                    models.DateField(
                        auto_now=True, verbose_name="дата последнего изменения"
                    ),
                ),
            ],
            options={
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
                "ordering": ["price"],
            },
        ),
    ]
