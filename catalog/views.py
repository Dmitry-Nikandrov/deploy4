from itertools import product

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from catalog.forms import ProductForm, ProductModeratorsForm
from catalog.models import Product
from users.models import CustomUser


def home_contact(request):
    return render(request, template_name="catalog/contacts.html")


class ProductListView(ListView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:prod_list")

    def form_valid(self,form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:prod_list")

    def get_form_class(self):
        user = self.request.user
        if user.has_perm("catalog.delete_product") and user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorsForm
        raise PermissionDenied

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            return self.object
        raise PermissionDenied




class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:prod_list")
    form_class = ProductForm
    permission_required = 'catalog.delete_product'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        user = self.request.user
        if any([
            (user == self.object.owner),
            all([user.has_perm("catalog.delete_product"), user.has_perm("catalog.can_unpublish_product")])
            ]):
            return self.object
        raise PermissionDenied

class ContactView(TemplateView):
    template_name = "catalog/contacts.html"
