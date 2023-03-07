#!/usr/bin/env python3
def insert_school(mongo_collection, **kwargs):
    new_document = {}
    for key, value in kwargs.items():
        new_document[key] = value

    result = mongo_collection.insert_one(new_document)

    return result.inserted_id
