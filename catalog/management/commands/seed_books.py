from django.core.management.base import BaseCommand

from catalog.models import Book


SAMPLE_BOOKS = [
    {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "isbn": "9780132350884",
        "category": "Software Engineering",
        "total_copies": 4,
        "available_copies": 4,
    },
    {
        "title": "Django for Beginners",
        "author": "William S. Vincent",
        "isbn": "9781735467207",
        "category": "Web Development",
        "total_copies": 3,
        "available_copies": 3,
    },
    {
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "isbn": "9781718502703",
        "category": "Programming",
        "total_copies": 5,
        "available_copies": 5,
    },
    {
        "title": "The Pragmatic Programmer",
        "author": "David Thomas and Andrew Hunt",
        "isbn": "9780135957059",
        "category": "Software Engineering",
        "total_copies": 2,
        "available_copies": 2,
    },
    {
        "title": "Introduction to Algorithms",
        "author": "Thomas H. Cormen",
        "isbn": "9780262046305",
        "category": "Computer Science",
        "total_copies": 2,
        "available_copies": 2,
    },
]


class Command(BaseCommand):
    help = "Seed the catalog with sample books for local demos."

    def handle(self, *args, **options):
        created = 0
        updated = 0

        for data in SAMPLE_BOOKS:
            _, was_created = Book.objects.update_or_create(
                isbn=data["isbn"],
                defaults=data,
            )
            if was_created:
                created += 1
            else:
                updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Seeded catalog books: {created} created, {updated} updated."
            )
        )
