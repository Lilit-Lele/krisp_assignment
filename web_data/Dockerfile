# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . /usr/src/app

RUN pip install requests psycopg2-binary flask pandas

# Run the Python script when the container launches
CMD ["python", "./generate_data.py"]
