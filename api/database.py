"""Module for database connection"""
from pymongo import MongoClient

from exceptions import CollectionNotFound

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

def get_db_collection(db: MongoClient, collection_name: str):
    """
    Get the collection from the database.

    Args:
        db: database connection.
        collection_name: name of the collection.
    Returns:
        collection: collection from the database.
    Exceptions:
        CollectionNotFound. If the collection does not exist.
    """
    if collection_name not in db.list_collection_names():
        raise CollectionNotFound("collection_name")

    return db[collection_name]