from .default import *

SECRET_KEY = '823e5dc3ecc3fc5f1ebd185f6717e6a49f8cf179'

FLASK_ENV = APP_ENV_PRODUCTION

# SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://u3otevp05vjbg3hn:qkFupmMC3HBFDU941amf@br6ok3dyd1m1fzz5ksdk-mysql.services.clever-cloud.com:3306/br6ok3dyd1m1fzz5ksdk'

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost:5432/send_email_test';
