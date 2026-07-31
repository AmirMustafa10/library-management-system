from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "isbn",
        "category",
        "total_copies",
        "available_copies",
        "is_available",
    )
    list_filter = ("category",)
    search_fields = ("title", "author", "isbn")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("title", "author")
    fieldsets = (
        ("Book Details", {"fields": ("title", "author", "isbn", "category")}),
        ("Copy Counts", {"fields": ("total_copies", "available_copies")}),
        ("Audit", {"fields": ("created_at", "updated_at")}),
    )
