import datetime

from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request

from scripts import executr
from utils import Response


all_requests = []
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
    global all_requests
    url = str(request.url)
    executr.update_firebase(all_requests)
    all_requests = []
    res = response(status_code=200, req_url=url)
    return jsonify(res)


@app.route('/api/v1/profiles', methods=['GET'])
def fetch_profiles():
        global all_requests
        url = str(request.url)
        all_requests.append({
            'req_url': url,
            'time': datetime.datetime.now()
        })
        profile_count = int(request.args['count'])
        if profile_count > 100:
            res = response(status_code=413, req_url=url)
            return jsonify(res)
        else:
            res = response(status_code=201, req_url=url)
            res.update({'data':  executr.fetch_profile(profile_count)})
            return jsonify(res)


@app.route('/api/v1/profile', methods=['GET'])
def fetch_single_profile():
    global all_requests
    url = str(request.url)
    all_requests.append({
        'req_url': url,
        'time': datetime.datetime.now()
    })
    data = {'data': executr.fetch_profile()}
    res = response(status_code=201, req_url=url)
    res.update(data)
    return jsonify(res)


if __name__ == '__main__':
    app.run(threaded=True, debug=True)
