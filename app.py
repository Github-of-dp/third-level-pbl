from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Add this to serve your JSON file
@app.route('/research.json')
def serve_json():
    return send_from_directory(os.getcwd(), 'research.json')

if __name__ == '__main__':
    app.run(debug=True)