from sense_hat import SenseHat

sense = SenseHat()

W = [255, 255, 255]
B = [0, 0, 0]       

def generate_arrow(direction):
    arrow = [
        B, B, B, W, W, B, B, B,
        B, B, W, W, W, W, B, B,
        B, W, W, W, W, W, W, B,
        W, W, B, W, W, B, W, W,
        B, B, B, W, W, B, B, B,
        B, B, B, W, W, B, B, B,
        B, B, B, W, W, B, B, B,
        B, B, B, W, W, B, B, B,
    ]
    rotation = 0
    
    match direction:
        case "down":
            rotation = 180
        case "left":
            rotation = 270
        case "right":
            rotation = 90
    
    return (arrow, rotation) 

def display_arrow(direction):
    (arrow, rotation) = generate_arrow(direction)
    sense.set_rotation(rotation)
    sense.set_pixels(arrow)

def joystick_event(event):
    if event.action == "pressed" and event.direction != "middle":
        display_arrow(event.direction)
    if event.direction == "middle": 
        sense.clear()

while True:
    for event in sense.stick.get_events():
        joystick_event(event)
