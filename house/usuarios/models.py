from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    celular = models.CharField(max_length=20)
    identificacion = models.CharField(max_length=15, unique=True)
    foto_perfil = models.ImageField(upload_to='perfiles/', blank=True, null=True)

    # Opciones de roles
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('cliente', 'Cliente'),
        ('empleado', 'Empleado'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='cliente')

    # Añadir related_name para evitar conflictos con auth.User
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Añadir related_name para evitar conflicto
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Añadir related_name para evitar conflicto
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_role_display()})"
