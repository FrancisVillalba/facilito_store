from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('search', views.ProductSearchLiestView.as_view(), name='search-view'), 
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product-view'),  
]