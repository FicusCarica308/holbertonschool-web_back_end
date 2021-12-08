#!/usr/bin/env python3
""" Task(10): a Python function that changes all topics of a school document based on the name """
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """[changes all topics of a school document based on the name passed]
    Args:
        mongo_collection (mongo): A mongoDB collection
        name (str): the name of the document to be edited
        topics (list(str)): A list of new topis to be edited on the document
    """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
