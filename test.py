import sqlite3
from flask import request

def login():
    username = request.args.get("user")
    password = request.args.get("pass")

    conn = sqlite3.connect("db.sqlite")
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    conn.execute(query)   # SQL Injection
