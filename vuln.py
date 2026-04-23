import os
import subprocess
import sqlite3
import pickle
from flask import Flask, request, jsonify, redirect
app = Flask(__name__)
@app.route('/ping')
def ping():
    host = request.args.get('host')
    output = subprocess.check_output(f"ping -c 3 {host}", shell=True)
    return output
@app.route('/dns')
def dns():
    domain = request.args.get('domain')
    os.system("nslookup " + domain)
    return "done"
@app.route('/user')
def get_user():
    name = request.args.get('name')
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE name = '" + name + "'")
    return str(c.fetchall())
@app.route('/calc')
def calc():
    expr = request.args.get('expr')
    result = eval(expr)
    return str(result)
@app.route('/load', methods=['POST'])
def load():
    data = request.get_data()
    obj = pickle.loads(data)
    return str(obj)
@app.route('/fetch')
def fetch():
    import requests
    url = request.args.get('url')
    resp = requests.get(url)
    return resp.text
@app.route('/hello')
def hello():
    name = request.args.get('name')
    return "<h1>Hello " + name + "</h1>"
@app.route('/read')
def read_file():
    filename = request.args.get('file')
    f = open("/tmp/" + filename, "r")
    return f.read()
@app.route('/go')
def go():
    url = request.args.get('url')
    return redirect(url)
if __name__ == '__main__':
    app.run(debug=True)
