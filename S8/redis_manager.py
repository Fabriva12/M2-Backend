import redis
import json
import datetime

redis_client = redis.Redis(
    host="redis-17181.c124.us-central1-1.gce.redns.redis-cloud.com",
    port=17181,
    password="Q8o50fv7eB3J0KcePdMOzHaOLa9btN9h",)

class CacheManager():
    def __init__(self,redis_client):
        self.redis_client = redis_client
        
        try:
            connection_status = redis_client.ping()
            if connection_status:
                print("Connected to Redis!")
            else:
                print("The connection to Redis was unsuccessful!")
        except redis.ConnectionError as ex:
            print("An error ocurred while connecting to Redis: ", ex)
    

    def store_data(key, producto):
        try:
            if not isinstance(producto, dict):
                producto = dict(producto)

            for key, value in producto.items():
                if isinstance(value, (datetime.date, datetime.datetime)):
                    producto[key] = value.isoformat()

            redis_client.set(f"product:{producto['ID']}", json.dumps(producto))
        except redis.RedisError as error:
                print(f"An error ocurred while storing data in Redis: {error}")
    

    def get_data(product_id):
        try:
            key =(f"product:{product_id}")
            data = redis_client.get(key)
            if data:
                product = json.loads(data)
                print("✅ Data from cache:", product)
                return product
            else:
                return None
        except redis.RedisError as error:
            print(f"An error ocurred while retrieving data from Redis: {error}")
        

    def delete_data(product_ID):
        try:
            output = redis_client.delete(f"product:{product_ID}")
            if output > 0:
                print(f"product '{product_ID}' and its value have been deleted.")
            else:
                print(f"product '{product_ID}' not found.")

            return output == 1
        except redis.RedisError as error:
            print(f"An error ocurred while deleting data from Redis: {error}")
            return False
