from pymongo import MongoClient
def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://admin:v83gMU4ndOYVMHyy@cluster0.axbm8sf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
#"mongodb+srv://admin:pwd@cluster0.mongodb.net/"
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING, server_api=ServerApi('1'))
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['user_shopping_list']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()
