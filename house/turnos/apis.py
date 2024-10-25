# turnos/apis.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import Turno
from usuarios.models import Usuario  # Puedes importar el modelo sin crear un ciclo porque aquí no se importa ninguna vista.
from .serializers import TurnoSerializer

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
