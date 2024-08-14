FROM postgres:16

#set environment variables for PostgreSQL
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydatabase

#copy SQL scripts into docker image
COPY ../init-scripts: /docker-entrypoint-initdb.d/

#PostgreSQL port
EXPOSE 5432
