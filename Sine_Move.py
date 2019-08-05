# from time import sleep
from math import sin, cos, radians, pi, fabs
Tm = 5
Vd = 5
sign_changer = -1.0
# time.sleep(Tm)


def mechanum(Vd, Vo, T0):

    V0 = Vd * (sin(radians(T0) + pi / 4) + Vo)
    V1 = Vd * (cos(radians(T0) + pi / 4) - Vo)
    V2 = Vd * (cos(radians(T0) + pi / 4) + Vo)
    V3 = Vd * (sin(radians(T0) + pi / 4) - Vo)
    return [V0, V1, V2, V3]
# Demo - prints a sine curve with * and cos curve with #
# Modified to print something readable on the S1 Console
for n in range(28, 90):
    circle_1 = (1 * (1 + sin(radians(n * 10)))) * sign_changer
    print(circle_1)
    if fabs(circle_1) < .01:
        sign_changer = sign_changer * -1.0
        print(sign_changer)
    V = mechanum(5,circle_1,0)
    # chassis_ctrl.set_wheel_speed(V1, V2, V3, V4)
    print(V)
    # time.sleep(Tm)
