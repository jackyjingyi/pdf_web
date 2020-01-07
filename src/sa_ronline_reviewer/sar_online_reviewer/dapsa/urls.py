from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.signup, name = "signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('secret/', views.secret_page, name = 'secret'),
    path('secretProtocol/', views.secret_page_protocol_audit, name = 'secret_protocl'),
    path('secret/tasks/', views.tasks, name = 'tasks'),
    path('secret/tasks/<str:pdf_path>/', views.pdfmain, name='pdfmain' ),
]

