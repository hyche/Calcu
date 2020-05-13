from flask import Flask, request, jsonify
from flask_cors import CORS

from .core import evaluate


app = Flask(__name__)
cors = CORS(app)


@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.json['formula']
    result = evaluate(expression)
    return jsonify({'result': str(result)})
