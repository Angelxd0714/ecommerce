from sqlalchemy import *
import os
from dotenv import load_dotenv

load_dotenv("alembic.ini")
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


