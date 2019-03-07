#-*- coding:utf-8 -*-
from flask import Flask,render_template
from user.models import User
from extensions import db,mail,debug_toolbar,migrate,login_manager
from setting import DevConfig
from main.views import main
from auth.views import auth
from .user.models import User
from dim.models import Dimension
import commands


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_shellcontext(app)
    register_commands(app)
    return app

def register_extensions(app):
    db.init_app(app)
    mail.init_app(app)
    debug_toolbar.init_app(app)
    migrate.init_app(app,db)
    login_manager.init_app(app)

    login_manager.login_view='auth.login'
    login_manager.login_message=u'请先登录'
    login_manager.login_message_category = "info"

    @login_manager.user_loader
    def load_user(user_id):
        from user.models import User
        user = User.query.get(int(user_id))
        return user

    return None

def register_blueprints(app):
    app.register_blueprint(main)
    app.register_blueprint(auth)
    return None

def register_errorhandlers(app):
    def render_error(error):
        error_code = getattr(error, 'code', 500)
        return render_template("{0}.html".format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None

def register_shellcontext(app):
    def shell_context():
        return {
            'db':db,
            'User':User
        }
    app.shell_context_processor(shell_context)


def register_commands(app):
    app.cli.add_command(commands.create_user)
