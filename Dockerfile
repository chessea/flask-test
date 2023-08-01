# Utilizamos la imagen oficial de MySQL desde Docker Hub
FROM mysql:latest

# Establecemos las variables de entorno para configurar la base de datos
ENV MYSQL_ROOT_PASSWORD=my-secret-root-password
ENV MYSQL_DATABASE=my_database
ENV MYSQL_USER=my_user
ENV MYSQL_PASSWORD=my-secret-password

# Opcionalmente, puedes especificar el conjunto de caracteres y la collation para la base de datos
#ENV MYSQL_CHARSET=utf8mb4
#ENV MYSQL_COLLATION=utf8mb4_unicode_ci

# Opcionalmente, puedes copiar un archivo SQL con comandos para inicializar la base de datos
#COPY ./init.sql /docker-entrypoint-initdb.d/

# Exponemos el puerto 3306 para que se puedan realizar conexiones a la base de datos
EXPOSE 3306