from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroUsuarioForm(UserCreationForm):
    role = forms.ChoiceField(choices=Usuario.ROLE_CHOICES, label='Rol')

    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'celular', 'identificacion', 'foto_perfil', 'role']

    def clean_identificacion(self):
        identificacion = self.cleaned_data.get('identificacion')
        if not identificacion:
            raise forms.ValidationError('La identificación es un campo obligatorio.')
        if Usuario.objects.filter(identificacion=identificacion).exists():
            raise forms.ValidationError('Esta identificación ya está registrada.')
        return identificacion

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = self.cleaned_data['role']
        if commit:
            user.save()
        return user
