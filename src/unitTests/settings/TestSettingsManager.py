'''
Created on Jul 11, 2013

@author: Jimena Terceros
'''
import unittest
import os
from sudoku.settings.SettingsManager import SettingsManager
from sudoku.settings.Level import Level


class TestSettingsManager(unittest.TestCase):

    def setUp(self):
        self.fileName = "test.xml"

    def tearDown(self):
        if os.path.exists(self.fileName):
            os.remove(self.fileName)


    def test_If_There_is_Not_ConfigFile_Then_The_Settings_Manager_Should_Create_A_New_Config_File_With_Default_Values(self):
        manager = SettingsManager(self.fileName)
        manager.load()
        settings = manager.getSettings()
        defaultLevel = Level(settings.DEFAULT_LEVEL_NAME, settings.DEFAULT_MIN, settings.DEFAULT_MAX)
        
        self.assertTrue(os.path.exists(self.fileName))
        self.assertEqual(settings.DEFAULT_ALGORITHM_NAME, settings.getAlgorithmName())
        self.assertEqual(settings.DEFAULT_OUTPUT_TYPE, settings.getOutputType())
        self.assertEqual(settings.DEFAULT_LEVEL_NAME, settings.getDefaultLevel())
        self.assertEqual(defaultLevel, settings.getLevels()[0])

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()