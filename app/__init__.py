from flask import Flask
from werkzeug.routing import BaseConverter


from .config import config

# 为路由规则增加正则转换器
class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


def create_app():
    app = Flask(__name__)
    app.url_map.converters['regex'] = RegexConverter
    # 加载配置
    app.config.from_object(config['dev'])

    return app
