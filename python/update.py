import pymongo


if __name__== "__main__":
    print("welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['office']
    collection = db['emp']


    prev = {"name":"arvind"}
    nextt = {'$set': {"place":"mumbai"}}
    up = collection.update_many(prev, nextt)
    print(up.modified_count)
   
    