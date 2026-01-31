from django.conf import settings
from django.db import models

from parts.models import Part


class Location(models.Model):
    class LocationType(models.TextChoices):
        WAREHOUSE = "WAREHOUSE", "Warehouse"
        TECHNICIAN = "TECHNICIAN", "Technician"
        OTHER = "OTHER", "Other"

    name = models.CharField(max_length=120)
    location_type = models.CharField(max_length=20, choices=LocationType.choices)
    is_active = models.BooleanField(default=True)

    owner_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="owned_locations",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.location_type}: {self.name}"


class InventoryLedger(models.Model):
    class Action(models.TextChoices):
        RECEIVE = "RECEIVE", "Receive"
        ISSUE = "ISSUE", "Issue"
        TRANSFER = "TRANSFER", "Transfer"
        ADJUST = "ADJUST", "Adjust"

    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=10, choices=Action.choices)

    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="inventory_actions",
    )

    from_location = models.ForeignKey(
        Location,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="ledger_from",
    )
    to_location = models.ForeignKey(
        Location,
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        related_name="ledger_to",
    )

    reference = models.CharField(max_length=200, blank=True)
    note = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.timestamp:%Y-%m-%d %H:%M} {self.action}"


class InventoryLedgerItem(models.Model):
    ledger = models.ForeignKey(
        InventoryLedger,
        on_delete=models.CASCADE,
        related_name="items",
    )
    part = models.ForeignKey(
        Part,
        on_delete=models.PROTECT,
    )
    qty = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.part.part_number} x{self.qty}"
