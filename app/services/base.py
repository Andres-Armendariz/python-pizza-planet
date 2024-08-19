from flask import jsonify


def entity_response(data, error):
    response = data if not error else {'error': error}
    status_code = 200 if not error else 400
    return jsonify(response), status_code
