'''
Created on Jul 16, 2013

@author: Jimena Terceros
'''
import unittest
import os
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.game.Game import Game
from sudoku.game.ReadConfigurationCommand import ReadConfigurationCommand

class TestReadConfiguration(unittest.TestCase):

    def setUp(self):
        #self.readconfig_parameters = {"param1":"test.xml"}
        self.file_name_parameter1 = None
        self.file_name_parameter2 = {}
        self.file_name_parameter3 = {'fileName5':"test.xml"}
        self.file_name_parameter4 = {'fileName':None}
        self.readconfig_parameters = {'fileName':"test.xml"}
        
    def tearDown(self):
        if os.path.exists(self.readconfig_parameters['fileName']):
            os.remove(self.readconfig_parameters['fileName'])

    def test_given_the_cmd_readconfiguration_with_valid_one_parameter_then_should_verity_that_it_has_only_one_parameter(self):
        try:
            cmd_read = ReadConfigurationCommand(self.readconfig_parameters)
        except InvalidCmdParametersException:
            self.fail("Was raised an unexpected InvalidCmdParametersException.")
    
    def test_given_the_cmd_readconfiguration_with_file_name_parameter_equal_to_None_then_should_trown_an_exception(self):
        try:
            cmd_read = ReadConfigurationCommand(self.file_name_parameter1)
            self.fail("Did not raise the exception")
        except InvalidCmdParametersException:
            pass
    
    def test_given_the_cmd_readconfiguration_without_fileName_parameter_then_should_trown_an_exception(self):
        try:
            cmd_read = ReadConfigurationCommand(self.file_name_parameter2)
            self.fail("Did not raise the exception")
        except InvalidCmdParametersException:
            pass
    
    def test_given_the_cmd_readconfiguration_with_parameter_different_than_filename_then_should_trown_an_exception(self):
        try:
            cmd_read = ReadConfigurationCommand(self.file_name_parameter3)
            self.fail("Did not raise the exception")
        except InvalidCmdParametersException:
            pass
    
    def test_given_the_cmd_readconfiguration_with_none_filename_parameter_then_should_trown_an_exception(self):
        try:
            cmd_read = ReadConfigurationCommand(self.file_name_parameter4)
            self.fail("Did not raise the exception")
        except InvalidCmdParametersException:
            pass
    
    def test_given_the_cmd_readconfiguration_with_valid_one_parameter_then_should_read_configuration(self):
        game = Game()
        cmd = ReadConfigurationCommand(self.readconfig_parameters)
        cmd.set_game(game)
        cmd.execute()
        
        self.assertTrue(game.settings_manager != None)
        
        settings = game.settings_manager.getSettings()
        self.assertTrue(settings != None)
        self.assertEqual(settings.DEFAULT_OUTPUT_TYPE, settings.getOutputType())
        self.assertEqual(settings.DEFAULT_ALGORITHM_NAME, settings.getAlgorithmName())
        self.assertEqual(settings.DEFAULT_LEVEL_NAME, settings.getDefaultLevel())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()