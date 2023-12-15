from pymongo import MongoClient

docker_host = '10.20.224.5'
docker_port = 27017

database_name = 'iflab_db'
collection_name = 'aslab'

try:
    client = MongoClient(host=docker_host, port=docker_port)
    print('Connected successfully!')
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    exit()

db = client[database_name]

collection = db[collection_name]

