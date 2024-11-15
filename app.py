import json
import logging as log
from flask import Flask, request, jsonify

log.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=log. DEBUG)

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return 'server is running'

@app.route('/test', methods=['POST', 'GET'])
def test():
    content_length = request.headers.get("Content-Length", type=int)
    if content_length and content_length > 2048:
        msg = f"Content lenght of the request is {content_length} which is too big"
        log.error(msg)
        return jsonify({"error": msg})
        
    content_type = request.headers.get('Content-Type')
    if content_type and 'json' in content_type:
        param = request.get_json()
        log.info("received request parameters in json format: %s" % param)
        return jsonify(param)
    else:
        if request.method.upper() == 'GET':
            param = request.args.to_dict()
            log.info("received request parameters in query string: %s" % param)
        else:
            param = request.form.to_dict()
            log.info("received request parameters from form: %s" % param)
        return jsonify(param)

if __name__ == '__main__':
    app.run()