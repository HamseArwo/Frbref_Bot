import pymongo
from pymongo import MongoClient


class DataBaseConnection ():
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client["Premier_League"]
        self.team_collection = self.db["Teams"]
        self.player_collection = self.db["Players"]
        self.gk_collection = self.db["Gk"]
