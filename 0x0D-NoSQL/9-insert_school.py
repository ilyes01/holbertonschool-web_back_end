#!/usr/bin/env python3
from typing import Dict
from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs: Dict) -> str:
    result = mongo_collection.insert_one(kwargs)
    return str(result.inserted_id)
