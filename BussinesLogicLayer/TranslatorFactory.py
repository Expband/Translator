from BussinesLogicLayer.GoogleTranslatorService import GoogleTranslatorUnit
from BussinesLogicLayer.MyMemoryTranslatorService import MyMemoryTranslatorUnit


class TranslatorFactory:
    @staticmethod
    def choose_translator(translator):
        if translator == 'google':
            return GoogleTranslatorUnit
        if translator == 'mymemory':
            return MyMemoryTranslatorUnit
