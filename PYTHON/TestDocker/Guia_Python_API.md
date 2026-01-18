# Guía Docker para APIs en Python (FastAPI)

Esta guía se enfoca en crear contenedores para APIs modernas y rápidas, usando FastAPI y Uvicorn como ejemplo, que es el estándar actual para APIs en Python.

## 1. Estructura
```
mi-api/
├── main.py
├── requirements.txt
└── Dockerfile
```

## 2. Ejemplo de Dockerfile (FastAPI)

```dockerfile
# Usar imagen base
FROM python:3.9-slim

# Directorio de trabajo
WORKDIR /code

# Instalar dependencias
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copiar código de la API
COPY ./main.py /code/

# Exponer puerto (FastAPI/Uvicorn usan 8000 por defecto)
EXPOSE 8000

# Comando para iniciar con Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 3. requirements.txt
Necesitarás `fastapi` y un servidor como `uvicorn`.
```text
fastapi
uvicorn
```

## 4. Código ejemplo (main.py)

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensaje": "Hola desde la API en Docker"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

## 5. Construir y Correr

**Construir:**
```bash
docker build -t mi-api-python .
```

**Correr:**
```bash
docker run -p 8000:8000 mi-api-python
```

*   Accede a la API en: `http://localhost:8000`
*   Documentación automática (Swagger): `http://localhost:8000/docs`
