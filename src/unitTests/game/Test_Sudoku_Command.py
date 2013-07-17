'''
Created on Jul 16, 2013

@author: Jimena Terceros
'''
import unittest
from sudoku.game.Game import Game
from sudoku.game.SudokuCommand import SudokuCommand


class TestSudokuCommand(unittest.TestCase):

    def setUp(self):
        self.readconfig_parameters = {"param1":5, "param2": "test"}


    def test_when_a_command_is_created_then_should_be_set_the_params(self):
        cmd = SudokuCommand(self.readconfig_parameters)
        self.assertDictEqual(self.readconfig_parameters, cmd.readconfig_parameters)
        
    def test_when_a_command_is_created_then_should_be_set_the_game_as_none(self):
        cmd = SudokuCommand(self.readconfig_parameters)
        self.assertIsNone(cmd.game)
        
    def test_when_a_game_is_given_then_should_be_set_the_game(self):
        cmd = SudokuCommand(self.readconfig_parameters)
        game = Game()
        cmd.set_game(game)
        self.assertEqual(game, cmd.game)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'TestSudokuCommand.testName']
    unittest.main()