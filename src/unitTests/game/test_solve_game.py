'''
Created on Jul 22, 2013

@author: Administrator
'''
import unittest
import os
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.game.Game import Game
from sudoku.game.SolveGame import SolveGameCommand
from sudoku.model.sudokutable import SudokuBoard
from sudoku.settings.SettingsManager import SettingsManager
from sudoku.algorithm.recursive import Recursive

class TestSolveGameCommand(unittest.TestCase):

    def setUp(self):
        self.puzzle = {
            "A1":'.', "A2":'6', "A3":'7', "A4":'.', "A5":'4', "A6":'.', "A7":'.', "A8":'.', "A9":'2',
            "B1":'9', "B2":'.', "B3":'.', "B4":'7', "B5":'3', "B6":'.', "B7":'4', "B8":'5', "B9":'.',
            "C1":'4', "C2":'.', "C3":'5', "C4":'.', "C5":'.', "C6":'.', "C7":'.', "C8":'.', "C9":'.',
            "D1":'6', "D2":'.', "D3":'.', "D4":'.', "D5":'8', "D6":'.', "D7":'.', "D8":'.', "D9":'.',
            "E1":'.', "E2":'.', "E3":'.', "E4":'9', "E5":'.', "E6":'.', "E7":'3', "E8":'2', "E9":'.',
            "F1":'2', "F2":'8', "F3":'3', "F4":'5', "F5":'.', "F6":'.', "F7":'6', "F8":'4', "F9":'9',
            "G1":'.', "G2":'7', "G3":'.', "G4":'.', "G5":'.', "G6":'.', "G7":'.', "G8":'.', "G9":'3',
            "H1":'.', "H2":'.', "H3":'.', "H4":'6', "H5":'5', "H6":'7', "H7":'8', "H8":'.', "H9":'4',
            "I1":'.', "I2":'.', "I3":'6', "I4":'4', "I5":'2', "I6":'3', "I7":'5', "I8":'9', "I9":'7'
            }
        
        self.valid_params = {'algorithm': 'Backtracking'}
        self.too_many_params = {'algorithm': 'EASY', "ANOTHER_PARAM": "ANOTHER_PARAM_VALUE"}
        self.int_param = {'algorithm': 2}
        
    def tearDown(self):
        try:
            os.remove('mySettings.xml')
        except IOError:
            pass

    def test_an_InvalidCmdParametersException_should_be_raised_if_game_is_None(self):
        with self.assertRaises(InvalidCmdParametersException):
            cmd = SolveGameCommand(self.valid_params)
            cmd.execute()

    def test_an_InvalidCmdParametersException_should_be_raised_if_initial_sudoku_is_None(self):
        with self.assertRaises(InvalidCmdParametersException):
            game = Game()
            cmd = SolveGameCommand(self.valid_params)
            cmd.set_game(game)
            cmd.execute()

    def test_an_InvalidCmdParametersException_should_be_raised_if_too_many_parameters_are_given(self):
        with self.assertRaises(InvalidCmdParametersException):
            game = Game()
            cmd = SolveGameCommand(self.too_many_params)
            cmd.set_game(game)
            cmd.execute()

    def test_an_InvalidCmdParametersException_should_be_raised_if_parameter_has_int_value(self):
        with self.assertRaises(InvalidCmdParametersException):
            game = Game()
            game.initial_sudoku = SudokuBoard()
            cmd = SolveGameCommand(self.int_param)
            cmd.set_game(game)
            cmd.execute()

    def test_sudoku_puzzle_should_be_solved_when_no_solving_algorithm_is_specified(self):
        settings_manager = SettingsManager('mySettings.xml')
        settings_manager.load()
        game = Game()
        game.set_settings_manager(settings_manager)
        game.initial_sudoku = SudokuBoard()
        game.initial_sudoku.from_dictionary(self.puzzle, True)
        cmd = SolveGameCommand()
        cmd.set_game(game)
        cmd.execute()
        solving_algorithm = Recursive()
        expected_results = solving_algorithm.solve(self.puzzle)
        self.assertEqual(expected_results, game.solved_sudoku.to_dictionary())
        
    def test_sudoku_puzzle_should_be_solved_when_solving_algorithm_is_specified(self):
        settings_manager = SettingsManager('mySettings.xml')
        settings_manager.load()
        game = Game()
        game.set_settings_manager(settings_manager)
        game.initial_sudoku = SudokuBoard()
        game.initial_sudoku.from_dictionary(self.puzzle, True)
        game.start_game_timer()
        cmd = SolveGameCommand(self.valid_params)
        cmd.set_game(game)
        cmd.execute()
        solving_algorithm = Recursive()
        expected_results = solving_algorithm.solve(self.puzzle)
        self.assertEqual(expected_results, game.solved_sudoku.to_dictionary())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()