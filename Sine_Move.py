from time import sleep
from math import sin, cos, radians, pi, fabs

T0 = 0                # Init Theta Zero (direction of Translation)
Tm = 0.2              # Init Time Delay
Vd = 40               # Init Speed in RPM
vdmax = 59.9          # Set Max wheel RPM for tic toc
sign_changer1 = -1.0  # Tic toc for Heading
sign_changer2 = -1.0  # Tic toc for Theta Zero
sign_changer3 = 1.0   # Tic toc for Speed
start1 = 63           # Start Counter (treated as degrees)
stop1 = 230           # Stop Counter (sets total loops to be run)
trfact = 0.4          # Turn Radius Factor
ltfact = 30           # Lateral Translation Factor
vdfact = 30           # Speed Factor
t0max = 59.9          # Theta Zero tic toc threshold
voff = 45             # Speed offset in degrees
toff = 33             # Translate (Lateral) offset in degrees
roff = 66             # Radius of Turn Change Factor offset in degrees


def mecanum(Vd, Vo, T0):

    V0 = Vd * (sin(radians(T0) + pi / 4) + Vo)
    V1 = Vd * (cos(radians(T0) + pi / 4) - Vo)
    V2 = Vd * (cos(radians(T0) + pi / 4) + Vo)
    V3 = Vd * (sin(radians(T0) + pi / 4) - Vo)
    return V0, V1, V2, V3


for n in range(start1, stop1):
    Vo = (trfact * (1 + sin(radians((n+roff) * 10)))) * sign_changer1
    T0 = (ltfact * (1 + cos(radians((n+toff) * 10)))) * sign_changer2
    Vd = (vdfact * (1 + sin(radians((n+voff) * 10)))) * sign_changer3
    if fabs(Vo) < .01:   # Switches left / right turning near center
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
