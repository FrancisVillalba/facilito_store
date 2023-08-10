from django.conf import settings
from django.contrib import admin
from django.urls import path 

from facilito_store.views import index,login_vw,logout_vw

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_vw, name='vw-login'),
    path('logout', logout_vw, name='vw-logout'),
    path('index', index, name='vw-index'),
]
