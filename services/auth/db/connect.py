import sys
sys.path.append('/home/angel/Documents/ecommerce/')
from config.conectDb import get_url_db

db=get_url_db()

SQLALCHEMY_DATABASE_URI = db