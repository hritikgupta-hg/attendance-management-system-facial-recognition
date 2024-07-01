
# import pymongo



# if __name__ == "__main__":
#     print('Welcome to pymongo')
#     client = pymongo.MongoClient("mongodb+srv://hritikgupta:brApNtuVlM5df5Td@cluster0.jzgagdf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
#     print(client)
#     try:
#         client.admin.command('ping')
#         print("Pinged your deployment. You successfully connected to MongoDB!")
#     except Exception as e:
#         print(e)

import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

print(pymongo.__version__)

uri = "mongodb+srv://hritikgupta:brApNtuVlM5df5Td@cluster0.jzgagdf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'), tls=True, tlsAllowInvalidCertificates=True)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("error")
    print(e)


# Select the database
db = client['mydatabase']

# Select the collection
collection = db['mycollections']

# # Example data to be inserted
# document = {
#     "name": "John Doe",
#     "email": "john.doe@example.com",
#     "age": 30,
#     "city": "New York"
# }

# # Insert a single document
# result = collection.insert_one(document)
# print("Inserted document with _id:", result.inserted_id)

# Export the database and collection
__all__ = ['db', 'collection']