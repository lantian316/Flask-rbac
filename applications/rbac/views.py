from flask import request, session, render_template, redirect, url_for

from . import rbac


@rbac.route('/')
def index():
    return '首页测试'
