# Proyecto Django CRUD

Este proyecto contiene una aplicacion de ejemplo en Django que implementa operaciones CRUD usando Bootstrap para los estilos y SweetAlert2 para las alertas.

## Requisitos

- Python 3.10 o superior
- Dependencias listadas en `requirements.txt`

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

## Ejecucion

Aplica las migraciones y ejecuta el servidor de desarrollo:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Luego abre `http://localhost:8000/` en tu navegador para interactuar con el CRUD de Items.

