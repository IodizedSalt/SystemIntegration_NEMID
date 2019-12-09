# import bottle
# from bottle import route, run, request, response

from flask import Flask, request, render_template

import requests


app = Flask(__name__)


@app.route("/token", methods=['POST'])
def getNextCase():
    name = request.form["name"]
    print(name)
    return name

    # XML??
    # Decode JWT, Pass name to database, get data, return via xml


# app.run(host='localhost', port=8081, reloader=0)
if __name__ == "__main__":
    app.run()