#!/usr/bin/env python3
"""python function"""
from typing import Dict
from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs):
    """ function that insert dociment"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
