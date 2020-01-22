# set the student_files folder on your PYTHONPATH

from flask import Flask, render_template, jsonify, Response
from flask_demo.capitals import capitals

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/state/<name>', methods=['GET'])
def get_capital(name):
    name_capitalized = ' '.join(word.capitalize() for word in name.split())
    resp = jsonify(state=name, capital=capitals.get(name_capitalized, 'not found'))
    return Response(resp.data, status=200, mimetype='application/json')


@app.route('/state', methods=['GET'])
def list_states():
    resp = jsonify(names=[state for state in capitals])
    return Response(resp.data, status=200, mimetype='application/json')

app.run(host='localhost', port=8051)
