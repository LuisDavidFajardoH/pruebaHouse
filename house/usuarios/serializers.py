# usuarios/serializers.py
from rest_framework import serializers
from turnos.models import Turno  # Cambia esta importación al módulo correcto
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'celular', 'identificacion', 'foto_perfil']

class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ['numero_turno', 'fecha_creacion', 'estado', 'usuario', 'usuario_staff']
