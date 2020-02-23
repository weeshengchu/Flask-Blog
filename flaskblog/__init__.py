import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

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

# 10. pip install flask-mail
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
# app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
app.config['MAIL_USERNAME'] = 'weesheng.chu@gmail.com'
app.config['MAIL_PASSWORD'] = 'gmail password'
mail = Mail(app)

from flaskblog import routes
