from PresentationLayer.IValidator import IValidator
from respect_validation import Validator as validator, FormValidator as formValidator


class BaseValidator(IValidator):
    def __init__(self):
        super().__init__()
        self._error_status = bool
        self._error_message = dict
        self._errors_list = list
        self._rules = {
            'text': validator.stringType().length(1),
            'source': validator.optional(validator.stringType().length(2)),
            'target': validator.stringType().length(2),
            'engine': validator.stringType().alnum().length(6, 8)
        }

    def validate(self, request: dict):
        form_validation = formValidator()
        form_validation.validate(request=request, rules=self._rules)
        print(f'Is validation failed: {form_validation.failed()}')
        print(f'Validation message: {form_validation.get_messages()}')
        print(f'Validation errors: {form_validation.get_errors()}')
        self._error_status = form_validation.failed()
        self._error_message = form_validation.get_messages()
        self._errors_list = form_validation.get_errors()
        return self._error_status

    def return_validation_status(self):
        return self._error_message, self._error_message, self._errors_list
