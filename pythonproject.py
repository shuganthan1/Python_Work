class Trainee ():
    animal_kind = 'Canine'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def traineename(self):
        tname = input('give a trainee name: ')
        return ('{} '.format(self.fname, tname))