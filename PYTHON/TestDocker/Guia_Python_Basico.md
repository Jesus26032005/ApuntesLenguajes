# Guía Docker para Scripts Básicos de Python

Esta guía explica cómo crear un contenedor para scripts simples de Python (scripts de consola, procesamiento de datos, automatización, etc.).

## 1. Estructura del Proyecto
```
mi-proyecto/
├── main.py
├── requirements.txt (si tienes dependencias)
└── Dockerfile
```

## 2. Ejemplo de Dockerfile

```dockerfile
# Usar una imagen oficial de Python ligera (slim o alpine)
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias primero (para aprovechar la caché de Docker)
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Comando por defecto al ejecutar el contenedor
CMD ["python", "main.py"]
```

## 3. Ejemplo de requirements.txt
Si usas librerías externas (como `requests` o `pandas`), ponlas aquí:
```text
requests
pandas
```

## 4. Construir y Correr

**Construir:**
```bash
docker build -t mi-script-python .
```

**Correr:**
```bash
docker run --rm mi-script-python
```
*(La opción `--rm` elimina el contenedor automáticamente después de que termina de ejecutarse, útil para scripts de un solo uso).*
