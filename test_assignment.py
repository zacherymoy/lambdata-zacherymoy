from unittest import TestCase
import unittest
from assignment import Person #Import anything you want

#class TestPerson(unittest.TestCase):
class TestPerson(TestCase):

    def test_ShowName(self):
        bobby = Person("Hank") # Whatever class you bring in treat as
        self.assertFalse(bobby.show_name(), "Hank")

if __name__ == "__main__":
    unittest.main()
