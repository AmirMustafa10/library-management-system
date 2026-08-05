from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from catalog.models import Book
from .models import Loan


@login_required
def borrow_book(request, book_id):

    if request.method != "POST":
        return redirect("catalog")

    book = get_object_or_404(Book, id=book_id)

    if book.available_copies <= 0:
        messages.error(request, "No copies available.")
        return redirect("catalog")

    already_borrowed = Loan.objects.filter(
        member=request.user, book=book, status="Borrowed"
    ).exists()

    if already_borrowed:
        messages.error(request, "You already borrowed this book.")
        return redirect("catalog")

    Loan.objects.create(member=request.user, book=book, status="Borrowed")

    messages.success(request, "Book borrowed successfully.")

    return redirect("my_loans")


@login_required
def return_book(request, loan_id):

    if request.method != "POST":
        return redirect("my_loans")

    loan = get_object_or_404(Loan, id=loan_id, member=request.user, status="Borrowed")

    loan.status = "Returned"
    loan.return_date = timezone.now()
    loan.save()

    messages.success(request, "Book returned successfully.")

    return redirect("my_loans")


@login_required
def my_loans(request):

    loans = Loan.objects.filter(member=request.user, status="Borrowed")

    return render(request, "loans/my_loans.html", {"loans": loans})
