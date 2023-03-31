import pymongo


if __name__== "__main__":
    print("welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['office']
    collection = db['emp']
    #one = collection.find_one({'name':'arvind'})
    #print(one)
    alldoc = collection.find({'name':'arvind', 'id':{"$lte":4}})
   # print(alldoc.count_documents('names'))
    print(collection.count_documents({'name':'arvind', 'id':{"$lte":4}}))
    for item in alldoc:
        print(item)
    
    