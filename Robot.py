from MySocket import MySocket
from ColorSensor import ColorSensor
import ev3dev.ev3 as ev3

from helper.targetValue import targetvalue

stop_action = "coast"
power = 200
dt = 500
speed = 200


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
            if (keys == "mode"):
                self.cs.mode = value
        print("robo mode: " + str(self.cs.mode))

    def run_modes(self, ar, *args):
        switcher = {
            'go': self.run(self, args),
            'measure': self.run_measure(self, args[0])
        }
        func = switcher.get(ar, "nothing")

    def run_mode(self, *args):
        return 0
    def run_measure(self, time):
        for i in range(time):
            self.run(self)
            self.measure(self)

    def measure(self):
        self.cs.mode = 'COL-REFLECT'
        target_val = self.cs.value()

        print()
        print("target v:" + str(targetvalue(target_val)))

        print("red: " + str(self.cs.red))
        print("green: " + str(self.cs.green))
        print("blue:" + str(self.cs.blue))

        print("raw: " + str(self.cs.raw))

    def run(self):
        self.lm.run_timed(speed_sp=power, time_sp=dt, stop_action=stop_action)
        self.rm.run_timed(speed_sp=power, time_sp=dt, stop_action=stop_action)

        print("run")

    def run_measuretry(self, modus):
        self.lm.run_timed(speed_sp=power, time_sp=dt, stop_action=stop_action)
        self.rm.run_timed(speed_sp=power, time_sp=dt, stop_action=stop_action)
        self.measure(self, modus)
        return 0

    def change_C_Mode(self,mode):
        self.cs.mode=mode
