from flask import Flask
import socket
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <html>
        <head>
            <title>Linux Production App</title>
        </head>
        <body>
            <h1>🚀 Linux Multi-Tier Application</h1>
            <p>Application is running successfully.</p>
            <p>Hostname: {socket.gethostname()}</p>
            <p>Process ID: {os.getpid()}</p>
            <p>Time: {datetime.now()}</p>
        </body>
    </html>
    """

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "hostname": socket.gethostname()
    }

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
