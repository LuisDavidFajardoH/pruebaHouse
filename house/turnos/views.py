# turnos/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .models import Turno

User = get_user_model()

# Vista para listar turnos (solo usuarios autenticados)
class TurnoListView(LoginRequiredMixin, ListView):
    model = Turno
    template_name = 'turnos/listar_turnos.html'
    context_object_name = 'turnos'
    login_url = 'login'
    ordering = ['-fecha_creacion']

    def get_queryset(self):
        if self.request.user.is_staff:
            return Turno.objects.all()
        else:
            return Turno.objects.filter(usuario=self.request.user)

# Vista para crear un nuevo turno
class TurnoCreateView(LoginRequiredMixin, CreateView):
    model = Turno
    fields = ['estado', 'usuario']
    template_name = 'turnos/form_turno.html'
    success_url = reverse_lazy('turnos:listar')
    login_url = 'login'

    def form_valid(self, form):
        usuario_asignado = form.cleaned_data['usuario']
        if not usuario_asignado:
            form.add_error('usuario', 'Por favor, seleccione un usuario válido.')
        return super().form_valid(form)

# Vista para editar un turno existente (modificar estado)
class TurnoUpdateView(LoginRequiredMixin, UpdateView):
    model = Turno
    fields = ['estado', 'usuario_staff']
    template_name = 'turnos/form_turno.html'
    success_url = reverse_lazy('turnos:listar')
    login_url = 'login'

# Vista para cambiar el estado del turno, accesible solo para el staff
class CambiarEstadoTurnoStaffView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Turno
    fields = ['estado']
    template_name = 'turnos/form_cambiar_estado.html'
    success_url = reverse_lazy('turnos:listar')
    login_url = 'login'
    permission_required = 'turnos.change_turno'

    def form_valid(self, form):
        form.instance.usuario_staff = self.request.user
        return super().form_valid(form)
