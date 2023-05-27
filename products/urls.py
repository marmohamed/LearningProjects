from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('products/', views.products, name='products'),
    path('products/details/<int:id>', views.details, name='details')
]