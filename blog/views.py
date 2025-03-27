from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from blog.models import Blog


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published__exact=True)


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "image", "is_published", "count_watches")
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content", "image", "is_published", "count_watches")
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_watches += 1
        if self.object.count_watches == 17:
            print("Сообщение успешно отправлено")
            send_mail(
                "Поздравление",
                f"Поздравление: число просмотров статьи {self.model.title} достигло {self.model.count_watches}",
                "from@example.com",
                ["dnikandrov@yandex.ru"],
            )
            print("Сообщение успешно отправлено")
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")
