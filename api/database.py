"""Module for database connection"""
from os import environ
from pymongo import MongoClient

# CONSTANTS
BUG_REPORTS_COLLECTION = "bug_reports"

# ENV VARIABLES
host = environ.get("DB_HOST", 'localhost')
port = int(environ.get("DB_PORT", '27017'))
db_name = environ.get("DB_NAME", "bug_reports_db")

# CLIENT AND DATABASE CONNECTION
client = MongoClient(host, port)
conn_db = client[db_name]

# COLLECTIONS
if BUG_REPORTS_COLLECTION in conn_db.list_collection_names():
    reports_collection = conn_db[BUG_REPORTS_COLLECTION]
else:
    reports_collection = conn_db.create_collection(BUG_REPORTS_COLLECTION)