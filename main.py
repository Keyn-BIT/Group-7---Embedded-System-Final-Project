from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>EcoTower System Initialized</h1><p>The AI-Integrated Smart Vertical Hydroponic Tower is online and ready for development.</p>"

if __name__ == "__main__":
    # Railway automatically assigns a port, which we must use
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
