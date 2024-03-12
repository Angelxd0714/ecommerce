from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from db.connect import SQLALCHEMY_DATABASE_URI
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=SQLALCHEMY_DATABASE_URI