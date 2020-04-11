from animal import *
class Reptile(Animal):

    def __init__(self,name,age):
         super()._init_(name,age)
    def sleep(self):
        return ('zzz I am sleeping')
    def running(self,speed):
        return ('I am running in {} speed',speed)

# Rept1 = Reptile('Lizzard',5)
# Rept2 = Reptile('Mosy',8)
# print(Rept1.eat())
# print(Rept1.running(10))
Q9

def is_foo(param):
    if param == 'foo':
        return 'True'
    else:
        return 'False'
Q10
Q11 - super().__init__('hello')
Q12
def is_even_position(list_param,value):
    if list_param[value]%2==0:
        return 'True'
    else:
        return 'False'
t=[9,8,7,6,5,4,3,2,1,6]
print(is_even_position(t,6))
print(is_even_position(t,3))
print(is_even_position(t,1))
Q13

def solve(width,height,length,mass):
    volume =width * height*length
    bulky =volume>=1000000 or width >=150 or height >= 150 or length >= 150
    heavy = mass >=20
    if bulky and heavy:
        return 'Rejected'
    elif bulky or heavy:
        return 'Special'
    else:
        return 'Standard'