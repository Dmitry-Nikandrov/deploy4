from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product


def home(request):
    return render(request, template_name="catalog/main.html")


def home_contact(request):
    return render(request, template_name="catalog/contacts.html")


def post_contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        message = request.POST.get("message")
        return HttpResponse(
            f"Спасибо, {name}! Ваше сообщение успешно отправлено и получено"
        )
    return render(request, "catalog/contacts.html")


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {"product": product}
    return render(request, template_name="catalog/product.html", context=context)


def product_all(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "catalog/main.html", context=context)
