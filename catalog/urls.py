from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("catalog/", views.book_list, name="book_list"),
    path("", views.Home, name="home"),
]
