# Utiliza una imagen de Python como base
FROM python:3.10-alpine
RUN pip install --no-cache-dir --upgrade pip
RUN apk update && apk add --no-cache postgresql-dev gcc python3-dev musl-dev 
RUN apk add --no-cache build-base
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
