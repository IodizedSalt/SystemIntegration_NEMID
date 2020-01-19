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
    secret = 'example_key'

    my_jwt = jwt.decode(name, secret)

    userEmail = my_jwt['email']
    with open('./bank.json', 'r') as read_file:
            data = json.load(read_file)

    top = Element('DATA')
    body = SubElement(top, 'Users')
    uls = SubElement(body, 'Balance')

    for i in data:
        if(i['user'] == userEmail):
            top = Element('DATA')
            body = SubElement(top, 'User')
            uls = SubElement(body, 'Balance')
            
            body.text = i['user']
            uls.text =  str(i['balance'])

            tree_out = tostring(top, encoding="UTF-8")
            print(tree_out)
            return tree_out


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)