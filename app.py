import json
import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Route to serve the main HTML page
@app.route('/')
def home():
    return render_template('index.html')

# Route to serve the research data as JSON
@app.route('/get_research')
def get_research():
    # This reads your research.json file and sends it to the frontend
    try:
        with open('research.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({"error": "Research file not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)