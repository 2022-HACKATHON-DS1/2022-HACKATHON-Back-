from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mapapp import views as mapapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/',mapapp_views.map, name='map'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)