#!/usr/bin/env python3
""" Top students module """
import pymongo


def top_students(mongo_collection):
    """ Return all students sorted by average score """
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ]
    return mongo_collection.aggregate(pipeline)
