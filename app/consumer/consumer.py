"""The above code is importing the necessary libraries for the program to run.
"""
import os
import json
import sys
import pymongo
from kafka import KafkaConsumer
from dotenv import load_dotenv
load_dotenv()

CLIENT = pymongo.MongoClient(os.getenv("mongodbUri"))
DB = CLIENT['scmxpertlite']
DATA_STREAM = DB["devicedata"]

TOPIC_NAME = os.getenv("topic_name")
bootstrap_servers=os.getenv("bootstrap_servers")

try:
    CONSUMER = KafkaConsumer(TOPIC_NAME, bootstrap_servers=bootstrap_servers,\
                              auto_offset_reset='latest')
    for DATA in CONSUMER:
        try:
            DATA = json.loads(DATA.value)
            mdata = DATA_STREAM.insert_one(DATA)
        except json.decoder.JSONDecodeError:
            continue
except KeyboardInterrupt:
    sys.exit()





    

