from django.contrib import admin
from .models import Category, InventoryItem, InventoryChange

# Register your models here.

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'price', 'category', 'date_added', 'managed_by']
    search_fields = ['name', 'category__name']
    list_filter = ['category', 'date_added']
    ordering = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(InventoryChange)
class InventoryChangeAdmin(admin.ModelAdmin):
    list_display = ['item', 'change_type', 'quantity_changed', 'changed_by', 'change_date']
    list_filter = ['change_type', 'change_date']
    search_fields = ['item__name', 'changed_by__username']