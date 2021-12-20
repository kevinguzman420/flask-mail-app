from os.path import abspath, dirname, join, os

BASE_DIR = dirname(dirname(abspath(__file__)))

MAIL_TEMPLATES_DIR = join(BASE_DIR+'/app/templates', 'mail_templates')

# main config
SECRET_KEY = b'a1a9db1005f0f9880de42f8fd4acd2932d28e10a392dcc793a001596b15c922432101193bf2f11398b308a3f75541d9125fb22e797855b5b4769820f0911e58d'
SECURITY_PASSWORD_SALT = 'sal_de_contrasenia_de_seguridad'
BCRYP_LOG_ROUNDS = 13
WTF_CSRF_ENABLED = True
DEBUG_TB_ENABLED = False
DEBUG_TB_INTERCEPT_REDIRECT = False

# database config
SQLALCHEMY_TRACK_MODIFICATIONS = False

APP_ENV_DEVELOPMENT = 'development'
APP_ENV_PRODUCTION = 'production'
APP_ENV = ''


# Configuración del email:
MAIL_SERVER = os.getenv('MAIL_SERVER')
MAIL_PORT = os.getenv('MAIL_PORT')
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
DONT_REPLY_FROM_EMAIL = os.getenv('DONT_REPLY_FROM_EMAIL')
ADMINS = os.getenv('ADMINS')

MAIL_USE_TLS = True
MAIL_DEBUG = False

# mail default sender
MAIL_DEFAULT_SENDER = 'from@example.com'
