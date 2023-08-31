from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path('', views.cart, name='cart-view'),
    path('agregar', views.add, name='add-view'),
    path('eliminar', views.remove, name='remove-view'),
]