from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_research')
def get_research():
    with open('research.json', 'r') as f:
        return jsonify(json.load(f))

if __name__ == '__main__':
    app.run(debug=True)