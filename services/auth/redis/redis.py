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


def set_token(data,id):

    """
    set token, this only works for 3600 seconds, you can change it to your needs.
    :param data:
    :return: token, if token is not set, it will return None.
    """
    key_id = id
    token=get_redis_connection().setex(f"token:{key_id}",3600,data)
    return token
    