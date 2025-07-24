import requests
from flask import Flask, request
app = Flask(__name__)

@app.route("/log", methods=["POST"])
def log():
    ip, timestamp = request.data.decode("utf-8").strip().split(',')
    response = requests.post("https://api.sheetbest.com/sheets/47c67199-ce3f-4b24-964e-3a126012bc6f", json={
        "IP Address": ip,
        "Timestamp": timestamp
    })
    return "Logged to Google Sheet", 200
