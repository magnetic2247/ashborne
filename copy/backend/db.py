#!/usr/bin/python3
import sqlite3

"""
studli_db by Adrien Genevieve
"""

class Database:
    """
    A simple class that wraps around the sqlite3 module and handles errors
    """
    # Constructor
    def __init__(self, db_filename):
        self.con = sqlite3.connect(db_filename, check_same_thread=False)
        self.con.row_factory = sqlite3.Row # Use sqlite3 Row for iteration

    # Query
    def query(self, query, bindings=[], immediate_commit=True):
        # Attempt Query
        try:
            cur = self.con.cursor()
            cur.execute(query, bindings)
            # Commit Changes
            if immediate_commit: self.con.commit()
        # Handle Errors
        except sqlite3.Error as err:
            print("SQL ERROR:", err)
            return
        # Return results if any
        results = cur.fetchall()

        # Convert Results to JSON
        json_result = {}
        for idx,row in enumerate(results):
            json_result[idx] = dict(row) 
        return json_result

    # Commit Changes
    def commit(self):
        self.con.commit()

    # Destructor
    def __del__(self):
        self.con.close()
