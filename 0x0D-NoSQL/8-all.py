#!/usr/bin/env python3
""" Python function """


def list_all(mongo_collection):
    """lists all documents in a collection """
    l = mongo_collection.find()
    return l if l else []
