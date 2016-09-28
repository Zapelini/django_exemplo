
from main.settings import *

DEBUG = True

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL', 'sqlite:///:memory:')),
}
