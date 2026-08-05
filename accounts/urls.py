from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.user_login, name="login"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="catalog:book_list"),
        name="logout",
    ),
]
