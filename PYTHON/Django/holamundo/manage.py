#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'holamundo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


"""
__init__.py: un archivo vacío que le dice a Python que esta carpeta es un paquete de Python.
asgi.py: un punto de entrada para Compatible con ASGI servidores web para atender su proyecto. Por lo general, deja este archivo tal cual, ya que proporciona los enlaces para los servidores web de producción.
configuración.py: contiene configuraciones para el proyecto Django, que usted modifica durante el desarrollo de una aplicación web.
urls.py: contiene un índice del proyecto Django, que también modificas durante el desarrollo.
wsgi.py: un punto de entrada para que los servidores web compatibles con WSGI sirvan a su proyecto. Por lo general, deja este archivo tal cual, ya que proporciona los enlaces para los servidores web de producción.

"""