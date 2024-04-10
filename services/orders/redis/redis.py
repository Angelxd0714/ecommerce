import aioredis
from dotenv import load_dotenv
import os

try:
    load_dotenv("/home/angel/Documents/ecommerce/config/.env")
except Exception as e:
    print(e)

async def get_redis_connection():
    redis = aioredis.StrictRedis(host=os.getenv("REDIS_HOST"), port=int(os.getenv("REDIS_PORT")), db=int(os.getenv("REDIS_DB")))
    yield redis
    redis.close()
    await redis.wait_closed()
