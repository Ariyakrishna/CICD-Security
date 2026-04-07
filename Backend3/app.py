from flask import Flask, jsonify
from flask_cors import CORS   # 👈 ADD THIS
import socket

app = Flask(__name__)
CORS(app)   # 👈 ADD THIS (fixes CORS)

@app.route("/api3")
def api3():
    return jsonify({
        "service": "backend3",
        "pod": socket.gethostname()
    })

app.run(host="0.0.0.0", port=5000)