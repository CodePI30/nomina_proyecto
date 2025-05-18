from django.urls import path
from .views import nomina_frontend, NominaListView, NominaDetailedFile, NominaCreateView

urlpatterns = [
    path('', nomina_frontend, name='nomina_frontend'),
    path('nomina/', NominaListView.as_view(), name='nomina-list'),
    path('nomina-file', NominaDetailedFile.as_view(), name='nomina-file'),
    path('nomina/create', NominaCreateView.as_view(), name='nomina-create'),
]