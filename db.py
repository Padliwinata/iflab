from pymongo import MongoClient
from settings import *


try:
    client = MongoClient(host=DOCKER_HOST, port=DOCKER_PORT)
    print('Connected successfully!')
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit()

db = client[DATABASE_NAME]
