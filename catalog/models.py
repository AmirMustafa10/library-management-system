from django.db import models
from django.db.models import F, Q
from django.core.exceptions import ValidationError


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField("ISBN", max_length=13, unique=True)
    category = models.CharField(max_length=100)
    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title", "author"]
        constraints = [
            models.CheckConstraint(
                condition=Q(total_copies__gte=0),
                name="book_total_copies_non_negative",
            ),
            models.CheckConstraint(
                condition=Q(available_copies__gte=0),
                name="book_available_copies_non_negative",
            ),
            models.CheckConstraint(
                condition=Q(available_copies__lte=F("total_copies")),
                name="book_available_not_more_than_total",
            ),
        ]

    def __str__(self):
        return f"{self.title} by {self.author}"

    def clean(self):
        super().clean()
        if len(self.isbn) not in {10, 13}:
            raise ValidationError({"isbn": "ISBN must contain 10 or 13 characters."})
        if self.available_copies > self.total_copies:
            raise ValidationError(
                {"available_copies": "Available copies cannot exceed total copies."}
            )

    @property
    def is_available(self):
        return self.available_copies > 0
