from wtforms import StringField, IntegerField
from wtforms.validators import Email, Length, InputRequired, EqualTo
from ..forms import BaseForm


class LoginForm(BaseForm):
    email = StringField(validators=[Email(message="请输出正确的邮箱"),
                                    InputRequired(message="请输入邮箱")])
    password = StringField(validators=[Length(6, 20, message="密码长度不够或超出")])
    rember = IntegerField()


class ResetpwdForm(BaseForm):
    oldpwd = StringField(validators=[Length(6, 20, message="请输入正确格式的旧密码")])
    newpwd = StringField(validators=[Length(6, 20, message="请输入正确格式的新密码")])
    newpwd2 = StringField(validators=[EqualTo('newpwd',message="两次输入密码不一致")])

