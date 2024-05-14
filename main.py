from flask import Flask, jsonify, request
import dotenv
from features.barcode_detector import readElements
import os

dotenv.load_dotenv()

app = Flask(__name__)

def processJson():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json(silent=True)
        return json
    else:
        raise ValueError('Content-Type not supported')

@app.route('/name', methods=['GET'])
def getName():
    result = 'this API is doomed'
    return jsonify({'name': result.strip()})

@app.route('/version', methods=['GET'])
def getAPIVersion():
    result = os.environ.get('APIVERSION')
    return jsonify({'version': result.strip()})

@app.route('/validateElements', methods=['POST'])
def validateElements():
    try:
        bodyJson = processJson()
        if not bodyJson:
            raise Exception("No data found for field 'image' on request body")
        return jsonify(readElements(bodyJson['image']))
    except Exception as e:
        return jsonify({'message': e.args[0]})

if __name__ == '__main__':
    app.run(port=8001)

