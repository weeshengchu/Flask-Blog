from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# import secrets --> secrets.token_hex(16)
app.config['SECRET_KEY'] = '4453f2d45490c06c5d8abf1ab6555908'
# 4.SQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes
