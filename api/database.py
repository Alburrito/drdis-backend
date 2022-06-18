"""Module for database connection"""
from pymongo import MongoClient

BUG_REPORTS_COLLECTION = "bug_reports"

def connect_to_mongo_database(host: str, port: int, db_name: str):
    """
    Connect to the mongo client.

    Args:
        host: hostname of the mongo client.
        port: port of the mongo client.
        db_name: name of the database.
    """
    client = MongoClient(host, port)
    db = client[db_name]
    return db
