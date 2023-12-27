from deep_translator import MyMemoryTranslator
from BussinesLogicLayer.ITranslatorUnit import ITranslatorUnit


class MyMemoryTranslatorUnit(ITranslatorUnit):

    @staticmethod
    def translator(text: str, target: str, **kwargs: str) -> str:
        if 'source' not in kwargs.keys():
            return MyMemoryTranslator(source='auto', target=f'{target}').translate(f'{text}')
        return MyMemoryTranslator(source=f'{kwargs['source']}', target=f'{target}').translate(f'{text}')
