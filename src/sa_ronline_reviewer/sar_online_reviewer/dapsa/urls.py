from . import views
from django.urls import path

urlpatterns = [
    path('', views.PDFExtractionView.as_view(), name = 'pdf')
]