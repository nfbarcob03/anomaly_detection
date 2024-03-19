# Utiliza una imagen de Python como base
FROM python:3.10-alpine

# Actualiza pip
RUN pip install --no-cache-dir --upgrade pip

# Instala las dependencias necesarias
RUN apk update && apk add --no-cache postgresql-dev gcc python3-dev musl-dev 

# Instala las herramientas de compilación necesarias
RUN apk add --no-cache build-base

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al directorio de trabajo
COPY requirements.txt requirements.txt

# Instala las dependencias definidas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación al directorio de trabajo
COPY . .

# Comando por defecto que se ejecutará cuando se inicie el contenedor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
