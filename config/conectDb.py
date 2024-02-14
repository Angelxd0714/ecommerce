from sqlalchemy import *
import os
from dotenv import load_dotenv

try:
    load_dotenv("/home/angel/Documents/ecommerce/config/alembic.ini")
except Exception as e:
    print(e)

def get_url_db():
    try:
        dba=os.getenv("sqlalchemy.url")
      
        return dba
    except Exception as e:
        return e

def create_engine_db(engine=None):
 try:
    engine = get_url_db()
    return create_engine(engine)
 except Exception as e:
    return e


