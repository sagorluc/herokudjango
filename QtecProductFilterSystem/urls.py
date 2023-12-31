
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Product_app.urls')),
    path('api/', include('API.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    
] 

# if settings.DEBUG
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATICFILES_DIRS[0])
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
