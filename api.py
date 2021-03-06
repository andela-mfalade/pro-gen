import datetime

from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request

from scripts import executr
from utils import Response


app = Flask(__name__)
response = Response()


@app.errorhandler(404)
def page_not_found(error):
    url = str(request.url)
    res = response(status_code=404, req_url=url)
    return make_response(jsonify(res))


@app.errorhandler(400)
def server_error(error):
    url = str(request.url)
    res = response(status_code=400, req_url=url)
    return make_response(jsonify(res))


@app.route('/', methods=['GET'])
def get_home():
    url = str(request.url)
    res = response(status_code=200, req_url=url)
    return jsonify(res)


@app.route('/api/v1/profiles', methods=['GET'])
def fetch_profiles():
        url = str(request.url)
        profile_count = int(request.args['count'])
        if profile_count > 50:
            res = response(status_code=413, req_url=url)
            return jsonify(res)
        else:
            res = response(status_code=201, req_url=url)
            res.update({'data':  executr.fetch_profile(profile_count)})
            return jsonify(res)


@app.route('/api/v1/profile', methods=['GET'])
def fetch_single_profile():
    url = str(request.url)
    data = {'data': executr.fetch_profile()}
    res = response(status_code=201, req_url=url)
    res.update(data)
    return jsonify(res)


@app.route('/api/v1/bootstrap', methods=['GET'])
def refresh_files():
    url = str(request.url)
    status_code, flag = executr.refresh_file_contents()
    res = response(status_code=status_code, req_url=url, flag=flag)
    return jsonify(res)


if __name__ == '__main__':
    app.run(threaded=True, debug=True)
