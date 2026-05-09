import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>EcoTower System Initialized</h1>"

if __name__ == "__main__":
    # Uses Railway's assigned port in the cloud, but defaults to 8080 on your local Raspberry Pi
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
