import myMotor
from MySocket import MySocket
from ColorSensor import ColorSensor
import ev3dev.ev3 as ev3
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

        elif (str(ar) != str("run")):
            print('a: ' + ar)
            print('a len: ' + str(len(ar)))
            print('a rep: ' + repr(ar))
            print('b: ' + "run")

            print('b len: ' + str(len("run")))
            print('b rep: ' + repr("run"))
      #  return switcher.get(ar, lambda *_: "ERROR: Tank type not valid")(*args)


    def run_measure(self,**kwarg):


        print("in run_measure")
        for i in range(kwarg.time):
            self.run(kwarg)
            self.measure(kwarg)

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

    def lineF(self,**kwargs):
        print(type(kwargs.get('ms')))
        print(kwargs.get('ms'))
        ga = int(kwargs.get('ms'))
       # tank = ev3dev2.motor.MoveTank(self.lm,self.rm)
        tank = myMotor.MoveTank(OUTPUT_A,OUTPUT_B)
        tank.cs=ev3.ColorSensor()
        print(dict(kwargs))

        if(tank.follow_line(
         #   kp=0.3, ki=0.05, kd=0.2,
            follow_for=follow_for_ms,  #todo follow ms kwarg
            **kwargs
        ).get('ecke')==True and kwargs.get('turn')==True):

            tank.on_for_degrees(kwargs.get('lspeed'),kwargs.get('rspeed'),kwargs.get('degrees'))
