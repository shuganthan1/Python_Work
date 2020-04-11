#four pillars of object oriented programming
#abstraction,inheritance, encapusation, polymorphism

#abstraction - displaying only essential info to user and hiding the detail from user

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