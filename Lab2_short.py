from sense_hat import SenseHat
s=SenseHat()
def arrow():
    W, B = [255, 255, 255], [0, 0, 0]
    return [B]*3 + [W]*2 + [B]*5 + [W]*4 + [B]*3 + [W]*6 + ([B] + [W]*2)*3 + [B]*3 + ([W]*2 + [B]*6)*3 + [W]*2 + [B]*3
while True: 
  for e in s.stick.get_events(): 
    if e.action == "pressed": s.clear() if e.direction == "middle" else s.set_rotation({"down": 180, "left": 270, "right": 90}.get(e.direction, 0)) or s.set_pixels(arrow())
