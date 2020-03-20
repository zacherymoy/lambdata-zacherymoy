from unittest import TestCase
import unittest
from assignment import Person #Import anything you want
from assignment import BasicMath

#class TestPerson(unittest.TestCase):
class TestPerson(TestCase):

    def test_ShowName(self):
        bobby = Person("Hank") # Whatever class you bring in treat as
        self.assertFalse(bobby.show_name(), "Hank")

class TestBasicMath(unittest.TestCase):

    def test_add(self):
        result = BasicMath.add(10, 5)
        self.assertEqual(result, 15)
        self.assertEqual(BasicMath.add(10, 5), 15)
        self.assertEqual(BasicMath.add(-1, -1), -2)

    # def test_subtract(self):
    #     self.assertEqual(calc.subtract(10, 5), 5)
    #     self.assertEqual(calc.subtract(-1, 1), -2)
    #
    # def test_multiply(self):
    #     self.assertEqual(calc.multiply(10, 5), 50)

if __name__ == "__main__":
    unittest.main()
