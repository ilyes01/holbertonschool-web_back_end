#!/usr/bin/env python3
""" module list"""
def insert_school(mongo_collection, **kwargs):
     """documents of all list"""
     return mongo_collection.insert_one(kwargs).inserted_id or None
