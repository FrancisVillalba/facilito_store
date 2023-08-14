from django.conf import settings
from django.contrib import admin
from django.urls import path
from products.views import ProductListView  
from facilito_store.views import login_vw,logout_vw,register_vw

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('usuarios/login', login_vw, name='vw-login'), 
    path('', ProductListView.as_view(), name='vw-index'),
    path('usuarios/logout', logout_vw, name='vw-logout'),
    path('usuarios/registro', register_vw, name='vw-register'),
]
