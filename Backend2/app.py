from flask import Flask, jsonify
from flask_cors import CORS   # 👈 ADD THIS
import socket

app = Flask(__name__)
CORS(app)   # 👈 ADD THIS (fixes CORS)

@app.route("/api2")
def api2():
    return jsonify({
        "service": "backend2",
        "pod": socket.gethostname()
    })

app.run(host="0.0.0.0", port=5000)