from flask import Flask, request, jsonify
from flask_cors import CORS
from logic.regex import *

app = Flask(__name__)
cors = CORS(app)

@app.route('/replace', methods=['POST'])
def handle_text():
    data = request.get_json()
    text = data['text']
    regex = data['regex']
    replacement = data['replace']
    result = replace_matches(regex, text, replacement)
    print(result)
    return jsonify({'result': result})

@app.route('/match', methods=['POST'])
def handle_match():
    data = request.get_json()
    text = data['text']
    regex = data['regex']
    matches = match(regex, text)
    print(matches)
    return jsonify({'matches': matches})

if __name__ == '__main__':
    app.run(port=8000)