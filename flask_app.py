from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/")
def hello_world():
    return "<p>Hello, from Techlabs!</p>"


@app.route("/hello/")
def hello():
    return f"<p>hello!</p>"
