from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# import secrets --> secrets.token_hex(16)
app.config['SECRET_KEY'] = '4453f2d45490c06c5d8abf1ab6555908'
# 4.SQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
# 6. User authentication
login_manager = LoginManager(app)
# 6. redirects account.html to login page
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
