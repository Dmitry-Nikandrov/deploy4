from django.urls import path

from catalog.apps import CatalorConfig
from catalog.views import home_contact, post_contact, product_all, product_detail

app_name = CatalorConfig.name

urlpatterns = [
    path("home/", product_all, name="main"),
    path("contacts/", home_contact, name="contacts"),
    path("contacts_post/", post_contact, name="contacts_post"),
    path("products/<int:pk>", product_detail, name="products"),
]
