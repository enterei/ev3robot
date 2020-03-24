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

        cs.mode = 'COL-REFLECT'  # measure light intensity

        us.mode = 'US-DIST-CM'  # measure distance in cm
        target_value = cs.value()


        target_value_name=cs.value()
        print(target_value)
        print(cs.raw())
