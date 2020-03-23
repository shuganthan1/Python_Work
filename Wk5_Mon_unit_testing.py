from unittestingfunctions import SimpleCalc
import unittest
class Calctests(unittest.TestCase):

   calc = SimpleCalc()

  def test_add(self):
    self.assertEqual(self.calc.add(2, 4), 6)


  def test_substract(self):
    self.assertEqual(self.calc.subtract(4, 2), 2)

  def test_multiply(self):
    self.assertEqual(self.calc.subtract(2, 2), 4)


if __name__ == '__main__':
        unittest.main()
