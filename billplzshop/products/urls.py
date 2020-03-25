from django.urls import path

from .views import ProductListView, ProductDetailView, ProductCheckoutView

app_name = 'products'
urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='detail'),
    path(
        'products/<int:pk>/checkout',
        ProductCheckoutView.as_view(),
        name='checkout'
    )
]