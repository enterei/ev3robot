parser = argparse.ArgumentParser(description="rosolve robo modes")
parser.add_argument('rmode',type=str,help='rmode!')
parser.add_argument('--cmode',type=int,default=1,help='cmode!',required=False)
parser.add_argument('--speed',type=int,default=7,help='speed!',required=False)
parser.add_argument('--time',type=int,default=10,help='time!',required=False)
parser.add_argument('--ms',type=int,default=4500,help='ms!',required=False)
parser.add_argument('--edgemax',type=int,default=1,help='edgemax!',required=False)
parser.add_argument('--edgev',type=int,default=52,help='tagarget_light_intensity!',required=False)
parser.add_argument('--bscan',type=bool,default=False,help='bscan!',required=False)
#follow
parser.add_argument('--kp',type=float,default=2.0,help='kp!',required=False)
parser.add_argument('--ki',type=float,default=0.00,help='ki!',required=False)
parser.add_argument('--kd',type=float,default=0.3,help='kd!',required=False)
parser.add_argument('--tlr',type=float,default=None,help='tlr!',required=False)
#### turn
parser.add_argument('--lspeed',type=int,default=0,help='rsped!',required=False)
parser.add_argument('--rspeed',type=int,default=5,help='lspeed!',required=False)
parser.add_argument('--turn',type=bool,default=False,help='turn!',required=False)
parser.add_argument('--degrees',type=int,default=120,help='deg!',required=False)
parser.add_argument('--rot',type=float,default=0,help='rot!',required=False)
parser.add_argument('--edgetest',type=bool,default=False,help='edgetest!',required=False)
parser.add_argument('--wsp',type=int,default=78,help='wsp!',required=False)
parser.add_argument('--uspeed',type=int,default=1,help='deg!',required=False)
parser.add_argument('--ulspeed',type=float,default=7,help='rot!',required=False)
parser.add_argument('--urspeed',type=float,default=-3,help='rot!',required=False)



parser.add_argument('--back',type=bool,default=False,help='back!',required=False)

parser.add_argument('--way',type=str,help='way!',required=False)

pargs = parser.parse_args()
print(vars(pargs).get('rmode'))

print('pargs: ')
print(pargs.rmode)
print(pargs.cmode)
#  print(pargs.speed)

robot = Robot(cmode=pargs.cmode)
robot.makesound()
