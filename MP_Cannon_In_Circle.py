from math import sin, cos, radians, pi
from time import sleep

Vd = 60       # Init Speed in RPM (100 is pretty fast)
Vo = 0.7      # Init Turn Factor (-3.0 to + 3.0)
T0 = 90       # Init Theta Zero (direction of Translation in degrees)
Tm = 5        # Time of movement in seconds


def mecanum(Vd, Vo, T0):

    V0 = Vd * (sin(radians(T0) + pi / 4) + Vo)
    V1 = Vd * (cos(radians(T0) + pi / 4) - Vo)
    V2 = Vd * (cos(radians(T0) + pi / 4) + Vo)
    V3 = Vd * (sin(radians(T0) + pi / 4) - Vo)
    return V0, V1, V2, V3


print(Vd, Vo, T0)
V = mecanum(Vd, Vo, T0)
# chassis_ctrl.set_wheel_speed(V[0], V[1], V[2], V[3])
print(V[0], V[1], V[2], V[3])
sleep(Tm)