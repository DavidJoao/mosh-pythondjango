#########################################      Classes
class Point:
    def move(self):
        print('move')
    
    def draw(self):
        print('draw')

    
point_one = Point()
point_one.draw()

#########################################      Constructors
#If we want to define extra attributes, we need to make a constructor:

class SecondPoint:
    def __init__(self, x, y): #This way we initialize our object
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')

point = SecondPoint(10, 20)

#Exercise

class Person:
    def __init__(self, name):
        self.name = name # "self" references the object

    def talk(self):
        print(f'Hello! I am {self.name}')

david = Person('David Sandoval')
tinker = Person('Tinkerbeliana')
david.talk()
tinker.talk()

#########################################      Inheritance
class Mammal:
    def walk(self):
        print('walk')

class Dog(Mammal):
    pass


class Cat(Mammal):
    pass
    
tinker = Dog()
tinker.walk()
