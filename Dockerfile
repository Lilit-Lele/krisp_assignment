# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install the requests library
RUN pip install requests
RUN pip install psycopg2-binary

# Run the Python script when the container launches
CMD ["python", "./query_database.py"]
