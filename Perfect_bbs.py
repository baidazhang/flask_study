# Perfect_bbs.py
__author__ = "xx"

from flask import Flask
import config
from exts import db
from app.cms import bp as cms_bp
from app.common import bp as common_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    # 注册蓝图
    app.register_blueprint(cms_bp)
    app.register_blueprint(common_bp)

    db.init_app(app)

    return app

