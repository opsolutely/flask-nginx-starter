import os

CSRF_ENABLED = True
ENV = os.environ.get('ENVIRONMENT', 'dev')
MODEL_HASH = os.environ.get('MODEL_HASH')
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

ROOT_PATH = BASE_DIR = os.path.join(os.path.dirname(__file__), '..')
SECRET_KEY = os.environ.get('SECRET_KEY')
STATIC_FOLDER = os.path.join(ROOT_PATH, 'static')
TEMPLATE_FOLDER = os.path.join(ROOT_PATH, 'templates')
SQLALCHEMY_MIGRATE_REPO = os.path.join(ROOT_PATH, 'db_repository')

if ENV == 'dev':
    PORT = 7070
    APP_BASE_LINK = 'http://localhost:{}'.format(PORT)
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/dev_db'
else:
    APP_BASE_LINK = os.environ.get('APP_BASE_LINK')
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(os.environ.get('POSTGRES_ENV_POSTGRES_USER'),
                                                                   os.environ.get('POSTGRES_ENV_POSTGRES_PASSWORD'),
                                                                   os.environ.get('POSTGRES_PORT_5432_TCP_ADDR'),
                                                                   os.environ.get('POSTGRES_PORT_5432_TCP_PORT'),
                                                                   os.environ.get('POSTGRES_ENV_POSTGRESQL_DB'))
