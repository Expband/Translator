from flask import Flask
from flask_restful import Api
from PresentationLayer.TranslationHandler import TranslationHandler

app = Flask(__name__)
api = Api(app)

api.add_resource(TranslationHandler, '/translate')

if __name__ == '__main__':
    app.run(debug=True)
