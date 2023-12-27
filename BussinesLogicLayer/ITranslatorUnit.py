from abc import ABCMeta


class ITranslatorUnit(metaclass=ABCMeta):
    @staticmethod
    def auto_translator(text: str, target: str, **kwargs: str) -> str:
        """
        :param text: text to translate
        :param target: target language to translate
        :param kwargs: source language parameter [optional] \\n
        """
