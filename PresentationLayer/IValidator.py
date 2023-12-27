from abc import ABC


class IValidator(ABC):
    def __init__(self):
        self._error_status: bool
        self._error_message: dict
        self._errors_list: list
        self._rules: dict

    @staticmethod
    def _validate(request: dict) -> bool:
        """
        :param request: request body
        """
