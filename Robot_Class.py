class Robot:

    def __init__(self, name, color, armor, weapon, speed):
        self.name = name
        self.color = color
        self.armor = armor
        self.weapon = weapon

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)