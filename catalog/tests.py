from io import StringIO

from django.contrib import admin
from django.core.exceptions import ValidationError
from django.core.management import call_command
from django.db import IntegrityError, transaction
from django.test import TestCase

from .admin import BookAdmin
from .models import Book


class BookModelTests(TestCase):
    def test_book_string_representation_uses_title_and_author(self):
        book = Book(
            title="Clean Code",
            author="Robert C. Martin",
            isbn="9780132350884",
            category="Software Engineering",
            total_copies=4,
            available_copies=2,
        )

        self.assertEqual(str(book), "Clean Code by Robert C. Martin")

    def test_available_copies_cannot_exceed_total_copies(self):
        book = Book(
            title="Invalid Inventory",
            author="A. Librarian",
            isbn="1234567890",
            category="Testing",
            total_copies=1,
            available_copies=2,
        )

        with self.assertRaises(ValidationError):
            book.full_clean()

    def test_database_enforces_available_copies_not_more_than_total(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Book.objects.create(
                    title="Invalid Inventory",
                    author="A. Librarian",
                    isbn="1234567890123",
                    category="Testing",
                    total_copies=1,
                    available_copies=2,
                )

    def test_is_available_reflects_inventory_count(self):
        available = Book(available_copies=1)
        unavailable = Book(available_copies=0)

        self.assertTrue(available.is_available)
        self.assertFalse(unavailable.is_available)


class BookAdminTests(TestCase):
    def test_book_is_registered_with_custom_admin(self):
        self.assertIsInstance(admin.site._registry[Book], BookAdmin)


class SeedBooksCommandTests(TestCase):
    def test_seed_books_command_is_idempotent(self):
        output = StringIO()

        call_command("seed_books", stdout=output)
        first_count = Book.objects.count()
        call_command("seed_books", stdout=output)
        second_count = Book.objects.count()

        self.assertEqual(first_count, 5)
        self.assertEqual(second_count, 5)
