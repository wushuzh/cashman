from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_restful():
    return "Hello RESTful!"
