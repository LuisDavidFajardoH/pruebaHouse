# turnos/urls.py
from django.urls import path
from .views import TurnoListView, TurnoCreateView, TurnoUpdateView, CambiarEstadoTurnoStaffView,TurnosPendientesView
from .apis import UsuarioExistenciaAPIView, TurnoListAPIView

urlpatterns = [
    path('', TurnoListView.as_view(), name='listar'),
    path('nuevo/', TurnoCreateView.as_view(), name='nuevo'),
    path('<int:pk>/editar/', TurnoUpdateView.as_view(), name='editar'),
    path('<int:pk>/cambiar-estado/', CambiarEstadoTurnoStaffView.as_view(), name='cambiar_estado'),
    path('api/usuario/<str:identificacion>/', UsuarioExistenciaAPIView.as_view(), name='validar_usuario'),
    path('api/turnos/', TurnoListAPIView.as_view(), name='listar_turnos'),
    path('pendientes/', TurnosPendientesView.as_view(), name='listar_pendientes'),
]
