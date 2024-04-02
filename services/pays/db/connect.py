import sys
from sqlalchemy import create_engine
sys.path.append('/home/angel/Documents/ecommerce/')
from config.conectDb import get_url_db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db=get_url_db()

SQLALCHEMY_DATABASE_URI = db

engine = create_engine(SQLALCHEMY_DATABASE_URI)


session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

