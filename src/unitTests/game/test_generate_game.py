'''
Created on Jul 17, 2013

@author: Administrator
'''
import unittest
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.game.Game import Game
from sudoku.game.GenerateGame import GenerateGameCommand
from sudoku.generator.generator import Generator
from sudoku.settings.SettingsManager import SettingsManager


class TestGenerateGameCommand(unittest.TestCase):


    def setUp(self):
        self.valid_params = {'level': 'EASY'}
        self.invalid_params = {'level': 'EASY', "ANOTHER_PARAM": "ANOTHER_PARAM_VALUE"} 
        self.none_param = {'level': None}
        self.int_param = {'level': 2}

    def tearDown(self):
        pass

    def test_an_InvalidCmdParametersException_should_be_raised_if_game_is_None(self):
        with self.assertRaises(InvalidCmdParametersException):
            cmd = GenerateGameCommand(self.valid_params)
            cmd.execute()

    def test_an_InvalidCmdParametersException_should_be_raised_if_too_many_parameters_are_given(self):
        with self.assertRaises(InvalidCmdParametersException):
            cmd = GenerateGameCommand(self.invalid_params)

    def test_an_InvalidCmdParametersException_should_be_raised_if_parameter_has_int_value(self):
        with self.assertRaises(InvalidCmdParametersException):
            game = Game()
            cmd = GenerateGameCommand(self.int_param)
            cmd.set_game(game)
            cmd.execute()
            
    def test_if_level_name_is_easy_then_an_easy_level_sudoku_puzzle_should_be_generated(self):
        valid_params = {'level': 'EASY'}
        settings_manager = SettingsManager('mySettings.xml')
        settings_manager.load()
        game = Game()
        game.set_settings_manager(settings_manager)
        cmd = GenerateGameCommand(valid_params)
        cmd.set_game(game)
        cmd.execute()
        self.assertIsNotNone(game.initial_sudoku)
        
    def test_if_level_is_moderate_then_a_moderate_level_sudoku_puzzle_should_be_generated(self):
        settings_manager = SettingsManager('mySettings.xml')
        settings_manager.load()
        game = Game()
        game.set_settings_manager(settings_manager)
        game.start_game_timer()
        cmd = GenerateGameCommand(None)
        cmd.set_game(game)
        cmd.execute()
        self.assertIsNotNone(game.initial_sudoku)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()