import redis
import json
import datetime
# Creamos la conexion con la base de datos de reddis para crear las caches
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
    

    def store_data(entity_type, data):
        try:
            if not isinstance(data, dict):
                data = dict(data)

            for key, value in data.items():
                if isinstance(value, (datetime.date, datetime.datetime)):
                    data[key] = value.isoformat()

            entity_id = data.get('ID')
            if entity_id is None:
                raise ValueError(f"La entidad {entity_type} no tiene un campo 'ID'.")

            redis_key = f"{entity_type}:{entity_id}"

            redis_client.set(redis_key, json.dumps(data))
            print(f"{entity_type.capitalize()} {entity_id} guardado correctamente en Redis.")

        except Exception as e:
            print(f"Error general al guardar {entity_type}: {e}")

    def get_data(entity_type, entity_ID):
        try:
            key = f"{entity_type}:{entity_ID}"
            data = redis_client.get(key)

            if data:
                entity = json.loads(data)
                print(f"✅ Data from cache ({entity_type}):", entity)
                return entity
            else:
                print(f"⚠️ No cache found for {entity_type}:{entity_ID}")
                return None

        except redis.RedisError as error:
            print(f"❌ Redis error while retrieving {entity_type}: {error}")
            return None

    def delete_data(entity_type, entity_ID):
        try:
            key = f"{entity_type}:{entity_ID}"
            output = redis_client.delete(key)

            if output > 0:
                print(f"✅ {entity_type} '{entity_ID}' deleted from cache.")
            else:
                print(f"⚠️ {entity_type} '{entity_ID}' not found in cache.")

            return output == 1

        except redis.RedisError as error:
            print(f"❌ Redis error while deleting {entity_type}:{entity_ID}: {error}")
            return False
