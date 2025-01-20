# InfoCom Drone Project - Part 2 - Microservices
Install the required Python packages if not done already (you probably did this in the previous assignment):
```
sudo apt update
sudo apt install python3-socketio
sudo apt install python3-engineio
sudo apt install python3-flask-socketio
sudo apt install python3-flask-cors

```
Go to `/webserver`, start your Redis server (if it is not already running, which it probably is – test using `redis-cli`) and run the two flask servers:

1. Run server for writing data to the redis server
```
export FLASK_APP=database.py
export FLASK_DEBUG=1
flask run --port=5001
```
2. Open a new terminal, go to `/webserver` and run `build.py`
```
export FLASK_APP=build.py
export FLASK_DEBUG=1
flask run
```
Open a web browser (e.g. Chromium) on your Raspberry Pi and enter the following URL. You should see a map of Lund as in the previous assignment. Make sure you see a red dot representing the drone at the LTH location.
```
http://localhost:5000
```

Open a new terminal, go to `/pi` and run the Pi controller:
```
python3 pi_controller.py
```
You can replace `pi_controller.py` with the one you created in Part 1, but keep `SERVER_URL` the same as in the file provided in this lab. Make sure you can move the drone on the map using `pi_controller.py`.

Note: Don't use `python3 build.py` or `python3 database.py` to run the webservers, since this does not provide all the functionality required by the application.

