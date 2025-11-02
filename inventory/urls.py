from django.urls import path
from . import views
from .views import product_list

urlpatterns = [
    path("", product_list, name="product-list"),
]
