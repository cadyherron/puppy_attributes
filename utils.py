from flask import jsonify


def jsonapi(*args, **kwargs):
    """
    Wrapper around jsonify that sets the Content-Type of the response to 'application/vnd.api+json'
    """
    response = jsonify(*args, **kwargs)
    response.mimetype = 'application/vnd.api+json'
    return response