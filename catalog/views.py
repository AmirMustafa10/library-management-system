from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book


@login_required
def book_list(request):
    query = request.GET.get("q", "").strip()
    books = Book.objects.all()

    if query:
        books = books.filter(Q(title__icontains=query) | Q(author__icontains=query))

    context = {
        "books": books,
        "query": query,
    }
    return render(request, "catalog/book_list.html", context)


def Home(request):
    if request.user.is_authenticated:
        return redirect("catalog:book_list")

    return render(request, "home.html")
