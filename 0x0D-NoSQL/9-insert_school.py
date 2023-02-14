#!/usr/bin/env python3
"""python function"""
from typing import Dict
from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs: Dict) -> str:
    """ function that insert dociment"""
    result = mongo_collection.insert_one(kwargs)
    return str(result.inserted_id)
