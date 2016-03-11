"""Progen entry point.

Main script to initiate biogenesis.
"""
from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request

from scripts import executr


app = Flask(__name__)


@app.errorhandler(404)
def server_error(error):
    error_message = {
        'success': False,
        'status_code': 404,
        'message': 'Nothing Exists On This Endpoint',
        'valid_request': '/api/v1/profiles?count=<number of desired profile.>',
        'links': {
            'self': str(request.url)
        },
    }
    return make_response(jsonify(error_message))


@app.errorhandler(400)
def server_error(error):
    error_message = {
        'success': False,
        'status_code': 400,
        'message': 'You are doing this wrong. You need to specify the count.',
        'valid_request': '/api/v1/profiles?count=<number of desired profile.>',
        'links': {
            'self': str(request.url)
        },
    }
    return make_response(jsonify(error_message))


@app.route('/api/v1/profiles', methods=['GET'])
def fetch_profiles():
    response = {
        'success': True,
        'status_code': 200,
        'links': {
            'self': str(request.url)
        },
    }
    profile_count = int(request.args['count'])
    if profile_count > 20:
        error_message = {
            'success': False,
            'status_code': 413,
            'message': 'Request Limit Exceeded. 20 or less profiles count allowed per request.',
            'links': {
                'self': str(request.url)
            },
        }
        return jsonify(error_message)
    else:
        response.update({'data':  executr.fetch_profile(profile_count)})
        return jsonify(response)


@app.route('/api/v1/profile', methods=['GET'])
def fetch_single_profile():
    response = {
        'success': True,
        'status_code': 200,
        'data': executr.fetch_profile(),
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
