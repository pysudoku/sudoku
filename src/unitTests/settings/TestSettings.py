'''
Created on Jul 9, 2013

@author: Jimena Terceros
'''
import unittest
from sudoku.settings.Settings import Settings
from sudoku.settings.Level import Level


class TestSettings(unittest.TestCase):

    def setUp(self):
        self.level1 = Level("Level 1", 5, 10)
        self.level2 = Level("Level 2", 11, 20)
        self.level3 = Level("Level 3", 21, 30)
        
        self.settings = Settings("")
        self.settings.addLevel(self.level1)
        self.settings.addLevel(self.level2)
        self.settings.addLevel(self.level3)
        
        self.defaultLevel = Level(self.settings.DEFAULT_LEVEL_NAME, self.settings.DEFAULT_MIN, self.settings.DEFAULT_MAX)
        
    def tearDown(self):
        pass
    
    def test_getLevelNone(self):
        level = self.settings.getLevel("Level 4")
        self.assertEqual(None, level)
    
    def test_getLevel(self):
        level = self.settings.getLevel("Level 2")
        self.assertEqual(self.level2, level)

    def test_the_create_default_settings_should_set_default_value_for_output_type(self):
        settings = Settings("")
        settings.createDefaultSettings()
        
        self.assertEqual(settings.DEFAULT_OUTPUT_TYPE, settings.getOutputType())
        self.assertEqual(settings.DEFAULT_ALGORITHM_NAME, settings.getAlgorithmName())
        self.assertEqual(settings.DEFAULT_LEVEL_NAME, settings.getDefaultLevel())
        self.assertEqual(3, len(settings.getLevels()))
        self.assertEqual(self.defaultLevel, settings.getLevels()[0])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()