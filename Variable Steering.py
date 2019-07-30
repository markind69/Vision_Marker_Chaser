from math import sin, cos, radians, pi

'''
VX is the Speed Multiplier for Wheel X
Vd is mostly a constant - the max speed you want for this run
T0 is Theta Zero the desired direction of travel, hopefully to be variable
Vo is a Steering Factor - 0 is straight ahead, negative values turn left
'''
Vd = 5
T0 = 0
Vo = 0
Tm = 0


def mechanum(Vd, Vo, T0):
    V1 = Vd * (sin(radians(T0) + pi / 4) + Vo)
    V2 = Vd * (cos(radians(T0) + pi / 4) - Vo)
    V3 = Vd * (cos(radians(T0) + pi / 4) + Vo)
    V4 = Vd * (sin(radians(T0) + pi / 4) - Vo)
    return [V1, V2, V3, V4]


V = mechanum(Vd, Vo, T0)
# chassis_ctrl.set_wheel_speed(V[0], V[1], V[2], V[3])
# time.sleep(Tm)

print(V)
print(V[0], V[1], V[2], V[3])
print(Vd, Vo, T0)




'''
def mechanum(Vd, Vo, T0):
    V1 = Vd * (sin(radians(T0) + 0.7854) + Vo)
    V2 = Vd * (cos(radians(T0) + 0.7854) - Vo)
    V3 = Vd * (cos(radians(T0) + 0.7854) + Vo)
    V4 = Vd * (sin(radians(T0) + 0.7854) - Vo)
    return [V1, V2, V3, V4]


for count in range(3):
    mecanum(Vd, Vo, T0)
    chassis_ctrl.set_wheel_speed(V1, V2, V3, V4)
    time.sleep(2)

chassis_ctrl.set_trans_speed(0)

# Driver code to test above method
t = fun()
print(t.str)
print(t.x)



class Mechanum:
    def __init__(self):
        self.V1 = Vd * (sin(radians(T0) + 0.7854) + Vo)
        self.V2 = Vd * (cos(radians(T0) + 0.7854) - Vo)
        self.V3 = Vd * (cos(radians(T0) + 0.7854) + Vo)
        self.V4 = Vd * (sin(radians(T0) + 0.7854) - Vo)
'''
