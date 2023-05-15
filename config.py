# config.py
__author__ = "xx"

import os

SECRET_KEY = "abcdefg"
DEBUG = True
DB_URI = "mysql+pymysql://root:123456@192.168.60.122:3306/bbs?charset=utf8"

CMS_USER_ID = "aaa"
FRONT_USER_ID = "FFFF"

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

