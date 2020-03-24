import ev3dev.ev3 as ev3
from time import sleep

class LineTest:
    def __init__(self):
        self.btn = ev3.Button()
        self.shut_down = False

    def meassure(self):
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
        cs.mode = 'COL-AMBIENT'  # measure light intensity
        print(cs.green)
        print(cs.blue)
        print(cs.red)
        print(cs.raw)

def run(self):
    cs = ev3.ColorSensor();

#    us = ev3.UltrasonicSensor();
 #   assert us.connected  # measures distance

    cs.mode = 'COL-REFLECT'  # measure light intensity
  #  us.mode = 'US-DIST-CM'  # measure distance in cm

    # motors
    lm = ev3.LargeMotor('outB');
    assert lm.connected  # left motor
    rm = ev3.LargeMotor('outC');
    assert rm.connected  # right motor
    mm = ev3.MediumMotor('outD');
    assert mm.connected  # medium motor

    speed = 360 / 4  # deg/sec, [-1000, 1000]
    dt = 500  # milliseconds
    stop_action = "coast"

    # PID tuning
    Kp = 1  # proportional gain
    Ki = 0  # integral gain
    Kd = 0  # derivative gain

    integral = 0
    previous_error = 0

    # initial measurment
    target_value = cs.value()
    print(target_value)
    print(self.btn.down)


    end = 30

    # Start the main loop
    #while not self.shut_down:
    for x in range(end):
        print(self.btn.down)

        # deal with obstacles
      #  distance = us.value() // 10  # convert mm to cm

       # if distance <= 5:  # sweep away the obstacle
        #    mm.run_timed(time_sp=600, speed_sp=+150, stop_action="hold").wait()
         #   mm.run_timed(time_sp=600, speed_sp=-150, stop_action="hold").wait()

        # Calculate steering using PID algorithm
        error = target_value - cs.value()
        integral += (error * dt)
        derivative = (error - previous_error) / dt

        # u zero:     on target,  drive forward
        # u positive: too bright, turn right
        # u negative: too dark,   turn left

        u = (Kp * error) + (Ki * integral) + (Kd * derivative)

        # limit u to safe values: [-1000, 1000] deg/sec
        if speed + abs(u) > 1000:
            if u >= 0:
                u = 1000 - speed
            else:
                u = speed - 1000

        # run motors
        print("u ist:", u)
        if u >= 0:
            lm.run_timed(time_sp=dt, speed_sp=speed + u, stop_action=stop_action)
            rm.run_timed(time_sp=dt, speed_sp=speed - u, stop_action=stop_action)
            sleep(dt / 1000)
        else:
            lm.run_timed(time_sp=dt, speed_sp=speed - u, stop_action=stop_action)
            rm.run_timed(time_sp=dt, speed_sp=speed + u, stop_action=stop_action)
            sleep(dt / 1000)

        previous_error = error