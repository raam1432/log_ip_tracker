from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/log", methods=["POST"])
def log():
    with open("visitor_log.csv", "a") as f:
        f.write(request.data.decode("utf-8"))
    print(f"[{datetime.now()}] Visitor Logged")
    return "OK", 200
