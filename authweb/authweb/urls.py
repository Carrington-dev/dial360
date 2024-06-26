from django.contrib import admin
from django.urls import path, include
from authweb import  settings
from django.conf.urls.static import static

admin.site.site_header = 'Dial360 '                   
admin.site.index_title = 'Dial360 Portal'                 
admin.site.site_title = 'Dial360 Administration'

version = 'v1'

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path(f'api/{version}/auth/', include('djoser.urls')),
    path(f'api/{version}/auth/', include('djoser.urls.jwt')),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)