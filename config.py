import os
from os import environ


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ku7trwcbelsawuehniavuwefhiaukb'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATBASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS =  False

    # SMTP config
    MAIL_SERVER = environ.get('MAIL_SERVER')
    MAIL_PORT = int(environ.get('MAIL_PORT')or 25)
    MAIL_USE_TLS = environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')
    ADMINS = ['foto.nurbek@gmail.com']
    POSTS_PER_PAGE = 2