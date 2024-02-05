from flask import jsonify


def render_json(status, *args, **kwargs):
    
    response = jsonify(*args, **kwargs)
    response.status_code = status

    return response
