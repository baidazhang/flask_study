# Perfect_bbs.py
__author__ = "xx"

from flask import Flask
import config
from exts import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    # 注册蓝图

    db.init_app(app)

    return app

