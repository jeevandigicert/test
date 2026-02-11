from flask import Flask, request
import os
import sqlite3

app = Flask(__name__)
# harmless change to re-run CodeQL
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    cursor.execute(query)

    return "Login attempted"

@app.route("/ping")
def ping():
    host = request.args.get("host")
    os.system("ping -c 1 " + host)
    return "Pinged"

if __name__ == "__main__":
    app.run()
