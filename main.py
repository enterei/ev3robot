# from Robot import Robot
import sys
from followline import LineFollower
from ColorSensor import ColorSensor
from MySocket import MySocket
import json
from helper import resolver

# robot = LineTest()


def main(*args):



    mysocket = MySocket
    mysocket.conn(mysocket)
    a={'id':"ecke",'r':"vor"}
    serialized_dict = json.dumps(a).encode("ascii")
    x=json.load(mysocket.send(mysocket, serialized_dict))
    print(x.get('zug'))
    #mysocket.send(mysocket, [3, 24, 34, 53])
if __name__ == '__main__':
    # server()
    main(sys.argv)
