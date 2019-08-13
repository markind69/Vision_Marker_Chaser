from math import sin, cos, radians, pi


class Robot:
    Vd = 5
    T0 = 0
    Vo = 0
    Tm = 5

    def __init__(self, name, color, armor, weapon, speed):
        self.name = name
        self.color = color
        self.armor = armor
        self.weapon = weapon
        self.speed = speed

    def program(self):
        return (f'My designation is {self.name} and my armor is {self.color}'
                f' {self.armor} and my Program\n is to destroy all humans with '
                f'my {self.weapon}\n at {self.speed} meters per second.')

    def mecanum(self, Vd, Vo, T0):
        self.V0 = Vd * (sin(radians(T0) + pi / 4) + Vo)
        self.V1 = Vd * (cos(radians(T0) + pi / 4) - Vo)
        self.V2 = Vd * (cos(radians(T0) + pi / 4) + Vo)
        self.V3 = Vd * (sin(radians(T0) + pi / 4) - Vo)
        return [self.V0, self.V1, self.V2, self.V3]


Robot_1 = Robot('Blast-Star', 'Red', 'Titanium', 'Ion Cannon', 20)
Robot_2 = Robot('Eye-Scythe', 'Silver', 'Aluminum', 'Mass Driver', 30)
Robot_3 = Robot('Vader', 'Black', 'Steel', 'Plasma Beam', 30)

print(Robot_1.program())
print(Robot_2.program())

print(Robot_2.armor)
print(Robot_3.name)
print(Robot_1.weapon)

V = Robot_1.mecanum(5,2,23)
V = Robot_2.mecanum(6,2,27)
print(V)
V = Robot_3.mecanum(7,1,13)
print(type(V))
print(Robot_2.V0)
print(Robot_3.V1)
print(Robot_1.V3)
# V = mecanum(Vd, Vo, T0)
# chassis_ctrl.set_wheel_speed(V[0], V[1], V[2], V[3])
# time.sleep(Tm)