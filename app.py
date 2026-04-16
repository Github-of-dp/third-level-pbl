from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_research')
def get_research():
    # This pathing is safer for Linux servers like Render
    basedir = os.path.abspath(os.path.dirname(__file__))
    json_path = os.path.join(basedir, 'research.json')
    with open(json_path, 'r') as f:
        return jsonify(json.load(f))

if __name__ == '__main__':
    # Render binds to a specific PORT provided by the environment
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)