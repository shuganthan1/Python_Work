#Encapulusation - in an object oriented python program, you can restrict access to methods and variables.
#this can prevent the data from being modified by accident and is known as encapsulation
#add __ be4 the method to restrict acces e.g def __eat
from reptile import *
class Snake(Reptile):
#name of class always capital
    def __init__(self,name,age):
        super().__init__(name,age)

        self.name=name
        self.age=age
    def seek_heat(self):
        return ('Let me see some sunshine')
    def sleep(self):
        return ('Please leave me to class')
Sidney =Snake('Doo',2)
print(Sidney.eat())
print(Sidney.sleep())

#Polymorphism - in python defines methods in the child class that have the same name as the methods in the parent class
#in Inheritance, the child class inherits the methods from the parent class
#also it is possible to modify a method in a child class that it has inherited from the parent class and this is called
#as method overriding  - when two method has same name  and prints one

#Lamda function - essentially anonymous function that can take multiple parameters but return only one expression

def add (num1,num2):
    return num1 + num2

addition = lambda num1, num2:num1 + num2
print(add(23,45))
print(addition(23,45))
savings = [234,567,674,78]
bonus = list(map(lambda x: x*1.1,savings))
print(bonus)