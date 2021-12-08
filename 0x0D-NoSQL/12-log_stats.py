#!/usr/bin/env python3
""" Task(12): a Python script that provides some stats
about Nginx logs stored in MongoDB """
from pymongo import MongoClient


if __name__ == "__main__":
    """ Script """
    DB_CLIENT = MongoClient()
    logs_db = DB_CLIENT.logs
    nginx_collection = logs_db.nginx
    document_count = nginx_collection.find().count()
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("{} logs".format(document_count))
    print("Methods:")
    for meth in method:
        print("    method {}: {}".format(meth, nginx_collection.count_documents({"method": meth})))
    status = nginx_collection.count_documents({"path": "/status"})
    print("{} status check".format(status))
