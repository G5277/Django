from django.urls import path
from .views import product_create_view

urlpatterns = [
    path('product_create/', product_create_view)
]
