from flask import Flask # type: ignore
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"
