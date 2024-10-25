from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from .forms import RegistroUsuarioForm
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django.urls import reverse_lazy

# Solo los usuarios autenticados pueden acceder a esta vista
class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = 'usuarios/lista_usuarios.html'
    login_url = 'login'  # Redirigir al inicio de sesión si no está autenticado

# Solo los usuarios autenticados pueden acceder a esta vista
class UsuarioCreateView(LoginRequiredMixin, CreateView):
    model = Usuario
    fields = ['username', 'first_name', 'last_name', 'email', 'celular', 'identificacion', 'foto_perfil']
    template_name = 'usuarios/form_usuario.html'
    success_url = reverse_lazy('usuarios:listar')
    login_url = 'login'  # Redirigir al inicio de sesión si no está autenticado

# Solo los usuarios autenticados pueden acceder a esta vista
class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ['username', 'first_name', 'last_name', 'email', 'celular', 'identificacion', 'foto_perfil']
    template_name = 'usuarios/form_usuario.html'
    success_url = reverse_lazy('usuarios:listar')
    login_url = 'login'  # Redirigir al inicio de sesión si no está autenticado

# Registro de usuarios
class RegistroUsuario(CreateView):
    model = Usuario
    form_class = RegistroUsuarioForm  # Usar el nuevo formulario que has creado
    template_name = 'registration/registro.html'  # La plantilla de registro
    success_url = reverse_lazy('login')  # Redirigir al login después del registro exitoso