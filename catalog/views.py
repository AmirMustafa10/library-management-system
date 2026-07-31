from django.db.models import Q
from django.shortcuts import render

from .models import Book


def book_list(request):
    query = request.GET.get("q", "").strip()
    books = Book.objects.all()

    if query:
        books = books.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

    context = {
        "books": books,
        "query": query,
    }
    return render(request, "catalog/book_list.html", context)
