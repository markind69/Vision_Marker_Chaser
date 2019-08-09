from time import sleep
from math import sin, cos, radians, pi, fabs, acos, asin
T0 = 0
Tm = 0.2
Vd = 40
vdmax = 59.9
sign_changer1 = -1.0
sign_changer2 = -1.0
sign_changer3 = 1.0
start1 = 63
stop1 = 230
trfact = 0.4   # Turn Radius Factor
ltfact = 30    # Lateral Translation Factor
vdfact = 30     # Speed Factor
t0max = 60
voff = 45

def mecanum(Vd, Vo, T0):

    V0 = Vd * (sin(radians(T0) + pi / 4) + Vo)
    V1 = Vd * (cos(radians(T0) + pi / 4) - Vo)
    V2 = Vd * (cos(radians(T0) + pi / 4) + Vo)
    V3 = Vd * (sin(radians(T0) + pi / 4) - Vo)
    return V0, V1, V2, V3


for n in range(start1, stop1):
    Vo = (trfact * (1 + sin(radians(n * 10)))) * sign_changer1
    T0 = (ltfact * (1 + cos(radians(n * 10)))) * sign_changer2
    Vd = (vdfact * (1 + sin(radians((n+voff) * 10)))) * sign_changer3
    if fabs(Vo) < .01:
        sign_changer1 = sign_changer1 * -1.0
        print(sign_changer1)
    if fabs(T0) > t0max:
        sign_changer2 = sign_changer2 * -1.0
        print(sign_changer2)
    if fabs(Vd) > vdmax:
        sign_changer3 = sign_changer3 * -1.0
        print(sign_changer3)
    print(Vd, Vo, T0, n)
    V = mecanum(Vd, Vo, T0)
    # chassis_ctrl.set_wheel_speed(V[0], V[1], V[2], V[3])
    print(V[0], V[1], V[2], V[3])
    sleep(Tm)
