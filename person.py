class Person:
  def __init__(self, fname, lname):
    self.fname = fname
    self.lname = lname

  def talk(self):
    return ('{} is talking'.format(self.fname))


x = Person('shug','sarv')
x.talk()
