'''
Created on Jul 9, 2013

@author: Jimena Terceros
'''
import unittest
from sudoku.settings.Settings import Settings


class TestSettings(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_the_create_default_settings_should_set_default_value_for_output_type(self):
        settings = Settings("")
        settings.createDefaultSettings()
        
        self.assertEqual(settings.DEFAULT_OUTPUT_TYPE, settings.getOutputType())
        self.assertEqual(settings.DEFAULT_ALGORITHM_NAME, settings.getalgorithmName())
        self.assertEqual(settings.DEFAULT_LEVEL_NAME, settings.getdefaultLevel())
        self.assertEqual(1, len(settings.getlevels()))
        self.assertEqual(settings.DEFAULT_LEVEL_NAME, settings.getlevels()[0])


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()