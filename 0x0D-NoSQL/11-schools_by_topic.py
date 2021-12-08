#!/usr/bin/env python3
""" Task(11): a Python function that returns the list of school having a specific topic """
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """[returns the list of schools having a specific topic]
    Args:
        mongo_collection (mongo): A mongoDB collection
        topic (str): the topic search
    """
    return mongo_collection.find_many({"topic": topic})
