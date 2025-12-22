from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    app_name = os.getenv("APP_NAME", "My First DevOps App")
    env = os.getenv("APP_ENV", "dev")
    return jsonify({
        "message": f"Hello from {app_name}!",
        "environment": env,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })

@app.route("/healthz")
def health():
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
