from MySocket import MySocket
from ColorSensor import ColorSensor
import ev3dev.ev3 as ev3

stop_action= "coast"
power = 200
dt = 5500

class Robot:
    socket = MySocket()
    colorS = ColorSensor()
    lm = ev3.LargeMotor('outB');
    assert lm.connected  # left motor
    rm = ev3.LargeMotor('outC');
    assert rm.connected  # right motor
    #dt = 5500


    def run(self):
        self.lm.run_timed(speed_sp = power,time_sp=dt,stop_action=stop_action)
        self.rm.run_timed(speed_sp = power,time_sp=dt,stop_action=stop_action)

        print("run")

