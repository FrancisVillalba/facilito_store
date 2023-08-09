from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from facilito_store.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='vw-index'),
    path('principal', index, name='vw-principal'),
]
