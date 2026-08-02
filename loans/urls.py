from django.urls import path
from .views import borrow_book, return_book, my_loans

urlpatterns = [
    path("borrow/<int:book_id>/", borrow_book, name="borrow_book"),
    path("return/<int:loan_id>/", return_book, name="return_book"),
    path("my-loans/", my_loans, name="my_loans"),
]