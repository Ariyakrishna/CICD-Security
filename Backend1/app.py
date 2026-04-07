from flask import Flask, jsonify
from flask_cors import CORS   # 👈 ADD THIS
import socket

app = Flask(__name__)
CORS(app)   # 👈 ADD THIS (fixes CORS)

@app.route("/api1")
def api1():
    return jsonify({
        "service": "backend1",
        "pod": socket.gethostname()
    })

app.run(host="0.0.0.0", port=5000)