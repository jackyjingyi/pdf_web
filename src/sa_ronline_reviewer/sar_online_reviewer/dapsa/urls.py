from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.signup, name = "signup"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('secret/<str:task_type>/', views.secret_page, name = 'secret'),
    path('secretProtocol/', views.secret_page_protocol_audit, name = 'secret_protocl'),
    path('secret/<str:task_type>/<str:asin_number>/', views.tasks, name = 'tasks'),
    path('secret/<str:task_type>/<str:asin_number>/<str:caseid>/', views.pdfmain, name='pdfmain' ),
    path('secret/<str:task_type>/<str:asin_number>/<str:caseid>/check_<str:speck>/', views.conclusion_check, name="mapping_check")
]

