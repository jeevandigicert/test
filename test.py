from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/run")
def run():
    cmd = request.args.get("cmd", "")
    subprocess.call(cmd, shell=True)  # intentionally vulnerable for CodeQL test
    return "done"
