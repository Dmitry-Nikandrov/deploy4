from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Load test data from fixture"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(
            name="Бытовая химия", description="Химия для дома, дачи, огорода"
        )

        products = [
            {
                "name": "Стиральный порошок",
                "description": "Ариэль колор",
                "category": category,
                "price": 100,
            },
            {
                "name": "Средство для мытья пола",
                "description": "Ваниш",
                "category": category,
                "price": 200,
            },
            {
                "name": "Соляная кислота",
                "description": "Раствор 40%",
                "category": category,
                "price": 150,
            },
            {
                "name": "Тирет",
                "description": "Средство дял устранения засоров",
                "category": category,
                "price": 500,
            },
        ]

        for product in products:
            prod, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Успешно добавлен новый продукт: {prod.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Продукт уже создан: {prod.name}")
                )
