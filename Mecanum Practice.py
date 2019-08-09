T0 = 0                # Init Theta Zero (direction of Translation)
Tm = 0.2              # Init Time Delay
Vd = 20               # Init Speed in RPM
start1 = 1            # Start Counter (treated as degrees)
stop1 = 30            # Stop Counter (sets total loops to be run)


def mecanum(Vd, Vo, T0):

    V0 = Vd * (sin(radians(T0) + pi / 4) + Vo)
    V1 = Vd * (cos(radians(T0) + pi / 4) - Vo)
    V2 = Vd * (cos(radians(T0) + pi / 4) + Vo)
    V3 = Vd * (sin(radians(T0) + pi / 4) - Vo)
    return V0, V1, V2, V3


for n in range(start1, stop1):
    print(Vd, Vo, T0, n)
    V = mecanum(Vd, Vo, T0)
    # chassis_ctrl.set_wheel_speed(V[0], V[1], V[2], V[3])
    print(V[0], V[1], V[2], V[3])
    sleep(Tm)
