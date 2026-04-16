from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Route to serve the SPA (Single Page Application)
@app.route('/')
def index():
    return render_template('index.html')

# API Route for the research database
@app.route('/get_research')
def get_research():
    try:
        # Construct path to JSON file
        json_path = os.path.join(os.path.dirname(__file__), 'research.json')
        with open(json_path, 'r') as file:
            data = json.load(file)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # In production (Render), debug should be False
    app.run(debug=True)