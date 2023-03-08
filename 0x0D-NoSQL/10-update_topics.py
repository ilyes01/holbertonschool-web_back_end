#!/usr/bin/env python3
""" Update topics for a document(s) module """

def update_document_topics(collection, document_name, topics):
    """
    Update the 'topics' field for document(s) in the MongoDB collection with the
    provided 'document_name' with the given 'topics' list.

    Arguments:
    collection -- The MongoDB collection to update.
    document_name -- The name of the document(s) to update.
    """
    collection.update_many(
        {'name': document_name},
        {'$set': {'topics': topics}}
    )
