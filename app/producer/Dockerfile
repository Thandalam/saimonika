
# Base image
FROM python:3.8.10

# Copy the producer file to the container
COPY . /scmxpertlite/scmxpert/app/producer

# Set the working directory
WORKDIR /scmxpertlite/scmxpert/app/producer

RUN pip3 install python-dotenv kafka-python

# Run the socket server
CMD ["python3", "producer.py"]
