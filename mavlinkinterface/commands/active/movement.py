from time import sleep

def move3d(ml, sem, time, throttleX, throttleY, throttleZ):
    '''Throttle functions are integers from -100 to 100'''
    try:
        print("Moving in direction X=" + str(throttleX) + " Y=" + str(throttleY) + " Z=" + str(throttleZ) + " for " + str(time) + " seconds")
        x = 10 * throttleX
        y = 10 * throttleY
        z = 5 * throttleZ + 500
        for i in range(0, time):
            ml.mav.manual_control_send(
                ml.target_system,
                x,  # x [back(-1000), forward(1000)]
                y,  # y [left(-1000), right(1000)]
                z,  # z [down(0), up(1000)]
                0,  # r [ corresponds to a twisting of the joystick, with counter-clockwise being 1000 and clockwise being -1000, and the yaw of a vehicle]
                0)  # b [ A bitfield corresponding to the joystick buttons' current state, 1 for pressed, 0 for released. The lowest bit corresponds to Button 1]
            sleep(1)

    finally:
        sem.release()

def move(ml, sem, direction, time, throttle=100):
    try:
        print("Moving in direction: " + str(direction) + " at " + str(throttle) + "% throttle for " + str(time) + " seconds")
        x = y = 0
        if direction == "forward":
            x = 10 * throttle
        elif direction == "back":
            x = -10 * throttle
        elif direction == "left":
            y = -10 * throttle
        elif direction == "right":
            y = 10 * throttle

        for i in range(0, time):
            ml.mav.manual_control_send(
                ml.target_system,
                x,      # x [ forward(1000)-backward(-1000)]
                y,      # y [ left(-1000)-right(1000) ]
                500,    # z [ maximum being 1000 and minimum being 0 on a joystick and the thrust of a vehicle.]
                0,      # r [ corresponds to a twisting of the joystick, with counter-clockwise being 1000 and clockwise being -1000, and the yaw of a vehicle]
                0)      # b [ A bitfield corresponding to the joystick buttons' current state, 1 for pressed, 0 for released. The lowest bit corresponds to Button 1]
            sleep(1)

    finally:
        sem.release()

def moveAbsolute(ml, sem, direction, time, throttle=100):  # TODO
    # TODO: insert movement code here
    try:
        sleep(5)
    finally:
        sem.release()

def dive(ml, sem, time, throttle):
    '''
    :param time: the number of seconds to power the thrusters
    :param throttle: Throttle value is from -100 to 100, with negative indicating down
    '''
    print("Diving at " + str(throttle) + "% throttle for " + str(time) + "seconds")
    z = (throttle * 5) + 500
    i = 0
    while i < time:
        ml.mav.manual_control_send(
            ml.target_system,
            0,  # x [ forward(1000)-backward(-1000)]
            0,  # y [ left(-1000)-right(1000) ]
            z,  # z [ maximum being 1000 and minimum being 0 on a joystick and the thrust of a vehicle.]
            0,  # r [ corresponds to a twisting of the joystick, with counter-clockwise being 1000 and clockwise being -1000, and the yaw of a vehicle]
            0)  # b [ A bitfield corresponding to the joystick buttons' current state, 1 for pressed, 0 for released. The lowest bit corresponds to Button 1]
        sleep(0.5)
        i += 1
    sem.release()

def diveAbsolute(ml, sem, depth):  # TODO
    # TODO: insert movement code here
    try:
        sleep(5)
    finally:
        sem.release()

def surface(ml, sem):  # TODO
    # TODO: insert movement code here
    try:
        sleep(5)
    finally:
        sem.release()

def yaw(ml, sem, angle, absolute=False):
    try:
        print("Yawing by " + str(angle) + " degrees")
        while angle > 180:
            angle -= 360
        while angle < -180:
            angle += 360
        r = angle * (50 / 9)
        ml.mav.manual_control_send(
            ml.target_system,
            0,      # x [ forward(1000)-backward(-1000)]
            0,      # y [ left(-1000)-right(1000) ]
            500,    # z [ maximum being 1000 and minimum being 0 on a joystick and the thrust of a vehicle. ]
            r,      # r [ 500 will turn the drone 90 degrees ]
            0)      # b [ A bitfield corresponding to the joystick buttons' current state, 1 for pressed, 0 for released. The lowest bit corresponds to Button 1 ]
        sleep(abs(r) / 200)

    finally:
        sem.release()
