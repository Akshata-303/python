import pymongo


if __name__== "__main__":
    print("welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017")

    db = client['office']
    collection = db['emp']

    #delete one
    #rec = {"name":"kamala"}
    #collection.delete_one(rec)

    #delete many

    rec = {"name":"pooja"}
    up = collection.delete_many(rec)
    print(up.deleted_count)
   