import pymongo
import certifi


client = pymongo.MongoClient("mongodb://admin:supersecurePass1@localhost:27017")
ca = certifi.where()

def dbConnection():
    try:
        db = client["users"]
    except ConnectionError:
        print("Error connection to bdd")
    return db