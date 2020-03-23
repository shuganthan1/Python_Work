#functions - it is a special relationship where each input has single output
#input  --->Blackbox --->Output

#function without arguments
# def hello():
#     print('Hello')
# hello()

#function with arguments
# def func (a,b):
#     return a+b
# print('The sum is',func(10,20))

#function with default argument
# def func(a=10,b=30):
#     return a+b
# print('The sum is',func())

#function with default and again passing the values
# def func(a=10,b=30):
#     return a+b
# print('The sum is ', func(20,40))

# def add(a,b):
#     return a+b
# print(add(2,6))

# def mutliplication(a,b):
#     return a*b
# print(mutliplication(2,8))
#
# def subtract(a,b):
#     return a-b
# print(subtract(7,2))
#
# def division(a,b):
#     return a/b
# print(division(4,2))

#class- a way of bringing both data and functionality together
#
# class Dog:
#     animal_kind = 'canine' #class variable # when a function is declared inside a class, it is called a method
#     def __init__(self,name,age):
#         self.name =name
#         self.age = age
#         #run &jump
#
#     def bark(self): #self  - referring to class dog #going to create another object so that i can make use of this
#         return('woof')
#     def eat(self):
#         return ('{} says I am eating chicken'.format(self.name))
# print(Dog.animal_kind)
# print(type(Dog))
# #creating objects from the class
# x = Dog('Fido',8)
# y=Dog('Dido',4)
# print('Name of my dog is',x.name)
# print('Age of my dog is',x.age)
# print(x.bark())
# print(x.eat())
# #
# # # creating a student class
# # have a method enrol:
# # print student type and some msg in the method enrol
# class Student:
#         def enrol(self):
#         return 'All good'
# print(Student.student_type)
# print(type(Student))
# y=Student()
# print(y.enrol())
#
# class Student:
#     student_type = 'Trainee' #class variable # when a function is declared inside a class, it is called a method
#     def __init__(self,name,age):
#         self.name =name
#         self.age = age
#
#     def room(self): #self  - referring to class dog #going to create another object so that i can make use of this
#         return('Room 1')
#     def subject(self):
#         return ('{} is studying '.format(self.name))
# print(Student.student_type)
# print(type(Student))
# #creating objects from the class
# x =Student('bob'6)
# y=Student('sam',4)
# print('Name of my student is',x.name)
# print('Age of student is',x.age)
# print(x.room())
# print(x.subject())

#create a car class
# class Car:
#     car_type = 'mini'
#     def speed(self):
#         return 'good choice'
# print(Car.car_type)
# print(type(Car))

# class FizzBuzz(object):
#
#     def start(self, end_number):
#         return ",".join(self._parse_numbers(end_number))
#
#     def _parse_numbers(self, end_number):
#         number_list = []
#         for number in range(1, end_number+1):
#             number_list.append(self.parse_number(number))
#         return number_list
#
#     def parse_number(self, number):
#         if self._is_number_divisible_by_five_and_three(number):
#             return "FizzBuzz"
#         elif self._is_number_divisible_by_three(number):
#             return "Fizz"
#         elif self._is_number_divisible_by_five(number):
#             return "Buzz"
#         else:
#             return str(number)
#
#     def _is_number_divisible_by_five_and_three(self, number):
#         return number % 15 == 0
#
#     def _is_number_divisible_by_three(self, number):
#         return number % 3 == 0
#
#     def _is_number_divisible_by_five(self, number):
#         return number % 5 == 0

# class Animal():
#     def __init__(self,name,colour,species = 'animal'):

#libraries and modules
# import random
# import math
# #useful for web scraping
#
# print(random.random())
# num_float =23.66
# print(math.ceil(num_float))
# print(math.floor(num_float))



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