from django.urls import path, include
from .views import CategoryListCreateView, CategoryDetailView, InventoryItemListCreateView, InventoryItemDetailView
from rest_framework.routers import DefaultRouter
from .views import InventoryChangeViewSet, UserViewSet, InventoryLevelView, InventoryChangeHistoryView


# Routers
router = DefaultRouter()
router.register(r'inventory-changes', InventoryChangeViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('inventory/', InventoryItemListCreateView.as_view(), name='inventory-list-create'),
    path('inventory/<int:pk>/', InventoryItemDetailView.as_view(), name='inventory-detail'),
    path('', include(router.urls)),
    path('inventory-levels/', InventoryLevelView.as_view(), name='inventory-levels'),
    path('inventory/<int:item_id>/changes/', InventoryChangeHistoryView.as_view(), name='inventory-change-history'),
]
