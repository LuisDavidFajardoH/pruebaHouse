from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView
from .models import Turno
from django.urls import reverse_lazy

# Solo los usuarios autenticados pueden acceder a esta vista
class TurnoListView(LoginRequiredMixin, ListView):
    model = Turno
    template_name = 'turnos/listar_turnos.html'
    login_url = 'login'  # Redirigir al inicio de sesión si no está autenticado

# Solo los usuarios autenticados pueden acceder a esta vista
class TurnoCreateView(LoginRequiredMixin, CreateView):
    model = Turno
    fields = ['usuario', 'estado']
    template_name = 'turnos/form_turno.html'
    success_url = reverse_lazy('turnos:listar')
    login_url = 'login'  # Redirigir al inicio de sesión si no está autenticado

# Solo los usuarios autenticados con permisos pueden acceder a esta vista
class TurnoUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Turno
    fields = ['estado', 'usuario_staff']
    template_name = 'turnos/form_turno.html'
    success_url = reverse_lazy('turnos:listar')
    login_url = 'login'  # Redirigir al inicio de sesión si no está autenticado
    permission_required = 'turnos.change_turno'  # Verifica que el usuario tenga permiso para cambiar turnos

class CambiarEstadoTurnoStaffView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Turno
    fields = ['estado']
    template_name = 'turnos/cambiar_estado_turno.html'
    success_url = reverse_lazy('turnos:listar')
    login_url = 'login'  # Redirigir al inicio de sesión si no está autenticado

    # Esta función verifica si el usuario tiene permisos de staff
    def test_func(self):
        return self.request.user.is_staff

