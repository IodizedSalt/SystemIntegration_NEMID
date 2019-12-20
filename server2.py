# REMEMBER TO RUN ' python server2.py AND NOT py server2.py '
# You should've stopped using Windows a long time ago....


from flask import Flask, request, render_template
import requests
import jwt
import json
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/token", methods=['POST'])

def getNextCase():
    name = request.form["name"]
    my_jwt = jwt.decode(name, verify=False)

    userEmail = my_jwt['email']

    with open('./db/bank.txt', 'r') as read_file:
        data = json.load(read_file)


    userBankBalance = data['users'][userEmail]

    top = Element('XML-DATA')

    user = SubElement(top, 'user-email')
    user.text = userEmail

    balance = SubElement(top, 'balance')
    balance.text = str(userBankBalance)

    print(tostring(top))

    return tostring(top)

# app.run(host='localhost', port=8081, reloader=0)
if __name__ == "__main__":
    app.run()