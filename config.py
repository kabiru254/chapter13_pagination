import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Define app configurations"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-to-guess'

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Email configurations
    MAIL_SERVER = os.environ.get("MAIL SERVER")
    MAIL_PORT = int(os.environ.get('MAIL PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL USE TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL PASSWORD')
    ADMINS = os.environ.get('ADMINS')

    # Pagination
    POSTS_PER_PAGE = int(os.environ.get('POSTS_PER_PAGE'))
