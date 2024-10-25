# usuarios/api_urls.py
from django.urls import path
from .views import UsuarioExistenciaAPIView, TurnoListAPIView

urlpatterns = [
    path('usuario/<str:identificacion>/', UsuarioExistenciaAPIView.as_view(), name='validar_usuario'),
    path('turnos/', TurnoListAPIView.as_view(), name='listar_turnos'),
]
