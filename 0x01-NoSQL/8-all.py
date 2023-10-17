#!/usr/bin/env python3
def list_all(mongo_collection):
    ''' Use the find method to retrieve all documents from the collection'''
    documents = list(mongo_collection.find({}))

    return documents

if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
