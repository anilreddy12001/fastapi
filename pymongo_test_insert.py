# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database
dbname = get_database()
collection_name = dbname["sample_airbnb"]

item_1 = {
  "_id" : "U1IT0009999",
  "listing_url":
"https://www.airbnb.com/rooms/1003530",
"name":
"New York City - Upper West Side Apt",
"summary":
"from python app",
"space":
"Murphy bed, optional second bedroom available. Wifi available, Hulu, N…",
"description":
"Murphy bed, optional second bedroom available. Wifi available, Hulu, N…",
"neighborhood_overview":
"Great neighborhood - many terrific restaurants, bakeries, bagelries. W…",
"notes":
"My cat, Samantha, are in and out during the summer.  The apt is layed …",
"transit":
"Conveniently located near 1, 2, 3, B & C subway lines. Also buses on C…",
"access":
"NYC!",
"interaction":
""
}


collection_name.insert_many([item_1,item_2])
