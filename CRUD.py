# Corey Denny
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    #"" CRUD operations for Anmal collection in MongoDB """
    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to access the
        # MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:47543/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
        self.database = self.client['AAC']
        
    # Method to implement create commands for database
    def create(self, data):
        if data is not None and type(data) == dict: 
            self.database.animals.insert(data)   # data should be dictionary
            return True
        else:
            print("Nothing was saved.\n")
            return False
            
    # Method to implement read commands for database
    def read(self, query):
        #data = ""
        if query is not None:
            return self.database.animals.find(query, {"_id": False})
   
        else: 
            failMessage = print("\nNo entry found.")
            return failMessage
        
    # Method to implement update commands for database
    def update(self, oldInfo, newInfo):
        if oldInfo is not None and newInfo is not None:
            if self.database.animals.find(oldInfo).count() > 0:
                self.database.animals.update_many(oldInfo, newInfo)
                passMessage = print("Entry found and updated.")
                return passMessage
            else: 
                failMessage = print("No entry found to update.")
                return failMessage
        
    # Method to implement delete commands for database
    def delete(self, data):
        if data is not None:
            if self.database.animals.find(data).count() > 0: 
                deletedData = self.database.animals.delete_many(data)
                passMessage = print("\nEntry found and deleted.")
                return passMessage
            else:
                failMessage = print("\nNo entry found to delete.")
                return failMessage