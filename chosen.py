class Circle:
    pi = 3.14
    
    # Circle gets instantiated with a radius
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi
        
    # Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius * new_radius * self.pi
        
    # Method for getting circumference
    def getCircumference(self):
        return self.radius * self.pi * 2

c = Circle()        
c.setRadius(2)

print('Radius is: ', c.radius)
print('Area is: ', c.area)
print('Circumference is: ', c.getCircumference())

"""
Example of Inheritance in Python
"""

class Animal:
    def __init__(self):
        print("Animal created")
        
    def whoAmI(self):
        print("Animal")
        
    def eat(self):
        print("Eating")
        
class Dog(Animal):
    def __init__(self):
        print("Dog created")
        
    def whoAmI(self):
        Animal.__init__(self)
        print("Dog")
        
    def bark(self):
        print("Woof!")