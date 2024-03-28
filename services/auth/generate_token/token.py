import jwt
import os
from dotenv import load_dotenv

try:
    load_dotenv("/home/angel/Documents/ecommerce/config/.env")
except Exception as e:
    print(e)
def generate_token(data):
    return jwt.encode(data,os.getenv("SECRET_KEY"), algorithm='HS256')