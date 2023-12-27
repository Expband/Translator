from deep_translator import GoogleTranslator
from BussinesLogicLayer.ITranslatorUnit import ITranslatorUnit


class GoogleTranslatorUnit(ITranslatorUnit):
    @staticmethod
    def translator(text: str, target: str, **kwargs: str):
        if 'source' in kwargs.keys():
            return GoogleTranslator(source=kwargs['source'], target=target).translate(f'{text}')
        return GoogleTranslator(source='auto', target=target).translate(f'{text}')
