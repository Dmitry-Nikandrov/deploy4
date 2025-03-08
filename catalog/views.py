from django.http import HttpResponse
from django.shortcuts import render


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
