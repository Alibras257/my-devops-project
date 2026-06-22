from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello DevOps",
        "environment": os.getenv("APP_ENV", "development")
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/info")
def info():
    return jsonify({
        "app_name": "my-devops-project",
        "version": "1.0.0"
    })

if __name__ == "__main__":
    app.run(debug=True)
