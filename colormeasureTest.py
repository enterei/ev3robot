from Robot import Robot
import sys
import argparse
from followline import LineFollower
from ColorSensor import ColorSensor
from MySocket import MySocket
from helper import resolver

#robot = LineTest()
#from helper.resolver import resolve
parser = argparse.ArgumentParser(description="rosolve robo modes")
parser.add_argument('--cmode',type=int,default=1,help='cmode!',required=False)
parser.add_argument('--speed',type=int,default=200,help='speed!',required=False)
parser.add_argument('--time',type=int,default=10,help='time!',required=False)
parser.add_argument('rmode',type=str,help='rmode!')
def main():
    pargs= parser.parse_args()

    print('pargs: ')
    print(pargs.items().rmode)
    print(pargs.cmodeK)

    robot = Robot(cmode=pargs.cmode)
    ar=pargs.rmode
    print('parks.rmode in ar :'+ar)
    print('parks.rmode  :' + pargs.rmode)
    robot.run_modes(ar,**{'speed':pargs.speed,'time':pargs.time})

    #robot.run_measure(10)


#mysocket = MySocket
#mysocket.conn(mysocket)
#mysocket.send(mysocket,[2,3,4,5])
#mysocket.send(mysocket,[3,24,34,53])
if __name__ == '__main__':
    #server()
    main()
