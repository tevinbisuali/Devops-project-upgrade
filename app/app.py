from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from a production-style Flask app on Azure!"
