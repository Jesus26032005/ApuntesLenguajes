# Guía Docker para Aplicaciones Web en Python (Flask/Django)

Esta guía explica cómo dockerizar una aplicación web tradicional, usando Flask como ejemplo.

## 1. Estructura del Proyecto
```
mi-web-app/
├── app.py
├── templates/
├── static/
├── requirements.txt
└── Dockerfile
```

## 2. Ejemplo de Dockerfile (Flask)

```dockerfile
# Imagen base
FROM python:3.9-slim

# Directorio de trabajo
WORKDIR /app

# Copiar dependencias e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código fuente
COPY . .

# Exponer el puerto donde corre la app (Flask usa 5000 por defecto)
EXPOSE 5000

# Comando de ejecución
# host=0.0.0.0 es CRUCIAL para que sea accesible desde fuera del contenedor
CMD ["python", "app.py"] 
# O si usas Gunicorn (producción):
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

## 3. Código de ejemplo (app.py)
Asegúrate de que tu app escuche en `0.0.0.0`:

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "¡Hola desde Docker Web!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## 4. Construir y Correr con Puertos

**Construir:**
```bash
docker build -t mi-web-app .
```

**Correr (Mapeando puertos):**
```bash
docker run -p 8080:5000 mi-web-app
```
*   `-p 8080:5000`: Redirige el puerto 8080 de tu máquina al puerto 5000 del contenedor.
*   Ahora puedes ver tu web en: `http://localhost:8080`
