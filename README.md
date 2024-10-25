
# Sistema de Creación y Asignación de Turnos

Este es un sistema de gestión de turnos desarrollado utilizando Django y PostgreSQL, con funcionalidades que permiten crear y asignar turnos a usuarios y staff. El sistema cuenta con un backend robusto y una interfaz web amigable utilizando HTML y Bootstrap.

## Características

- CRUD completo para **Usuarios** y **Turnos**.
- Sistema de autenticación y permisos para definir roles (usuarios y staff).
- Uso de **Class-based Views (CBV)** para una mayor mantenibilidad.
- **APIs REST** para la validación de usuarios y la consulta de turnos.
- Frontend basado en **Bootstrap** con preprocesamiento de CSS usando **Sass**.

## Tecnologías Utilizadas

- **Python 3.12**
- **Django 5.1.2**
- **PostgreSQL**
- **Django REST Framework**
- **Webpack**
- **Git**

## Instalación y Ejecución Local

Sigue los siguientes pasos para levantar el entorno localmente.

### 1. Clonar el Repositorio

```sh
$ git clone <repositorio>
$ cd <directorio_del_proyecto>
```

### 2. Crear un Entorno Virtual e Instalar Dependencias

```sh
$ python -m venv venv
$ source venv/bin/activate  # En Windows: venv\Scripts\activate
$ pip install -r requirements.txt
```

### 3. Configurar la Base de Datos

Asegúrate de tener PostgreSQL instalado y funcionando. Configura la base de datos en `house/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_base_datos',
        'USER': 'usuario_bd',
        'PASSWORD': 'password_bd',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 4. Realizar las Migraciones

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

### 5. Crear un Superusuario

```sh
$ python manage.py createsuperuser
```

### 6. Correr el Servidor de Desarrollo

```sh
$ python manage.py runserver
```

La aplicación estará disponible en `http://127.0.0.1:8000/`.

## Ejecutar Pruebas

Para ejecutar las pruebas unitarias y de integración, corre el siguiente comando:

```sh
$ python manage.py test
```

Asegúrate de que todas las pruebas pasen antes de desplegar cualquier cambio.

## Estrategia de Git

- **`main`**: Rama principal para la versión estable.
- **`develop`**: Rama de desarrollo, donde se integran todas las nuevas funcionalidades antes de pasar a producción.

## Estructura del Proyecto

- **house/**: Carpeta principal del proyecto Django.
  - **usuarios/**: Aplicación que maneja la gestión de usuarios.
  - **turnos/**: Aplicación que maneja la creación y asignación de turnos.
  - **templates/**: Contiene las plantillas HTML para las vistas de la aplicación.
  - **static/**: Archivos estáticos (CSS, JS, imágenes).

## Notas de Seguridad

- **Protección CSRF**: Todos los formularios están protegidos contra ataques CSRF.
- **Autenticación y Permisos**: Se usa el sistema de autenticación de Django para restringir el acceso a las vistas según los roles y permisos del usuario.

## Mejoras Sugeridas

- **Optimizar Consultas a la Base de Datos**: Usar `select_related()` o `prefetch_related()` para mejorar la eficiencia de las consultas.
- **Implementar Caché**: Utilizar cacheo para optimizar las vistas que se acceden con frecuencia.

## Contribución

Las contribuciones son bienvenidas. Para contribuir:

1. Haz un fork del proyecto.
2. Crea una rama para tu función (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -am 'Agrega nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.

