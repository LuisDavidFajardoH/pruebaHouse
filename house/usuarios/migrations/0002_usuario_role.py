# Generated by Django 5.1.2 on 2024-10-25 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('cliente', 'Cliente'), ('empleado', 'Empleado')], default='cliente', max_length=20),
        ),
    ]
