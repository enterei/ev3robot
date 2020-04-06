from Robot import Robot
import sys
from followline import LineFollower
from ColorSensor import ColorSensor
from MySocket import MySocket
from helper import resolver

#robot = LineTest()
from helper.resolver import resolve


def main(*args):
    robot = Robot()
    robot.run_measure(10)
    #resolve(gs)


#mysocket = MySocket
#mysocket.conn(mysocket)
#mysocket.send(mysocket,[2,3,4,5])
#mysocket.send(mysocket,[3,24,34,53])
if __name__ == '__main__':
    #server()
    main(sys.argv)
