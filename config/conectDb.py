from sqlalchemy import *
import os
from dotenv import load_dotenv

load_dotenv()
def get_url_db():
    try:
       
        dba=os.getenv("DATABASE_URI")
    
        return dba
    except Exception as e:
        return e

def create_engine_db():
 try:
    engine = get_url_db()
    return create_engine(engine)
 except Exception as e:
    return e


