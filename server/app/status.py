from flask import jsonify

SUCCESS = 200
CREATED = 201

BAD_REQUEST = 400
UNAUTHORIZED = 401
NOT_FOUND = 404

INTERNAL_SERVER_ERROR = 500


def respond(data=None, status=SUCCESS):
    if not data:
        data = {}
    response = jsonify(data)
    response.status_code = status
    return response
