# cms/views.py
__author__ = "xx"

from flask import Blueprint, render_template, views, request, session
from flask import redirect, url_for

import config
from .forms import LoginForm, ResetpwdForm
from .models import CMSUser, CMSPermission

bp = Blueprint('cms', __name__, url_prefix='/cms')


@bp.route('/')
def index():
    return render_template('cms/cms.index.html')


class LoginView(views.MethodView):
    def get(self, message=None):
        return render_template('cms/cms_login.html', message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.rember.data
            user = CMSUser.query.filter_by(email=email).frist()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                if remember:
                    session.permanent = True
                return redirect(url_for('cms.index'))
            else:
                return self.get(message="用户名或者密码错误")
        else:
            message = form.errors.popitem()[1][0]
            return self.get(message)

