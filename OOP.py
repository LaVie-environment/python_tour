#!/usr/bin/python3

class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
        
    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayCount()
emp2.displayCount()
print("Total Employee %d" % Employee.empCount)

'''
Review class on OOP
'''

class Employee:
    'Common base class for all employees'
    empCount = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
        
    def displayEmployee(self):
        print ("Name : ", self.name, ", Salary: ", self.salary)
        
emp1 = Employee("Zara", 2000) # This would create first object of Employee class
emp2 = Employee("Manni", 5000) # This would create second object of Employee class

emp1.displayEmployee()
emp2.displayEmployee()

print("Total Employee %d" % Employee.empCount)

emp1.age = 7 # Add an 'age' attribute.
emp1.age = 8 # Modify 'age' attribute.

