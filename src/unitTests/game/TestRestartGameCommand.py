'''
Created on Jul 17, 2013

@author: Jimena Terceros
'''
import unittest
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.game.Game import Game
from sudoku.game.RestartGameCommand import RestartGameCommand
from sudoku.model.sudokutable import SudokuBoard


class TestRestartGameCommand(unittest.TestCase):

    def setUp(self):
        self.solved_sudoku = self.dic_with_data = {"A1":1, "A2":3, "A3":2, 
                                                   "B1":2, "B2":1, "B3":3, 
                                                   "C1":3, "C2":2, "C3":1}
        self.sudoku = self.dic_with_data =      {"A1":0, "A2":0, "A3":2, 
                                                 "B1":2, "B2":0, "B3":0, 
                                                 "C1":0, "C2":2, "C3":0}
        self.user_sudoku = self.dic_with_data = {"A1":1, "A2":3, "A3":2, 
                                                 "B1":2, "B2":1, "B3":3, 
                                                 "C1":0, "C2":2, "C3":0}

    def test_when_an_restart_cmd_is_created_with_None_parameter_then_should_pass_validation(self):
        try:
            restart = RestartGameCommand(None)
        except InvalidCmdParametersException:
            self.fail("The initializer should not raise an exception.")
            
    def test_when_an_about_cmd_is_created_with_clear_parameter_then_should_pass_validation(self):
        dict = {}
        try:
            restart = RestartGameCommand(dict)
        except InvalidCmdParametersException:
            self.fail("The initializer should not raise an exception.")
            
    def test_when_an_about_cmd_is_created_with_no_clear_parameter_then_should_raise_an_exception(self):
        dict = {"param": 5}
        try:
            restart = RestartGameCommand(dict)
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
            
    def test_given_a_valid_parameters_and_none_game_then_should_raise_an_exception(self):
        cmd = RestartGameCommand(None)
        
        try:
            cmd.execute()
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    
    def test_given_a_valid_parameters_and_none_user_sudoku_then_should_raise_an_exception(self):
        game = Game()
        cmd = RestartGameCommand(None)
        cmd.set_game(game)
        
        try:
            cmd.execute()
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
        
    def test_given_a_valid_parameters_and_none_initial_sudoku_then_should_raise_an_exception(self):
        game = Game()
        game.user_sudoku = SudokuBoard(3)
        cmd = RestartGameCommand(None)
        cmd.set_game(game)
        
        try:
            cmd.execute()
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
            
    def test_when_restart_game_is_executed_then_the_user_table_should_be_restarted_properly(self):
        sudoku = SudokuBoard(3)
        user_sudoku = SudokuBoard(3)
        
        sudoku.from_dictionary(self.solved_sudoku)
        user_sudoku.from_dictionary(self.user_sudoku)
        
        game = Game()
        game.initial_sudoku = sudoku
        game.user_sudoku = user_sudoku
        
        cmd = RestartGameCommand(None)
        cmd.set_game(game)
        cmd.execute()
        
        self.assertDictEqual(game.initial_sudoku.to_dictionary(), game.user_sudoku.to_dictionary())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()