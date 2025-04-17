from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


class ProductService:



    @staticmethod
    def get_products_from_cache():
        if not CACHE_ENABLED:
            return Product.objects.all()
        products = cache.get("prod_list")
        if not products:
            products = Product.objects.all()
            cache.set("prod_list", products)
            return products
        return products
