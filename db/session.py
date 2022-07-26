from utils.config import DATABASE_URI
from pymongo import MongoClient


myclient = MongoClient(DATABASE_URI)
myDB = myclient["gold_price"]

