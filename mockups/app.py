from flask import Flask, Response, request, render_template
from flask import jsonify
import logging

# Below generated imports (do not edit or delete this comment!):
from src.rest.current_generation_rest import current_generation_rest
from src.rest.current_usage_rest import current_usage_rest
from src.rest.energy_usage_rest import energy_usage_rest
from src.rest.energy_generation_rest import energy_generation_rest
from src.rest.example_sqlite_rest import example_sqlite_rest
from src.rest.example_rest import example_rest

LOGFORMAT = "%(asctime)s - %(name)s - [%(process)d/%(threadName)-10s] %(levelname)-8s \"%(filename)s/%(funcName)s:%(lineno)d\" \"%(message)s\""
logging.basicConfig(format=LOGFORMAT)

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/example_rest')
def example():
    request = {'id': 1}
    return f'{example_rest(request)}'


@app.route('/example_sqlite_rest')
def example_sqlite():
    request = {'id': 1}
    return example_sqlite_rest(request)


@app.route('/energy_generation_rest', methods=['GET', 'POST'])
def energy_generation():
    # Process POST:
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        result = energy_generation_rest(json)
        return jsonify(result)


@app.route('/energy_usage_rest', methods=['GET', 'POST'])
def energy_usage():
    # Process POST:
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        result = energy_usage_rest(json)
        return jsonify(result)


@app.route('/current_usage_rest', methods=['GET', 'POST'])
def current_usage():
    # Process POST:
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        result = current_usage_rest(json)
        return jsonify(result)


@app.route('/current_generation_rest', methods=['GET', 'POST'])
def current_generation():
    # Process POST:
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        result = current_generation_rest(json)
        return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
