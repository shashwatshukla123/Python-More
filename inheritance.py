#Python Inheritance
#https://www.w3schools.com/python/python_inheritance.asp
#Inheritance allows us to define a class that inherits all the methods and properties from another class.

#Parent class is the class being inherited from, also called base class.

#Child class is the class that inherits from another class, also called derived class.


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()
#------------------------------------
#Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
