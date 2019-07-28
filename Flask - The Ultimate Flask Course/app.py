from flask import Flask, jsonify, request, url_for, redirect, session

app = Flask(__name__)

app.config['DEBUG']
app.config['SECRET_KEY'] = 'senha'

@app.route('/<name>')
def index(name):
    return '<h1>Hello {} !</h1>'
