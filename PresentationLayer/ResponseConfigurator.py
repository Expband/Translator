from flask import make_response, jsonify
from multipledispatch import dispatch


class ResponseConfigurator:
    @staticmethod
    @dispatch(str, int)
    def generate_response(payload: str, status_code: int):
        response = make_response(jsonify({'response': f'{payload}'}), status_code)
        return response

    @staticmethod
    @dispatch(Exception, int)
    def generate_response(payload: Exception, status_code: int):
        response = make_response(jsonify({'error': f'{payload}'}), status_code)
        return response

    @staticmethod
    @dispatch(dict, int)
    def generate_response(error_response: dict, status_code):
        response = make_response(error_response, status_code)
        return response
