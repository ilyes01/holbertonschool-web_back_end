#!/usr/bin/env python3
"""
Script that provides stats about Nginx logs stored in Mongo
"""

import pymongo


def count_documents(collection):
    """Count the number of documents in a collection"""
    return collection.count_documents({})


def count_method_documents(collection, method):
    """Count the number of document in a collection with a given method"""
    return collection.count_documents({"method": method})


def count_status_documents(collection):
    """Count the number of documents in a collection with method=GET and path=/status"""
    return collection.count_documents({"method": "GET", "path": "/status"})


if __name__ == "__main__":
    # Connect to MongoDB
    client = pymongo.MongoClient()
    collection = client.logs.nginx

    # Get stats
    num_logs = count_documents(collection)
    num_get = count_method_documents(collection, "GET")
    num_post = count_method_documents(collection, "POST")
    num_put = count_method_documents(collection, "PUT")
    num_patch = count_method_documents(collection, "PATCH")
    num_delete = count_method_documents(collection, "DELETE")
    num_status = count_status_documents(collection)

    # Print stats
    print(f"{num_logs} logs")
    print("Methods:")
    print(f"\tmethod GET: {num_get}")
    print(f"\tmethod POST: {num_post}")
    print(f"\tmethod PUT: {num_put}")
    print(f"\tmethod PATCH: {num_patch}")
    print(f"\tmethod DELETE: {num_delete}")
    print(f"{num_status} status check")
