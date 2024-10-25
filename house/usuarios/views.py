#Usuarios/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from turnos.models import Turno
from .forms import RegistroUsuarioForm
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from .serializers import TurnoSerializer

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

# API para validar la existencia de un usuario por identificación
class UsuarioExistenciaAPIView(APIView):
    permission_classes = [AllowAny]  # Permite acceso anónimo

    def get(self, request, identificacion):
        try:
            usuario = Usuario.objects.get(identificacion=identificacion)
            return Response({"exists": True, "message": "Usuario encontrado"}, status=status.HTTP_200_OK)
        except Usuario.DoesNotExist:
            return Response({"exists": False, "message": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

# Endpoint para listar todos los turnos
class TurnoListAPIView(APIView):
    permission_classes = [AllowAny]  # Permite acceso anónimo

    def get(self, request):
        turnos = Turno.objects.all()
        serializer = TurnoSerializer(turnos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ListarPacientesView(ListView):
    model = Usuario
    template_name = 'usuarios/listar_pacientes.html'
    context_object_name = 'pacientes'

    def get_queryset(self):
        # Listar todos los pacientes (usuarios)
        return Usuario.objects.all()