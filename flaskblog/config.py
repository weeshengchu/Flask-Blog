import os

# 12. Config blueprint -> hide token in .bash_profile unsuccessful


class Config:
    # import secrets --> secrets.token_hex(16)
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    # 4.SQL database
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = '4453f2d45490c06c5d8abf1ab6555908'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # 10. pip install flask-mail
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    # app.config['MAIL_USERNAME'] = 'weesheng.chu@gmail.com'
    # app.config['MAIL_PASSWORD'] = 'gmail password'
