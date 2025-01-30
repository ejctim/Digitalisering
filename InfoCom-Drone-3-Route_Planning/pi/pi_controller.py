import math
import requests
import argparse
import redis

redis_server = redis.Redis(host="127.0.0.1")

#Write you own function that moves the drone from one place to another 
#the function returns the drone's current location while moving
#====================================================================================================
def travel(cc, fc, tc, ft):
    stepSize = 0.00003  

    if ft:
        vec_x, vec_y = fc[0] - cc[0], fc[1] - cc[1]
        vec = math.sqrt(vec_x**2 + vec_y**2)

        if vec < stepSize:  
            return fc, False

        unitvec = (vec_x / vec, vec_y / vec)
        new_coords = (cc[0] + unitvec[0] * stepSize, cc[1] + unitvec[1] * stepSize)
        return new_coords, True 

    else:
        vec_x, vec_y = tc[0] - cc[0], tc[1] - cc[1]
        vec = math.sqrt(vec_x**2 + vec_y**2)

        if vec < stepSize:
            return tc, False 

        unitvec = (vec_x / vec, vec_y / vec)
        new_coords = (cc[0] + unitvec[0] * stepSize, cc[1] + unitvec[1] * stepSize)
        return new_coords, False 
#====================================================================================================


def run(current_coords, from_coords, to_coords, SERVER_URL):
    # Complete the while loop:
    # 1. Change the loop condition so that it stops sending location to the data base when the drone arrives the to_address
    # 2. Plan a path with your own function, so that the drone moves from [current_address] to [from_address], and the from [from_address] to [to_address]. 
    # 3. While moving, the drone keeps sending it's location to the database.
    #====================================================================================================
    drone_coords = current_coords
    fromToken = True
    tolerance = 0.0001

    while math.sqrt((drone_coords[0] - to_coords[0])**2 + (drone_coords[1] - to_coords[1])**2) > tolerance or fromToken:
        drone_coords, fromToken = travel(drone_coords, from_coords, to_coords, fromToken)
        print(drone_coords)
        with requests.Session() as session:
            drone_location = {'longitude': drone_coords[0],
                              'latitude': drone_coords[1]
                        }
            resp = session.post(SERVER_URL, json=drone_location)

  #====================================================================================================

   
if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5001/drone"

    parser = argparse.ArgumentParser()
    parser.add_argument("--clong", help='current longitude of drone location' ,type=float)
    parser.add_argument("--clat", help='current latitude of drone location',type=float)
    parser.add_argument("--flong", help='longitude of input [from address]',type=float)
    parser.add_argument("--flat", help='latitude of input [from address]' ,type=float)
    parser.add_argument("--tlong", help ='longitude of input [to address]' ,type=float)
    parser.add_argument("--tlat", help ='latitude of input [to address]' ,type=float)
    args = parser.parse_args()

    current_coords = (args.clong, args.clat)
    from_coords = (args.flong, args.flat)
    to_coords = (args.tlong, args.tlat)

    print(current_coords)
    print(from_coords)
    print(to_coords)

    run(current_coords, from_coords, to_coords, SERVER_URL)
