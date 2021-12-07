#!/usr/bin/env python3
""" Task(9): a Python function that inserts a new document in a collection based on kwargs """
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """[inserts a new document in a collection based on kwargs]
    Args:
        mongo_collection (mongo): A mongoDB collection
        kwargs: The new documents and values to be added
    """
    new_id = mongo_collection.insert(kwargs)
    return new_id
