#Usuario/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView
from usuarios.views import RegistroUsuario
from .views import ListarPacientesView

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/registro/', RegistroUsuario.as_view(), name='registro'),
    path('listar-pacientes/', ListarPacientesView.as_view(), name='listar_pacientes'),
]
