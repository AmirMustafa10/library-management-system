from django.db import models
from django.contrib.auth.models import User
from catalog.models import Book


class Loan(models.Model):

    STATUS_CHOICES = [
        ("Borrowed", "Borrowed"),
        ("Returned", "Returned"),
    ]

    member = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="loans"
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="loans"
    )

    borrow_date = models.DateTimeField(auto_now_add=True)

    return_date = models.DateTimeField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Borrowed"
    )

    def __str__(self):
        return f"{self.member.username} - {self.book.title}"