import os #untuk baca directory

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    HOST = str(os.environ.get("DB_HOST"))
    DATABASE = str(os.environ.get("DB_DATABASE"))
    USERNAME = str(os.environ.get("DB_USERNAME"))
    PASSWORD = str(os.environ.get("DB_PASSWORD"))
 
# sudah menuntukan semua classnya
# menghubungkan database dengan sqlalchemy

    SQLALCHEMY_DATABASE_URI='postgresql://postgres:admin@localhost:5432/belajar_full_stack'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_RECORD_QUERY = True

