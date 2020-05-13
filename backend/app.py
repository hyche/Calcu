from flask import Flask, request, jsonify
from .core import evaluate

app = Flask(__name__)


@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.json['format']
    result = evaluate(expression)
    return jsonify({'result': str(result)})
