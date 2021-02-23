from django.urls import path
from .views import MenuItemListAPIView, MenuItemDetailAPIView, OrderListAPIView, OrderDetailAPIView


app_name = "restaurant"

urlpatterns = [
    path('menu-items/<int:pk>/', MenuItemDetailAPIView.as_view(), name="item-detail"),
    path('menu-items/', MenuItemListAPIView.as_view(), name="item"),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view(), name="order-detail"),
    path('orders/', OrderListAPIView.as_view(), name="order")
]
