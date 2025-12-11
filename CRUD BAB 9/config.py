import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HOST = "localhost"
    DATABASE = "crud_flask"
    USERNAME = "root"
    PASSWORD = ""

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True

