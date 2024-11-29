import redis
from sense_hat import SenseHat

sense = SenseHat()
db = redis.Redis(host='localhost', port=6379, password='sHpMK7En65')

def store_sensor_data():
    try:
        data = {
            "temperature": round(sense.get_temperature(), 1),
            "humidity": round(sense.get_humidity(), 1),
            "pressure": round(sense.get_pressure(), 1)
        }
        db.hset("sensor_data", mapping=data)
        print("Stored:", data)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    store_sensor_data()
