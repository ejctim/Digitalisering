from flask import Flask, jsonify, render_template
import redis
import sensor_store

app = Flask(__name__)
db = redis.Redis(host='localhost', port=6379, password='sHpMK7En65')

@app.route('/sensor_data')
def sensor_data():
    sensor_store.store_sensor_data()
    data = db.hgetall("sensor_data")
    print(data)
    return jsonify({k.decode(): v.decode() for k, v in data.items()})

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
