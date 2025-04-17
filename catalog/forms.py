from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product


class ProductForm(forms.ModelForm):
    restriction_words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get("name")
        for word in ProductForm.restriction_words:
            if word in name.lower():
                raise ValidationError(f"Слово {name} недопустимо")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        for word in ProductForm.restriction_words:
            if word in description.lower():
                raise ValidationError(f"Слово {description} недопустимо")
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена товара не может быть отрицательной")
        return price

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields.get("name").widget.attrs.update(
            {
                "class": "form-group",
                "placeholder": "Введите продукт",
            }
        )

        self.fields.get("description").widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите описание продукта",
            }
        )

        self.fields.get("image").widget.attrs.update({"class": "form-control"})

        self.fields.get("category").widget.attrs.update({"class": "form-control"})

        self.fields.get("price").widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите цену продукта"}
        )


class ProductModeratorsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("is_published",)
