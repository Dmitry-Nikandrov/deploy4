from django.urls import path

from catalog.apps import CatalorConfig
from catalog.views import (
    ContactView,
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductsByCategoryView,
    ProductUpdateView,
)

app_name = CatalorConfig.name

urlpatterns = [
    path("prod/", ProductListView.as_view(), name="prod_list"),
    path("prod/new/", ProductCreateView.as_view(), name="prod_create"),
    path("prod/<int:pk>/update/", ProductUpdateView.as_view(), name="prod_update"),
    path("prod/<int:pk>/detail", ProductDetailView.as_view(), name="prod_detail"),
    path("prod/del/<int:pk>/del", ProductDeleteView.as_view(), name="prod_delete"),
    path("cont/", ContactView.as_view(), name="cont_list"),
    path("prod/<int:pk>/prodlist", ProductsByCategoryView.as_view(), name="prod_all"),
]
