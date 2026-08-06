from django.db import models, transaction
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from catalog.models import Book


class Loan(models.Model):

    STATUS_CHOICES = [
        ("Borrowed", "Borrowed"),
        ("Returned", "Returned"),
    ]

    member = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="loans",
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="loans",
    )

    borrow_date = models.DateTimeField(
        auto_now_add=True,
    )

    return_date = models.DateTimeField(
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Borrowed",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["book", "member"],
                condition=models.Q(status="Borrowed"),
                name="unique_active_loan_per_user_book",
            ),
        ]

    def clean(self):
        """
        Prevent the same member from borrowing
        the same book more than once at the same time.
        """

        super().clean()

        if self.status == "Borrowed" and self.member and self.book:
            exists = (
                Loan.objects.filter(
                    member=self.member,
                    book=self.book,
                    status="Borrowed",
                )
                .exclude(pk=self.pk)
                .exists()
            )

            if exists:
                raise ValidationError(
                    {
                        "book": (
                            "This member already has " "an active loan for this book."
                        )
                    }
                )

            if self.book.available_copies <= 0:
                raise ValidationError({"book": "This book is currently unavailable."})

    def save(self, *args, **kwargs):
        """
        Keep Book.available_copies synchronized
        whenever a Loan is created or its status changes.
        """

        with transaction.atomic():

            # Run model validation.
            self.full_clean()

            # New Loan
            if self.pk is None:

                if self.status == "Borrowed":

                    if self.book.available_copies <= 0:
                        raise ValidationError(
                            {"book": ("This book is currently " "unavailable.")}
                        )

                    self.book.available_copies -= 1

                    self.book.save(update_fields=["available_copies"])

            else:

                old_loan = Loan.objects.select_related("book").get(pk=self.pk)

                # Borrowed → Returned
                if old_loan.status == "Borrowed" and self.status == "Returned":
                    self.book.available_copies += 1

                    self.book.save(update_fields=["available_copies"])

                # Returned → Borrowed
                elif old_loan.status == "Returned" and self.status == "Borrowed":

                    if self.book.available_copies <= 0:
                        raise ValidationError(
                            {"book": ("This book is currently unavailable.")}
                        )

                    self.book.available_copies -= 1

                    self.book.save(update_fields=["available_copies"])

            super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.member.username} - {self.book.title}"
