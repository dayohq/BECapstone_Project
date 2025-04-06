import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    sku = models.CharField(max_length=20, unique=True, editable=False, default=uuid.uuid4().hex[:8].upper())
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    managed_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sku} - {self.name}"
    

class InventoryChange(models.Model):
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name='changes')
    changed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    change_type = models.CharField(max_length=10, choices=[('restock', 'Restock'), ('sale', 'Sale')])
    quantity_changed = models.IntegerField()
    change_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.name} - {self.change_type} ({self.quantity_changed})"
