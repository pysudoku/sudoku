'''
Created on Jul 10, 2013

@author: Jimena Terceros
'''
import unittest
from sudoku.settings.Level import Level


class TestLevel(unittest.TestCase):


    def setUp(self):
        self.levelName = "Level 2"
        self.minLevel = 10
        self.maxLevel = 20
        self.levels = []


    def tearDown(self):
        pass

    def test_Given_two_equal_levels__then_should_eq_should_return_true(self):
        level1 = Level(self.levelName, self.minLevel, self.maxLevel)
        level2 = Level(self.levelName, self.minLevel, self.maxLevel)
        self.assertTrue(level1 == level2)
        
    def test_Given_two_not_equal_levels__then_should_eq_should_return_false(self):
        level1 = Level("otherLevel", self.minLevel, self.maxLevel)
        level2 = Level(self.levelName, self.minLevel, self.maxLevel)
        self.assertFalse(level1 == level2)

    def test_level_eq_int_should_return_false(self):
        level1 = Level("otherLevel", self.minLevel, self.maxLevel)
        level2 = 2
        self.assertFalse(level1 == level2)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()