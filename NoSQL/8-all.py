#!/usr/bin/env python3
" Python function that lists all documents in a collection "

def list_all(mongo_collection):
    """Return a list of all documents."""
    return list(mongo_collection.find())
