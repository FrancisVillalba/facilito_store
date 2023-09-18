from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order, name='order-view'),
    path('direccion', views.address, name='address-view'),
    path('seleccionar/direccion', views.select_address, name='select_address-view'),
    path('establecer/direccion/<int:pk>', views.check_address, name='check_address-view'),
    path('confirmacion', views.confirm, name='confirm-view'),
    path('cancelar', views.cancel, name='cancel-view'),
    path('completar', views.complete, name='complete-view'),
]