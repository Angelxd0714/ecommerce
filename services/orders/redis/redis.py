import redis
from dotenv import load_dotenv
import os
from flask import jsonify
try:
    load_dotenv("/home/angel/Documents/ecommerce/config/.env")
except Exception as e:
    print(e)

def get_redis_connection():
    return redis.StrictRedis(host=os.getenv("REDIS_HOST"), port=int(os.getenv("REDIS_PORT")), db=int(os.getenv("REDIS_DB")))

