from typing import Optional

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class BadWordValidator:
    def __init__(self, bad_words: Optional[list]=None, message: str=None):
        self.bad_words = bad_words
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value or "This field must not contain bad words!"

    def __call__(self, value):
        for bad_word in value.split():
            if bad_word.lower() in self.bad_words:
                raise ValidationError(self.message)