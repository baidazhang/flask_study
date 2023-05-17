import hashlib

from app.forms import BaseForm
from wtforms import StringField
from wtforms.validators import regexp, InputRequired


class SMSCaptchaForm(BaseForm):
    salt='dfurtn5hdsesjc*&^nd'
    telephone = StringField(validators=[regexp(r'1[3578]\d{9}')])
    timestamp = StringField(validators=[regexp(r'\d{13}')])
    sign = StringField(validators=[InputRequired(message="这个是必传的")])

    def validate(self):
        result = super(SMSCaptchaForm, self).validate()
        if not result:
            return False
        telephone = self.telephone.data
        timestamp = self.timestamp.data
        sign = self.sign.data

        sign2 = hashlib.md5()