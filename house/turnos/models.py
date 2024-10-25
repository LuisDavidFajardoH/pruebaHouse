from django.conf import settings
from django.db import models

class Turno(models.Model):
    ESTADOS = [
        ('P', 'Pendiente'),
        ('A', 'Activo'),
        ('F', 'Finalizado'),
    ]

    numero_turno = models.AutoField(primary_key=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=1, choices=ESTADOS, default='P')
    
    # Asegúrate de que settings.AUTH_USER_MODEL está correctamente configurado para el modelo de usuario personalizado
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    usuario_staff = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='turnos_staff', on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"Turno {self.numero_turno} - {self.get_estado_display()}"
