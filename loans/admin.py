from django.contrib import admin
from .models import Loan


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = (
        "member",
        "book",
        "borrow_date",
        "return_date",
        "status",
    )

    list_filter = (
        "status",
        "borrow_date",
    )

    search_fields = (
        "member__username",
        "book__title",
    )