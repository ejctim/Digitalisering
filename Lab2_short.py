from sense_hat import SenseHat;s=SenseHat();W,B=[255,255,255],[0,0,0];
while True:[s.clear()if e.direction=="middle"else s.set_rotation({"down":180,"left":270,"right":90}.get(e.direction, 0))or s.set_pixels([B]*3+[W]*2+[B]*5+[W]*4+[B]*3+[W]*6+([B]+[W]*2)*3+[B]*3+([W]*2+[B]*6)*3+[W]*2+[B]*3)for e in s.stick.get_events()if e.action=="pressed"]
