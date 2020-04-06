#from Robot import Robot
import sys
import argparse



#robot = LineTest()
#from helper.resolver import resolve
#import helper.resolver
from helper import resolver

parser = argparse.ArgumentParser(description="rosolve robo modes")
parser.add_argument('--mode',type=int,default=1,help='mode!',required=False)

def main(*args):
    ar=parser.parse_args()
    print(ar.mode)
#    resolveMove(args)

#mysocket = MySocket
#mysocket.conn(mysocket)
#mysocket.send(mysocket,[2,3,4,5])
#mysocket.send(mysocket,[3,24,34,53])
if __name__ == '__main__':
    #server()
    main(sys.argv)
