FROM postgres:16

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydatabase

# Copy SQL scripts into the Docker image
COPY ../init-scripts: /docker-entrypoint-initdb.d/

# Expose PostgreSQL port
EXPOSE 5432
