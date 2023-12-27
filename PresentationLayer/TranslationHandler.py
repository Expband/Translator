from BussinesLogicLayer.TranslatorFactory import TranslatorFactory
from PresentationLayer.ResponseConfigurator import ResponseConfigurator
from PresentationLayer.BaseValidator import BaseValidator

from flask import request
from flask_restful import Resource


class TranslationHandler(Resource):

    @staticmethod
    def get():
        google_validator = BaseValidator()
        raw_request = request.get_json()
        if not google_validator.validate(request=raw_request):
            translator_engine = TranslatorFactory.choose_translator(raw_request['engine'])
            try:
                if 'source' not in raw_request.keys():
                    translated_text = translator_engine.translator(text=raw_request['text'],
                                                                   target=raw_request['target'])
                    response = ResponseConfigurator.generate_response(translated_text, 200)
                    return response
                else:
                    translated_text = translator_engine.translator(text=raw_request['text'],
                                                                   source=raw_request['source'],
                                                                   target=raw_request['target'])
                    response = ResponseConfigurator.generate_response(translated_text, 200)
                    return response
            except Exception as ex:
                print(f"Error: {ex}")
                response = ResponseConfigurator.generate_response(ex, 400)
                return response
        else:
            print('Validation failed')
            error_status, error_message, error_list = google_validator.return_validation_status()
            response_body = {'validation_error': f'{error_status}',
                             'validation_error_message': f'{error_list}',
                             'validation_error_list': f'{error_list}'}
            response = ResponseConfigurator.generate_response(response_body, 400)
            return response

    @staticmethod
    def post():
        pass
