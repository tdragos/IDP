FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD pass
ENV MYSQL_USER adm
ENV MYSQL_PASSWORD pass
ENV MYSQL_DATABASE tema
ADD script.sql /docker-entrypoint-initdb.d
EXPOSE 3306
