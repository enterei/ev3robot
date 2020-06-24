import json

import myMotor
from MySocket import MySocket
from ColorSensor import ColorSensor
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, follow_for_ms, follow_for_forever, \
   LineFollowErrorTooFast,  LineFollowErrorLostLine
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds


from helper.targetValue import targetvalue, targetMode

stop_action = "coast"
power = 200
dt = 500
speed = 200
time = 10


class Robot:

    power = 200
    dt = 500
    speed = 200
    time = 10
    socket = MySocket()
    colorS = ColorSensor()
    cs = ev3.ColorSensor();
    
    tank = myMotor.MoveTank(OUTPUT_A, OUTPUT_B)
    tank.cs = ev3.ColorSensor()
    tank.ts = ev3.TouchSensor()


    assert cs.connected  # measures light intensity
    cs.mode = 'COL-REFLECT'  # measure light intensity
    #   cs.mode = 'RGB-RAW'  # measure light intensity

    lm = ev3.LargeMotor('outA');
    assert lm.connected  # left motor
    rm = ev3.LargeMotor('outB');
    assert rm.connected  # right motor


    # dt = 5500

    def __init__(self, **kwargs):
        for keys, value in kwargs.items():
            if (keys == "cmode"):
                self.cs.mode = targetMode(value)
           # if(keys == 'speed'):
            #    self.speed=value
            #if(keys=='time'):
            #    self.time=value
        print("robo cmode: " + str(self.cs.mode))
    def makesound(self):
        #Sound.tone([(264, 500, 200), (352, 500, 200),(528, 1000, 100)]).wait()
        #Sound.play('VOLUME_uq83n-e4wo7.wav').wait()
        Sound.speak('Hello, my name is E V 3!').wait()
        Sound.speak('I play Tic Tac Toe Mother')
        Sound.tone(264, 2000)

    def run_modes(self, ar, **kwargs):
        print("rmode: " + str(ar))
     #   print(args.__len__())
        if(ar =="run"):
            print("run in if ")
            self.run(**kwargs)

        elif(ar == "mea"):
            self.measure(**kwargs)
        elif(ar == "runmea"):
            self.run_measure(**kwargs)
        elif(ar=="fol"):

            self.lineF(**kwargs)
           # self.lineF(**kwargs)
        elif(ar=="way"):
            self.goWay(**kwargs)
        elif (str(ar) != str("run")):
            print('a: ' + ar)
            print('a len: ' + str(len(ar)))
            print('a rep: ' + repr(ar))
            print('b: ' + "run")

            print('b len: ' + str(len("run")))
            print('b rep: ' + repr("run"))
      #  return switcher.get(ar, lambda *_: "ERROR: Tank type not valid")(*args)


    def run_measure(self,**kwarg):


        self.goWay(**kwarg)
        print(self.measure())
    def measure(self,**kwarg):
        print("in measure with:  "+ self.cs.mode)
        target_val = self.cs.value()
        self.cs.reflected_light_intensity
        print()
        print("refl line foll u know u shit: "+str(self.cs.reflected_light_intensity))
        print("target v:" + str(targetvalue(target_val)))

        print("red: " + str(self.cs.red))
        print("green: " + str(self.cs.green))
        print("blue:" + str(self.cs.blue))

        print("raw: " + str(self.cs.raw))

        self.cs.mode = 'COL-COLOR'
        print("in measure with:  "+ self.cs.mode)

        print("COL COLOR")
        print("refl line foll u know u shit: " + str(self.cs.reflected_light_intensity))
        print("target v:" + str(targetvalue(target_val)))

        print("red: " + str(self.cs.red))
        print("green: " + str(self.cs.green))
        print("blue:" + str(self.cs.blue))

        print("raw: " + str(self.cs.raw))
        messages = {'Aktion': 'Befehl', 'is': 2, 'found': False}
        if self.cs.red<86 and self.cs.blue>95 and self.cs.green>95:
            messages = {'Aktion': 'Befehl', 'is': 2, 'found': True}

        return json.dumps(messages).encode('utf-8')

    def run(self,**kwarg):
        print("in run")
        print('kwarg: power '+str(kwarg.power))
        self.lm.run_timed(speed_sp=kwarg.power, time_sp=dt, stop_action=stop_action)
        self.rm.run_timed(speed_sp=kwarg.power, time_sp=dt, stop_action=stop_action)


    def run_measuretry(self): ##tryout methode
        print("in run_measureTRY")
        self.lm.run_timed(speed_sp=power, time_sp=dt, stop_action=stop_action)
        self.rm.run_timed(speed_sp=power, time_sp=dt, stop_action=stop_action)
        self.measure(self)
        return 0

    def change_C_Mode(self,mode):
        self.cs.mode=mode
    def turn(self,tank,**kwargs):

        tank.on_for_degrees(kwargs.get('lspeed'), kwargs.get('rspeed'), kwargs.get('degrees'))
    def turn_corner(self,**kwargs):
        print('turn')

        self.tank.on_for_degrees(kwargs.get('lspeed'), kwargs.get('rspeed'), kwargs.get('degrees'))
        while self.cs.reflected_light_intensity> kwargs.get('target_light_intensity')+2:
            print(self.cs.reflected_light_intensity)
            self.tank.on_for_degrees(kwargs.get('lspeed'), kwargs.get('rspeed'), 10)

    def lineF(self,**kwargs):
        print(type(kwargs.get('ms')))
        print(kwargs.get('ms'))
        fj=True
       # ga = int(kwargs.get('ms'))
       # tank = ev3dev2.motor.MoveTank(self.lm,self.rm)

        print(dict(kwargs))
        print(kwargs.get('lspeed'))
        while(True):
            res= self.tank.follow_line(
             #   kp=0.3, ki=0.05, kd=0.2,
                #follow_for=follow_for_forever, #todo follow ms kwarg
                folow_for=follow_for_ms,jf=fj,
                **kwargs
            )
            print(res.get('return'))
            if res.get('return')=="off_line":
                print('offline')
                x = self.readjust(**res)
                fj=False
            else:
                return res




    def readjust(self,**kwargs):
        right =False
        counter =0
        mc=50
        if kwargs.get('lms')< (kwargs.get('rms')):
            right=True
      #  tank.on_for_degrees(kwargs.get('lspeed'), kwargs.get('rspeed'), kwargs.get('degrees'))
        while self.cs.reflected_light_intensity > kwargs.get('target_light_intensity')+2:  #todo i say kwargs targetet light reflection
          #  print(self.cs.reflected_light_intensity)
#            self.tank.on_for_degrees(kwargs.get('lms')*-1, kwargs.get('rms')*-1, 10)
            print(counter)
            if(right):
                if counter<mc:
                    self.tank.on_for_degrees(0, kwargs.get('rms') * -0.5, 10)
                else:
                    self.tank.on_for_degrees(kwargs.get('lms') * -0.5, 0, 10)

            else:
                if counter<mc:
                    self.tank.on_for_degrees(kwargs.get('lms') * -0.5, 0, 10)
                else:
                    self.tank.on_for_degrees(0, kwargs.get('rms') * -0.5, 10)
            counter=counter+1
        return True



    def goWay(self,**kwargs):
        orders=kwargs.get('way') #ORDAAAAAAAAAAAAAAAAAAAA
        strlen=len(orders)
        print("ordeaaaaaaa: "+orders)

        #idx=0
       # res = self.lineF(**kwargs)
        res={'return':"ecke"}
        for i in range (strlen) :
            if res.get('return')=="ecke":
                self.cs.mode='COL-REFLECT'
                if(orders[i]=='s'):
                    print("IN FUCKING STRAIGHT")
                    print(orders[i])
                    res=self.lineF(**kwargs)
                  #  print("res after lineF:"+dict(res))

                if(orders[i]=='r'):
                    print("IN FUCKING RIGHT")

                    print(orders[i])
                    self.tank.on_for_seconds(kwargs.get('uspeed'),kwargs.get('uspeed'), kwargs.get('rot'))

                    self.tank.on_for_degrees(kwargs.get('ulspeed'), kwargs.get('urspeed'), kwargs.get('degrees'))
                    while self.cs.reflected_light_intensity > kwargs.get('target_light_intensity') + 2:
                        print(self.cs.reflected_light_intensity)
                        self.tank.on_for_degrees(kwargs.get('rspeed'), kwargs.get('lspeed'), 10)
                      #  self.tank.on_for_degrees(kwargs.get('lspeed'), kwargs.get('rspeed'), 10)
                    self.lineF(**kwargs)


                if (orders[i] == 'l'):
                    print(orders[i])
                    print("IN FUCKING LEFRT")

                #    help = kwargs.get('lspeed')
                 #   kwargs['lspeed']=kwargs.get('rspeed')
                  #  kwargs['rspeed']=help
                    self.tank.on_for_seconds(kwargs.get('uspeed'),kwargs.get('uspeed'), kwargs.get('rot'))

                    self.tank.on_for_degrees(kwargs.get('urspeed'), kwargs.get('ulspeed'), kwargs.get('degrees'))
                    while self.cs.reflected_light_intensity > kwargs.get('target_light_intensity') + 2:
                        print(self.cs.reflected_light_intensity)
                        self.tank.on_for_degrees(kwargs.get('lspeed'), kwargs.get('rspeed'), 10)
                        #self.tank.on_for_degrees(kwargs.get('rspeed'), kwargs.get('lspeed'), 10)
                    self.lineF(**kwargs)

        return True

    def turn_new(self,right=True,**kwargs):
        dirs= kwargs.get('rspeed')
        offdirs=kwargs.get('lspeed')
        self.tank.on_for_degrees(dirs,offdirs)
