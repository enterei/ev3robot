from MySocket import MySocket
from ColorSensor import ColorSensor
import ev3dev.ev3 as ev3

from helper.targetValue import targetvalue, targetMode

stop_action = "coast"
power = 200
dt = 500
speed = 200
time = 10


class Robot:
    socket = MySocket()
    colorS = ColorSensor()
    cs = ev3.ColorSensor();
    assert cs.connected  # measures light intensity
    cs.mode = 'COL-REFLECT'  # measure light intensity
    #   cs.mode = 'RGB-RAW'  # measure light intensity

    lm = ev3.LargeMotor('outB');
    assert lm.connected  # left motor
    rm = ev3.LargeMotor('outC');
    assert rm.connected  # right motor

    # dt = 5500

    def __init__(self, **kwargs):
        for keys, value in kwargs.items():
            if (keys == "cmode"):
                self.cs.mode = targetMode(value)
        print("robo cmode: " + str(self.cs.mode))

    def run_modes(self, ar, *args):
        switcher = {
            'run': self.run(self, args),
            'mea': self.measure(),
            'runmea': self.run_measure()
        }
        func = switcher.get(ar, "nothing")

    def run_mode(self, *args):
        return 0
    def run_measure(self):
        for i in range(self.time):
            self.run(self)
            self.measure(self)

    def measure(self):
        target_val = self.cs.value()

        print()
        print("target v:" + str(targetvalue(target_val)))

        print("red: " + str(self.cs.red))
        print("green: " + str(self.cs.green))
        print("blue:" + str(self.cs.blue))

        print("raw: " + str(self.cs.raw))

    def run(self,*args):
        self.lm.run_timed(speed_sp=power, time_sp=dt, stop_action=stop_action)
        self.rm.run_timed(speed_sp=power, time_sp=dt, stop_action=stop_action)


    def run_measuretry(self): ##tryout methode
        self.lm.run_timed(speed_sp=power, time_sp=dt, stop_action=stop_action)
        self.rm.run_timed(speed_sp=power, time_sp=dt, stop_action=stop_action)
        self.measure(self)
        return 0

    def change_C_Mode(self,mode):
        self.cs.mode=mode
