from django.contrib import admin
from .models import Location, InventoryLedger, InventoryLedgerItem

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("name", "location_type", "is_active", "owner_user")
    list_filter = ("location_type", "is_active")
    search_fields = ("name",)
    
class InventoryLedgerItemInLine(admin.TabularInline):
    model = InventoryLedgerItem
    extra = 1
    

@admin.register(InventoryLedger)
class InventoryLedgerAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "action", "actor", "from_location", "to_location", "reference")
    list_filter = ("action", "timestamp")
    search_fields = ("reference", "note")
    inlines = [InventoryLedgerItemInLine]