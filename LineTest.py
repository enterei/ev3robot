import ev3dev.ev3 as ev3
class LineTest:
    def __init__(self):
        self.btn = ev3.Button()
        self.shut_down = False

    def run(self):
        cs = ev3.ColorSensor();
        assert cs.connected  # measures light intensity

        us = ev3.UltrasonicSensor();
        assert us.connected  # measures distance

        cs.mode = 'RGB-RAW'  # measure light intensity

        us.mode = 'US-DIST-CM'  # measure distance in cm
        print(cs.mode)

        print(cs.green)
        print(cs.blue)
        print(cs.red)
        print(cs.raw)
        cs.mode = 'COL-REFLECT'  # measure light intensity
        print(cs.green)
        print(cs.blue)
        print(cs.red)
        print(cs.raw)

