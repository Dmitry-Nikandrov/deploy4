from django.urls import path
from catalog.apps import CatalorConfig
from catalog.views import home, home_contact, post_contact

app_name = CatalorConfig.name

urlpatterns = [
    path("home/", home, name="main"),
    path("contacts/", home_contact, name="contacts"),
    path("contacts_post/", post_contact, name="contacts_post"),
]
