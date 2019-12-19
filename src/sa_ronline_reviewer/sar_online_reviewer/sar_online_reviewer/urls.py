from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('dapsa.urls'), name='dapsa'),
    path('admin/', admin.site.urls),
]
