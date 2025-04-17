from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from catalog.forms import ProductForm, ProductModeratorsForm
from catalog.models import Category, Product

from .services import ProductService


def home_contact(request):
    return render(request, template_name="catalog/contacts.html")


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return ProductService.get_products_from_cache()


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:prod_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:prod_list")

    def get_form_class(self):
        user = self.request.user
        if user.has_perm("catalog.delete_product") and user.has_perm(
            "catalog.can_unpublish_product"
        ):
            return ProductModeratorsForm
        raise PermissionDenied

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            return self.object
        raise PermissionDenied


@method_decorator(cache_page(60 * 15), name="dispatch")
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductsByCategoryView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "catalog/product_from_category.html"

    def get_queryset(self):
        cat_id = self.kwargs.get("pk")
        return ProductService.get_products_from_category(category_id=cat_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = get_object_or_404(Category, id=self.kwargs.get("pk"))
        return context


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:prod_list")
    form_class = ProductForm
    permission_required = "catalog.delete_product"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if any(
            [
                (user == self.object.owner),
                all(
                    [
                        user.has_perm("catalog.delete_product"),
                        user.has_perm("catalog.can_unpublish_product"),
                    ]
                ),
            ]
        ):
            return self.object
        raise PermissionDenied


class ContactView(TemplateView):
    template_name = "catalog/contacts.html"
