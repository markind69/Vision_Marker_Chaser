class Robot:

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

Robot_1 = Robot('Blast-Star', 'Red', 'Titanium', 'Ion Cannon', 20)
Robot_2 = Robot('Eye-Scythe', 'Silver', 'Aluminum', 'Mass Driver', 30)
Robot_3 = Robot('Vader', 'Black', 'Steel', 'Plasma Beam', 30)

print(Robot_1.program())
print(Robot_2.program())

print(Robot_2.armor)
print(Robot_3.name)
print(Robot_1.weapon)
