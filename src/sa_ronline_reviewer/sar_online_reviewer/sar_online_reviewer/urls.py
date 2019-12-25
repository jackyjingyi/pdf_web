from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from dapsa import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dapsa/', include('dapsa.urls'), name = "dapsa"),
    
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)