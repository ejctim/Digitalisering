# InfoCom Drone Project - Part 3 - Route Planning
Install required Python packages if not done already (you probably did this in one of the previous assignments):
```
sudo apt update
sudo apt install python3-socketio
sudo apt install python3-engineio
sudo apt install python3-flask-socketio
sudo apt install python3-flask-cors

```

Install new Python package required for this assignment:
```
sudo apt update
sudo apt install python3-geopy
```

Go to `/webserver`, start your Redis server (if it is not already running, which it probably is – test using `redis-cli`) and run the three flask servers:

1. Run server for writing data to the redis server
    ```
    export FLASK_APP=database.py
    export FLASK_DEBUG=1
    flask run --port=5001
    ```
2. Open a new terminal, go to `/webserver`, and run the route planner
    ```
    export FLASK_APP=route_planner.py
    export FLASK_DEBUG=1
    flask run --port=5002
    ```

3. Open a new terminal, go to `/webserver`,  and run the website server
    ```
    export FLASK_APP=build.py
    export FLASK_DEBUG=1
    flask run
    ```

Open a web browser (e.g. Chromium) on your Raspberry Pi and enter the following URL. You should see a map of Lund as in the previous assignment. Make sure you see a red dot representing the drone at the LTH location.
```
http://localhost:5000
```


Note: Don't use `python3 build.py`, `python3 route_planner.py`, or `python3 database.py` to run the webservers, since this does not provide all the functionality requied by the application.

