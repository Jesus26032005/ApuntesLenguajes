# Guía Básica de Docker para este proyecto

Este archivo explica los pasos básicos para construir y ejecutar el contenedor Docker definido en `dockerfile`.

## 1. Construir la Imagen (Build)

Para crear la imagen de Docker basada en tu `dockerfile`, abre tu terminal en esta carpeta y ejecuta:

```bash
docker build -t mi-app-python .
```

*   `-t mi-app-python`: Asigna un nombre (tag) a tu imagen, en este caso "mi-app-python".
*   `.`: Indica que el `dockerfile` está en el directorio actual.

## 2. Ejecutar el Contenedor (Run)

Una vez construida la imagen, puedes ejecutarla con el siguiente comando:

```bash
docker run mi-app-python
```

Deberías ver la salida de tu script `main.py` (ej. "Hola mundo").

## 3. Comandos Útiles

*   **Ver imágenes creadas:**
    ```bash
    docker images
    ```

*   **Ver contenedores en ejecución:**
    ```bash
    docker ps
    ```

*   **Ver todos los contenedores (incluidos los detenidos):**
    ```bash
    docker ps -a
    ```

*   **Eliminar una imagen:**
    ```bash
    docker rmi mi-app-python
    ```
