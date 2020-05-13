from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

from .core import evaluate, InvalidExpression


app = Flask(__name__)
cors = CORS(app)


@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.json['formula']
    try:
        return jsonify({'result': str(evaluate(expression)), 'message': 'success'})
    except InvalidExpression as e:
        return make_response(jsonify({'result': '', 'message': str(e)}), 400)
