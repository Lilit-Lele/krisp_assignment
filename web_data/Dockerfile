FROM python:3.9-slim

WORKDIR /usr/src/app

#copy the current directory contents into the container
COPY . /usr/src/app

RUN pip install requests psycopg2-binary flask pandas

#run the py script when the container launches
CMD ["python", "./generate_data.py"]
