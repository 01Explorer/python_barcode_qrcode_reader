from flask import Flask, jsonify
import dotenv
import os

dotenv.load_dotenv()

app = Flask(__name__)

@app.route('/name', methods=['GET'])
def getName():
    result = 'this API is doomed'
    return jsonify({'name': result.strip()})

@app.route('/version', methods=['GET'])
def getAPIVersion():
    result = os.environ.get('APIVERSION')
    return jsonify({'version': result.strip()})

if __name__ == '__main__':
    app.run()

