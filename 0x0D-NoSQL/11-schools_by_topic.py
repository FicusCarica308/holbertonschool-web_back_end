#!/usr/bin/env python3
""" Task(11): a Python function that returns the list
of school having a specific topic """
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """[returns the list of schools having a specific topic]
    Args:
        mongo_collection (mongo): A mongoDB collection
        topic (str): the topic search
    """
    matching_docs = []
    documents = mongo_collection.find({})
    for doc in documents:
        topics = doc['topics']
        if topic in topics:
            matching_docs.append(doc)
    return matching_docs
