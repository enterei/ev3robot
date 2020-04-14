from Robot import Robot
import sys
import argparse
from followline import LineFollower
from ColorSensor import ColorSensor
from MySocket import MySocket
from helper import resolver
class c:
    pass
#robot = LineTest()
#from helper.resolver import resolve
parser = argparse.ArgumentParser(description="rosolve robo modes")
parser.add_argument('rmode',type=str,help='rmode!')
parser.add_argument('--cmode',type=int,default=1,help='cmode!',required=False)
parser.add_argument('--speed',type=int,default=200,help='speed!',required=False)
parser.add_argument('--time',type=int,default=10,help='time!',required=False)
parser.add_argument('--ms',type=int,default=4500,help='ms!',required=False)
parser.add_argument('--edgemax',type=int,default=4,help='edgemax!',required=False)
parser.add_argument('--edgev',type=int,default=74,help='edgev!',required=False)
parser.add_argument('--bscan',type=bool,default=False,help='bscan!',required=False)
#follow
parser.add_argument('--kp',type=float,default=0.3,help='kp!',required=False)
parser.add_argument('--ki',type=float,default=0.05,help='ki!',required=False)
parser.add_argument('--kd',type=float,default=0.2,help='kd!',required=False)
parser.add_argument('--tlr',type=float,default=None,help='tlr!',required=False)
#### turn
parser.add_argument('--lspeed',type=int,default=20,help='rsped!',required=False)
parser.add_argument('--rspeed',type=int,default=0,help='lspeed!',required=False)
parser.add_argument('--turn',type=bool,default=False,help='turn!',required=False)
parser.add_argument('--degrees',type=int,default=990,help='deg!',required=False)
parser.add_argument('--rot',type=float,default=1,help='rot!',required=False)






def main():
    pargs= parser.parse_args()
    print(vars(pargs).get('rmode'))

    print('pargs: ')
    print(pargs.rmode)
    print(pargs.cmode)
  #  print(pargs.speed)

    robot = Robot(cmode=pargs.cmode)
    ar=pargs.rmode
    print('parks.rmode in ar :'+ar)
    print('parks.rmode  :' + pargs.rmode)
    #assert pargs.edgemax
    print(pargs.edgemax)

    robot.run_modes(ar,**{'speed':pargs.speed,'time':pargs.time,'ms':pargs.ms,
                          'edgemax':pargs.edgemax,'bscan':pargs.bscan,'edgev':pargs.edgev,
                          'ki':pargs.ki,'kd':pargs.kd,'kp':pargs.kp,
                          'turn':pargs.turn,'lspeed':pargs.lspeed,'rspeed':pargs.rspeed,'degrees':pargs.degrees,
                          'rot':pargs.rot,'target_light_intensity':pargs.tlr
                          })

    #robot.run_measure(10)


#mysocket = MySocket
#mysocket.conn(mysocket)
#mysocket.send(mysocket,[2,3,4,5])
#mysocket.send(mysocket,[3,24,34,53])
if __name__ == '__main__':
    #server()
    main()
