#four pillars of object oriented programming

#Inheritance is a mechanism in which one class acquires the property of another class
 from file import *
 class Reptile(Animal):

     def __init__(self,name,age):
         super()._init_(name,age)
    def sleep(self):
        return ('zzz I am sleeping')
    def running(self,speed):
        return ('I am running in {} speed',speed)

Rept1 = Reptile('Lizzard',5)
Rept2 = Reptile('Mosy',8)
print(Rept2.sleep())

#abstraction,inheritance, encapusation, polymorphism

#abstraction - displaying only essential info to user and hiding the detail from user

from file import *
Rept1 = Reptile('Lizzard',5)
Rept2 = Reptile('Mosy',8)
print.....

class Animal ():
    animal_kind = 'Canine'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        return ('{} says i am eating chicken'.format(self.name))
#in a different py file


# Dog1 = Animal('Nyme',10)
# Dog2 = Animal('Mone',5)
# print(Dog1.age())

#Encapulusation - in an object oriented python program, you can restrict access to methods and variables.
#this can prevent the data from being modified by accident and is known as encapsulation
#add __ be4 the method to restrict acces e.g def __eatm hiding the methods from user
from reptile import *
class Snake(Reptile):
#name of class always capital
    def __init__(self,name,age):
        super().__init__(name,age)   #inheritance

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
#as method overriding   - when two method has same name  and prints one from the child is used

#Lamda function - essentially anonymous function that can take multiple parameters but return only one expression

def add (num1,num2):
    return num1 + num2

addition = lambda num1, num2:num1 + num2
print(add(23,45))
print(addition(23,45))
savings = [234,567,674,78]
bonus = list(map(lambda x: x*1.1,savings))
print(bonus)