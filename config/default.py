from os.path import abspath, dirname, join

BASE_DIR = dirname(dirname(abspath(__file__)))

MAIL_TEMPLATES_DIR = join(BASE_DIR+'/app/templates', 'mail_templates')

# main config
SECRET_KEY = "my secret"
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
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USERNAME = 'guzmankevin420@gmail.com'
MAIL_PASSWORD = 'Dios te bendiga777'
DONT_REPLY_FROM_EMAIL = '(Kevin, guzmankevin420@gmail.com)'
ADMINS = ('guzmankevin420@gmail.com', )
MAIL_USE_TLS = True
MAIL_DEBUG = False


# mail default sender
MAIL_DEFAULT_SENDER = 'from@example.com'