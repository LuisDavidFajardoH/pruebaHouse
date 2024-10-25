from django.db import models
from django.conf import settings

class Turno(models.Model):
    # Opciones de estado del turno
    ESTADOS = [
        ('P', 'Pendiente'),
        ('A', 'Activo'),
        ('F', 'Finalizado'),
    ]

    # Definición de los campos del modelo
    numero_turno = models.AutoField(primary_key=True)  # Número de turno único, se autoincrementa
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Fecha y hora de creación del turno
    estado = models.CharField(max_length=1, choices=ESTADOS, default='P')  # Estado del turno con opciones definidas
    
    # Relación con el usuario que creó el turno
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Usuario que solicita el turno
    
    # Relación con el staff que maneja el turno, este campo puede ser nulo
    usuario_staff = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='turnos_staff', on_delete=models.SET_NULL, null=True, blank=True
    )

    # Representación en forma de cadena
    def __str__(self):
        return f"Turno {self.numero_turno} - {self.get_estado_display()}"
