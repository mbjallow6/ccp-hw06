
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://mbjallow:9959923Mbj@cluster0.xdaah0a.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


# settup the database
def get_database():
    db = client['experiments_db']
    return db

# get collection
def get_collection():
    db = get_database()
    return db['experiments_collections']



# db = client['experiments_db']
# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)