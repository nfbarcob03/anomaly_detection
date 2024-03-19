# Usa la imagen oficial de PostgreSQL como base
FROM postgres

# Variables de entorno para configurar la base de datos
ENV POSTGRES_USER=master
ENV POSTGRES_PASSWORD=master123
ENV POSTGRES_DB=pricing

# Copia el archivo CSV al contenedor
COPY precios_historicos.csv /precios_historicos.csv

# Copia el script SQL para importar los datos
COPY init.sql /docker-entrypoint-initdb.d/init.sql


