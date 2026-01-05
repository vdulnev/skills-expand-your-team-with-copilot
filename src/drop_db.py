#!/usr/bin/env python3
"""
Script to drop the MongoDB database
Run: python drop_db.py
"""

from backend import database

if __name__ == "__main__":
    print("Dropping database 'mergington_high'...")
    database.drop_database()
    print("Database dropped successfully!")
