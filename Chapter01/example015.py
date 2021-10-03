# Inheritance

from example013 import Employee

class specialEmployee(Employee):
    def __init__(self, name, rate, bonus):
        Employee.__init__(self, name, rate)       #calls the base class
        self.bonus = bonus

    def hours(self, numHours):
        self.owed += numHours*self.rate + self.bonus
        return("%.2f hours worked" % numHours)

# Example issubclass() to check whether a class is a subclass of another class
# Example isinstance() to check if an object belongs to a class or not

print(issubclass(specialEmployee, Employee))
print(isinstance(Employee, specialEmployee))

d = specialEmployee("packt", 20, 100)
b = Employee("packt", 20)

print(isinstance(b, specialEmployee))
print(isinstance(b, Employee))

    

