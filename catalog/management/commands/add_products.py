from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Load test data from fixture"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category1, _ = Category.objects.get_or_create(
            name="Бытовая химия", description="Химия для дома, дачи, огорода"
        )

        products1 = [
            {
                "name": "Стиральный порошок",
                "description": "Ариэль колор",
                "category": category1,
                "price": 100,
            },
            {
                "name": "Средство для мытья пола",
                "description": "Ваниш",
                "category": category1,
                "price": 200,
            },
            {
                "name": "Соляная кислота",
                "description": "Раствор 40%",
                "category": category1,
                "price": 150,
            },
            {
                "name": "Тирет",
                "description": "Средство дял устранения засоров",
                "category": category1,
                "price": 500,
            },
        ]

        for product in products1:
            prod, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Успешно добавлен новый продукт: {prod.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Продукт уже создан: {prod.name}")
                )

        category2, _ = Category.objects.get_or_create(
            name="Фрукты", description="Сезонные или круглогодичные"
        )

        products2 = [
            {
                "name": "Апельсины",
                "description": "Азербайджан",
                "category": category2,
                "price": 90,
            },
            {
                "name": "Бананы",
                "description": "Эквадор",
                "category": category2,
                "price": 150,
            },
            {
                "name": "Яблоки",
                "description": "Молдавия",
                "category": category2,
                "price": 90,
            },
            {
                "name": "Кокосы",
                "description": "Куба",
                "category": category2,
                "price": 250,
            },
        ]

        for product in products2:
            prod, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Успешно добавлен новый продукт: {prod.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Продукт уже создан: {prod.name}")
                )

        category3, _ = Category.objects.get_or_create(
            name="Овощи", description="овощ хорошый, вкусный, полэзный)"
        )

        products3 = [
            {
                "name": "Картошка",
                "description": "Тамбов",
                "category": category3,
                "price": 25,
            },
            {
                "name": "Капуста",
                "description": "Вологда",
                "category": category3,
                "price": 80,
            },
            {
                "name": "Морковь",
                "description": "Луганск",
                "category": category3,
                "price": 500,
            },
            {
                "name": "Свекла",
                "description": "Ростов",
                "category": category3,
                "price": 45,
            },
            {
                "name": "Кабачки",
                "description": "Липецк",
                "category": category3,
                "price": 10,
            },
            {
                "name": "Огурцы",
                "description": "Луховцы",
                "category": category3,
                "price": 70,
            },
        ]

        for product in products3:
            prod, created = Product.objects.get_or_create(**product)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Успешно добавлен новый продукт: {prod.name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Продукт уже создан: {prod.name}")
                )
