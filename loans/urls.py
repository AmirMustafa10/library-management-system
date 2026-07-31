from django.urls import path

from . import views

app_name = "loans"

urlpatterns = [
    path("my/", views.my_loans, name="my_loans"),
]
