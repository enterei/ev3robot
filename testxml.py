import argparse

import xmlschema
parser = argparse.ArgumentParser(description="rosolve robo modes")
parser.add_argument('rmode',type=str,help='rmode!')
parser.add_argument('--cmode',type=int,default=1,help='cmode!',required=False)
parser.add_argument('--speed',type=int,default=200,help='speed!',required=False)
parser.add_argument('--time',type=int,default=10,help='time!',required=False)
parser.add_argument('--licht',type=str,help='licht!',required=False)
parser.add_argument('--farbe',type=int,default=10,help='farbe!',required=False)

pargs= parser.parse_args()
print(pargs.licht!=None)
schema=xmlschema.XMLSchema('MeasureResult.xsd')
print(schema.validate('res1.xml'))
print(dict(schema.elements))
a=schema.get_element('result')