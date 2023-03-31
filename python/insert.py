import pymongo


if __name__== "__main__":
    print("welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client['office']
    collection = db['emp']
    #insert one
    #dictionary = {'name':'arvind','id':1,'email':'arvind@gmail.com'}
    #collection.insert_one(dictionary)

    #dictionary2 = {'name':'pooja','id':2,'email':'pooja@gmail.com'}
    #collection.insert_one(dictionary2)
        #insert many
    insertThese = [
        {'name':'anand','id':3,'email':'anand@gmail.com','place':'mysore'},
        {'name':'ravi','id':4,'email':'ravi@gmail.com','place':'bidar'},
        {'name':'prema','id':5,'email':'prema@gmail.com','place':'hubli'},
        {'name':'kamala','id':6,'email':'akamala@gmail.com','place':'banglore'},
        {'name':'roohi','id':7,'email':'roohi@gmail.com','place':'bagalkot'}
    ]
    collection.insert_many(insertThese)