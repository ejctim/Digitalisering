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
    
    match direction:
        case "down":
            arrow = rotate_arrow(arrow, 180)
        case "left":
            arrow = rotate_arrow(arrow, 270)
        case "right":
            arrow = rotate_arrow(arrow, 90)
        case "middle":
            arrow = []

    return arrow


def rotate_arrow(arrow, angle):
    matrix = [arrow[i:i + 8] for i in range(0, 64, 8)]
    
    match angle:
      case 90:
        matrix = list(zip(*matrix[::-1]))
      case 180:
        matrix = [row[::-1] for row in matrix[::-1]]
      case 270:
        matrix = list(zip(*matrix))[::-1]
    
    return [pixel for row in matrix for pixel in row] 

def display_arrow(direction):
    arrow = generate_arrow(direction)
    sense.set_pixels(arrow)

def joystick_event(event):
    if event.action == "pressed":
        display_arrow(event.direction)

while True:
    for event in sense.stick.get_events():
        joystick_event(event)
