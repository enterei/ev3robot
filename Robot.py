from ev3dev2 import DeviceNotDefined

from MySocket import MySocket
from ColorSensor import ColorSensor
import ev3dev.ev3 as ev3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, follow_for_ms, follow_for_forever, \
    SpeedInvalid, LineFollowErrorTooFast, speed_to_speedvalue, LineFollowErrorLostLine
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
        print("in measure")
        target_val = self.cs.value()

        print()
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
       # tank = ev3dev2.motor.MoveTank(self.lm,self.rm)
        tank = MoveTank(OUTPUT_A,OUTPUT_B)
        tank.cs=ev3.ColorSensor()
        print(dict(kwargs))
        tank.cfollow_line(
        kp=11.3, ki=0.05, kd=3.2,
        speed=SpeedPercent(kwargs.get('speed')),
        follow_for=follow_for_ms,
        ms=4500
    )
    def cfollow_line(self,
                    kp,
                    ki,
                    kd,
                    speed,
                    target_light_intensity=None,
                    follow_left_edge=True,
                    white=60,
                    off_line_count_max=20,
                    sleep_time=0.01,
                    follow_for=follow_for_forever,
                    **kwargs):
        """
        PID line follower

        ``kp``, ``ki``, and ``kd`` are the PID constants.

        ``speed`` is the desired speed of the midpoint of the robot

        ``target_light_intensity`` is the reflected light intensity when the color sensor
            is on the edge of the line.  If this is None we assume that the color sensor
            is on the edge of the line and will take a reading to set this variable.

        ``follow_left_edge`` determines if we follow the left or right edge of the line

        ``white`` is the reflected_light_intensity that is used to determine if we have
            lost the line

        ``off_line_count_max`` is how many consecutive times through the loop the
            reflected_light_intensity must be greater than ``white`` before we
            declare the line lost and raise an exception

        ``sleep_time`` is how many seconds we sleep on each pass through
            the loop.  This is to give the robot a chance to react
            to the new motor settings. This should be something small such
            as 0.01 (10ms).

        ``follow_for`` is called to determine if we should keep following the
            line or stop.  This function will be passed ``self`` (the current
            ``MoveTank`` object). Current supported options are:
            - ``follow_for_forever``
            - ``follow_for_ms``

        ``**kwargs`` will be passed to the ``follow_for`` function

        Example:

        .. code:: python

            from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, SpeedPercent, follow_for_ms
            from ev3dev2.sensor.lego import ColorSensor

            tank = MoveTank(OUTPUT_A, OUTPUT_B)
            tank.cs = ColorSensor()

            try:
                # Follow the line for 4500ms
                tank.follow_line(
                    kp=11.3, ki=0.05, kd=3.2,
                    speed=SpeedPercent(30),
                    follow_for=follow_for_ms,
                    ms=4500
                )
            except LineFollowErrorTooFast:
                tank.stop()
                raise
        """
        if not self._cs:
            raise DeviceNotDefined(
                "The 'cs' variable must be defined with a ColorSensor. Example: tank.cs = ColorSensor()")

        if target_light_intensity is None:
            target_light_intensity = self._cs.reflected_light_intensity

        integral = 0.0
        last_error = 0.0
        derivative = 0.0
        off_line_count = 0
        speed = speed_to_speedvalue(speed)
        speed_native_units = speed.to_native_units(self.left_motor)

        while follow_for(self, **kwargs):
            reflected_light_intensity = self._cs.reflected_light_intensity
            error = target_light_intensity - reflected_light_intensity
            integral = integral + error
            derivative = error - last_error
            last_error = error
            turn_native_units = (kp * error) + (ki * integral) + (kd * derivative)

            if not follow_left_edge:
                turn_native_units *= -1

            left_speed = SpeedNativeUnits(speed_native_units - turn_native_units)
            right_speed = SpeedNativeUnits(speed_native_units + turn_native_units)

            # Have we lost the line?
            if reflected_light_intensity >= white:
                off_line_count += 1

                if off_line_count >= off_line_count_max:
                    self.stop()
                    raise LineFollowErrorLostLine("we lost the line")
            else:
                off_line_count = 0

            if sleep_time:
                time.sleep(sleep_time)

            try:
                self.on(left_speed, right_speed)
            except SpeedInvalid as e:
                log.exception(e)
                self.stop()
                raise LineFollowErrorTooFast("The robot is moving too fast to follow the line")

        self.stop()