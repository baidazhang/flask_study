# app/forms.py
__author__ = "xx"

from wtforms import Form


class BaseForm(Form):
    def get_error(self):
        message = self.errors.popitem()[1][0]
        return message
