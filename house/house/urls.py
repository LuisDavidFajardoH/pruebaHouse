from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from usuarios.views import RegistroUsuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('turnos/', include(('turnos.urls', 'turnos'), namespace='turnos')),
    path('usuarios/', include('usuarios.urls')),  # Incluye las URLs de la app 'usuarios'
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/registro/', RegistroUsuario.as_view(), name='registro'),
]
