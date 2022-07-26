import os
from urllib.parse import quote_plus

from crawler.config import MONGO_DB_USERNAME, MONGO_DB_PASSWORD, MONGO_DB_HOST

SECRET_KEY = os.getenv("SECRET_KEY", 'this is Really a secret Key').encode()
DATABASE_URI = "mongodb://%s:%s@%s" % (quote_plus(MONGO_DB_USERNAME), quote_plus(MONGO_DB_PASSWORD), MONGO_DB_HOST)