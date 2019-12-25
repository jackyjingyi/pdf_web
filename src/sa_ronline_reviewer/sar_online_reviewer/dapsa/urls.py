from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.signup, name = "signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('secret/', views.secret_page, name = 'secret'),
    path('secret/upload/',views.upload , name = 'upload'),
    path('list', views.list, name = 'list')
]

