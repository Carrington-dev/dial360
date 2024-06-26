from django.contrib import admin
from django.urls import path, include

version = 'v1'

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path(f'api/{version}/auth/', include('djoser.urls')),
    path(f'api/{version}/auth/', include('djoser.urls.jwt')),
]
