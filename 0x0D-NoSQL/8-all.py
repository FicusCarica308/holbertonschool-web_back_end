#!/usr/bin/env python3
""" Task(8): a Python function that lists all documents in a collection """
from pymongo import MongoClient


def list_all(mongo_collection):
    """[Lists all the documents from a given collection]
    Args:
        mongo_collection (mongo): A mongoDB collection
    """
    docs = mongo_collection.find({})
    return docs if docs != 0 else []
