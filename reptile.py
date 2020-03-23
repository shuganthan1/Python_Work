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
