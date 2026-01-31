from django.contrib import admin
from .models import Part


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ("part_number", "name", "unit", "is_active", "updated_at")
    search_fields = ("part_number", "name")
    list_filter = ("is_active", "unit")
    ordering = ("part_number",)
