"""The above code is importing the necessary libraries for the program to run.
"""
import socket
import os
from dotenv import load_dotenv
from kafka import KafkaProducer

load_dotenv()

socket_connection = socket.socket()
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
socket_connection.connect((HOST, int(PORT)))
bootstrap_servers =os.getenv("bootstrap_servers")


PRODUCER = KafkaProducer(bootstrap_servers=bootstrap_servers, retries=5)

TOPIC_NAME = ("devicedata")

while True:
    try:
        DATA = socket_connection.recv(70240)
        PRODUCER.send(TOPIC_NAME, DATA)

    except Exception as exception:
        print(exception)
socket_connection.close()




