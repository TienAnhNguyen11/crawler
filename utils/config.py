import os

SECRET_KEY = os.getenv("SECRET_KEY", 'this is Really a secret Key').encode()
DATABASE_URL = os.getenv("DATABASE_URL", "mongo://smartdocs:123456@localhost/smartdocs")
STORAGE_PATH = os.getenv("STORAGE_PATH", '../../data/files')