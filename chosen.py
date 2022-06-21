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


"""
An example of Polymorphism
"""
class Animal:
    def __init__(self, name):   # Constructor of the class
        self.name = name
        
    def speak(self):            # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")
        
class Dog(Animal):
    
    def speak(self):
        return self.name + ' says Woof!'
        
class Cat(Animal):
    
    def speak(self):
        return self.name + ' says Meow!'
        
fido = Dog('Fido')
isis = Cat('Isis')

print(fido.speak())
print(isis.speak())