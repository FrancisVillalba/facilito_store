from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from products.views import ProductListView  
from facilito_store.views import login_vw,logout_vw,register_vw
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('usuarios/login', login_vw, name='vw-login'), 
    path('', ProductListView.as_view(), name='vw-index'),
    path('usuarios/logout', logout_vw, name='vw-logout'),
    path('usuarios/registro', register_vw, name='vw-register'),
    path('productos/', include('products.urls'), name='vw-products'),
    # path('carrito/', include('carts.urls'), name='vw-carts'),
    path('carrito/', include('carts.urls')),
    path('orden_compras/', include('orders.urls')),
    path('direcciones/', include('shipping_addresses.urls')),
    path('codigos/', include('promo_codes.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
