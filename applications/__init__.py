from flask import Flask

from applications import rbac

app = Flask(__name__)  # type:Flask
app.debug = True

# 中间件


# 注册蓝图
app.register_blueprint(rbac.rbac)
