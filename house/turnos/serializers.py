# house/turnos/serializers.py

from rest_framework import serializers
from .models import Turno  # La importación de Turno está correcta
from usuarios.models import Usuario  # Importar el modelo Usuario desde el módulo de usuarios

# Serializador para el modelo Turno
class TurnoSerializer(serializers.ModelSerializer):
    # Puedes definir también cómo mostrar la información de usuario
    usuario = serializers.SlugRelatedField(slug_field='username', queryset=Usuario.objects.all())
    usuario_staff = serializers.SlugRelatedField(slug_field='username', queryset=Usuario.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Turno
        fields = ['numero_turno', 'fecha_creacion', 'estado', 'usuario', 'usuario_staff']
