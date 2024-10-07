from django.urls import path
from apps.main.views import (
    ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView
)


urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
]