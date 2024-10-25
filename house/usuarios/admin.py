from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Registra el modelo de Usuario en el admin
@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('celular', 'identificacion', 'foto_perfil', 'role')}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'role']
