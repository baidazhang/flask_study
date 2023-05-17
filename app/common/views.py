# common/views.py
__author__ = "xx"
from flask import Blueprint
from utils.captcha import Captcha

bp = Blueprint("common", __name__, url_prefix='/c')

@bp.route('/sms_captcha/', methods=["POST"])
def sms_captcha():
    pass

@bp.route('/captcha/')
def graph_captcha():
    test, image = Captcha.gene_graph_captcha()
