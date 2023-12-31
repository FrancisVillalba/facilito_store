from django.urls import path
from . import views

app_name = 'shipping_addresses'

urlpatterns = [
    path('', views.ShippingAddressListView.as_view(), name='shipping-address-view'), 
    path('nuevo', views.create, name='create-view'), 
    path('editar/<int:pk>', views.ShippingAddressUpdateView.as_view(), name='update-view'), 
    path('eliminar/<int:pk>', views.ShippingAddressDeleteView.as_view(), name='delete-view'), 
    path('default/<int:pk>', views.default, name='default-view'), 
]