#Url/turnos/urls.py
from django.urls import path
from .views import TurnoListView, TurnoCreateView, TurnoUpdateView,CambiarEstadoTurnoStaffView

urlpatterns = [
    path('', TurnoListView.as_view(), name='listar'),  # Listar turnos
    path('nuevo/', TurnoCreateView.as_view(), name='nuevo'),  # Crear turno
    path('<int:pk>/editar/', TurnoUpdateView.as_view(), name='editar'),  # Editar turno
     path('<int:pk>/cambiar-estado/', CambiarEstadoTurnoStaffView.as_view(), name='cambiar_estado'),
]
