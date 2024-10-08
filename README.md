# krisp_assignment
Assignment for Associate Data Engineer role

Assignment 1: data ingestion pipeline

To run these containers, clone this repository and run 
``` docker compose up --build ```
from this repository folder from the docker terminal.
For shuttting down run
``` docker compose down ```

Below you can see the repository structure. The data tables are made with the sql script in database/init-scripts folder. Scripts in the web_data folder are used to make a Flask web application that interacts with a PostgreSQL database and displays user, session, and metrics data tables according to the templete. 

| **File/Directory**                  | **Description**                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| `.vscode/`                          | Directory containing Visual Studio Code configuration files for the project.                      |
| `database/`                         | Directory containing files related to database setup and configuration.                           |
| &emsp;`database/Dockerfile`          | Dockerfile for the database service, specifying the environment for the PostgreSQL container.     |
| `init-scripts/`                  | Directory for database initialization scripts that run when the PostgreSQL container starts.      |
| &emsp;`init-scripts/data_tables.sql` | SQL script for creating necessary tables in the PostgreSQL database.                              |
| `web_data/`                      | Directory containing the web application files, Flask-related code and templates.                  |
| &emsp;`web_data/templates/`          | Directory for HTML templates used by the Flask application.                                       |
| &emsp; &emsp;`web_data/templates/index.html`| HTML file that displays data from the database on the web interface.                              |
| &emsp;`web_data/Dockerfile`          | Dockerfile for the web service, specifying the environment for the Flask application container.   |
| &emsp;`web_data/generate_data.py`    | Python script responsible for generating and inserting random data into the PostgreSQL database.  |
| `docker-compose.yml`             | YAML file for Docker Compose, used to define and run multi-container Docker applications.         |


To connect another container to the postgress database these parameters should be used, connection will be possible given the new container has access to the same network.
```
conn = psycopg2.connect(
    dbname="mydatabase",
    user="myuser",
    password="mypassword",
    host="postgres",  
    port="5432"
)
```

Further steps
- add the built docker to docker hub
- make flask parameterized routes for each user
