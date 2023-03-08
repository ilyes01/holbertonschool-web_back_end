#!/usr/bin/env python3
""" documents module """
def schools_by_topic(mongo_collection, topic):
    """
    Return schoolss list  from the provided Mongodb collection that have the
    given topic in the topics field

    Arguments
    topic The topic to search for
    Return
    A list of dictionarie represent the school matching thhe search criteria
    """
    return list(mongo_collection.find({'topics': topic}))
