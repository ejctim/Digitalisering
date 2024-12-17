import requests
import time
import random
import click
from sense_hat import SenseHat
sense = SenseHat()

def joystick_event(event):
    d_lo = 0
    d_la = 0
    send_vel = False
    if event.direction != "middle":
        match event.direction:
            case "up":
                send_vel = True
                d_la = 5
            case "down": 
                send_vel = True
                d_la = -5
            case "left":
                send_vel = True
                d_lo = -5
            case "right": 
                send_vel = True
                d_lo = 5
    return d_lo, d_la, send_vel


def get_direction():
    d_long = 0
    d_la = 0
    send_vel = False
    c = click.getchar()
    if c =='a':
        click.echo('Left')
        send_vel = True
        d_long = -10
        d_la = 0
    elif c == 'd':
        click.echo('Right')
        send_vel = True
        d_long = 10
        d_la = 0
    elif c =='w':
        click.echo('Up')
        send_vel = True
        d_long = 0
        d_la = 10
    elif c == 's':
        click.echo('Down')
        send_vel = True
        d_long = 0
        d_la = -10
    else:
        d_long = 0
        d_la = 0
        click.echo('Invalid input :(')
        send_vel = False
    return d_long, d_la, send_vel


if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5000/drone"
    while True:
        for event in sense.stick.get_events():
            print(f"Event: {event.direction} {event.action}")
            d_lo, d_la, send_vel = joystick_event(event)
            if send_vel:
                with requests.Session() as session:
                    current_location = {'longitude': d_lo,
                                        'latitude': d_la
                                          }
                resp = session.post(SERVER_URL, json=current_location)
