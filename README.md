# krisp_assignment
Assignment for Associate Data Engineer role

Assignment 1: data ingestion pipeline

| **File/Directory**               | **Description**                                                                                   |
|----------------------------------|---------------------------------------------------------------------------------------------------|
| `.vscode/`                       | Directory containing Visual Studio Code configuration files for the project.                      |
| `database/`                      | Directory containing files related to database setup and configuration.                           |
| &emsp;`database/Dockerfile`          | Dockerfile for the database service, specifying the environment for the PostgreSQL container.     |
| `init-scripts/`                  | Directory for database initialization scripts that run when the PostgreSQL container starts.      |
| &emsp;`init-scripts/data_tables.sql` | SQL script for creating necessary tables in the PostgreSQL database.                              |
| `web_data/`                      | Directory containing the web application files,Flask-related code and templates.                  |
| &emsp;`web_data/templates/`          | Directory for HTML templates used by the Flask application.                                       |
| &emsp;`web_data/templates/index.html`| HTML file that displays data from the database on the web interface.                              |
| &emsp;`web_data/Dockerfile`          | Dockerfile for the web service, specifying the environment for the Flask application container.   |
| `generate_data.py`               | Python script responsible for generating and inserting random data into the PostgreSQL database.  |
| `docker-compose.yml`             | YAML file for Docker Compose, used to define and run multi-container Docker applications.         |
| `Dockerfile` (root level)        | Dockerfile for the main application container, typically the web application.                     |
| `query_database.py`              | Python script that queries the PostgreSQL database to retrieve and manipulate data.               |

i probably do not need the query_databse.py with it's docker



