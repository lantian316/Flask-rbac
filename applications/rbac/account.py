from flask import request, session, render_template, redirect, url_for

class Auth(object):
    def __init__(self,app=None):
        self.app=app
        if app:
            self.init_app(app)

    def init_app(self,app):
        pass

    def check_login(self):
        pass




