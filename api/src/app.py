from flask import Flask
from db import database

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return "Hello world"


@app.route("/recipes", methods=["GET"])
def test():
    cursor = database.cursor()
    cursor.execute("SELECT * FROM recipes")
    result = cursor.fetchall()
    cursor.close()
    return result
