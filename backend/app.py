from flask import Flask, request

app = Flask(__name__)


def add(x, y):
    return x + y


def minus():
    return x - y


def multiply():
    return x * y


@app.route('/calculate', methods=['POST'])
def calculate():
    return request.data
