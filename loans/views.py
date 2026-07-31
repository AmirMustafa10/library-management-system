from django.shortcuts import render


def my_loans(request):
    placeholder_loans = [
        {
            "book_title": "Clean Code",
            "author": "Robert C. Martin",
            "borrow_date": "Pending FR-3",
            "status": "Placeholder",
        },
        {
            "book_title": "Python Crash Course",
            "author": "Eric Matthes",
            "borrow_date": "Pending FR-3",
            "status": "Placeholder",
        },
    ]
    return render(request, "loans/my_loans.html", {"loans": placeholder_loans})
