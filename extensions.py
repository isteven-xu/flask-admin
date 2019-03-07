from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
mail = Mail()
debug_toolbar = DebugToolbarExtension()
migrate = Migrate()
login_manager = LoginManager()