from django.urls import path
from . import views

urlpatterns = [
    path('search', views.ProductSearchLiestView.as_view(), name='search-view'), 
    path('<slug:slug>', views.ProductDetailView.as_view(), name='proeuct-view'),  
]