'''
Created on Jul 17, 2013

@author: Jimena Terceros
'''
import unittest
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.game.HintCommand import HintCommand
from sudoku.game.Game import Game
from sudoku.model.sudokutable import SudokuBoard

class TestHintCommand(unittest.TestCase):

    def setUp(self):
        self.clear_params = {}
        self.hint_parameters = {"row": 'B', "column": 3}
        self.invalid_number_of_params = {"row": 'B'}
        self.invalid_row_params = {"rown": 'B', "column": 3}
        self.invalid_column_params = {"row": 'B', "cmolumn": 3}
        self.none_row_params = {"row": None, "column": 3}
        self.none_column_params = {"row": 'B', "column": None}
        
        self.cell = "B3"
        self.solved_sudoku = self.dic_with_data = {"A1":1, "A2":3, "A3":2, 
                                                   "B1":2, "B2":1, "B3":3, 
                                                   "C1":3, "C2":2, "C3":1}
        self.sudoku = self.dic_with_data =      {"A1":0, "A2":0, "A3":2, 
                                                 "B1":2, "B2":0, "B3":0, 
                                                 "C1":0, "C2":2, "C3":0}
        self.user_sudoku = self.dic_with_data = {"A1":1, "A2":3, "A3":2, 
                                                 "B1":2, "B2":1, "B3":0, 
                                                 "C1":0, "C2":2, "C3":0}

    
    def test_given_a_none_parameter_then_should_raise_an_exception(self):
        try:
            cmd = HintCommand(None)
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    
    def test_given_a_clear_parameter_then_should_raise_an_exception(self):
        try:
            cmd = HintCommand(self.clear_params)
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    
    def test_given_a_invalid_number_of_parameters_then_should_raise_an_exception(self):
        try:
            cmd = HintCommand(self.invalid_number_of_params)
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    
    def test_given_a_parameters_without_row_then_should_raise_an_exception(self):
        try:
            cmd = HintCommand(self.invalid_row_params)
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    
    def test_given_a_parameters_without_col_then_should_raise_an_exception(self):
        try:
            cmd = HintCommand(self.invalid_column_params)
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    
    def test_given_a_parameters_with_none_as_row_then_should_raise_an_exception(self):
        try:
            cmd = HintCommand(self.none_row_params)
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    
    def test_given_a_parameters_with_none_as_col_then_should_raise_an_exception(self):
        try:
            cmd = HintCommand(self.none_column_params)
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    
    def test_given_a_valid_parameters_and_none_game_then_should_raise_an_exception(self):
        cmd = HintCommand(self.hint_parameters)
        
        try:
            cmd.execute()
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    
    def test_given_a_valid_parameters_and_none_user_sudoku_then_should_raise_an_exception(self):
        game = Game()
        cmd = HintCommand(self.hint_parameters)
        cmd.set_game(game)
        
        try:
            cmd.execute()
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
        
    def test_given_a_valid_parameters_then_should_set_the_hint_value_in_the_soduko_board(self):
        initial_sudoku = SudokuBoard(3)
        user_sudoku = SudokuBoard(3)
        solved_sudoku = SudokuBoard(3)
        
        initial_sudoku.from_dictionary(self.solved_sudoku)
        user_sudoku.from_dictionary(self.user_sudoku)
        solved_sudoku.from_dictionary(self.solved_sudoku)
        
        game = Game()
        game.initial_sudoku = initial_sudoku
        game.user_sudoku = user_sudoku
        game.solved_sudoku = solved_sudoku
        
        cmd = HintCommand(self.hint_parameters)
        cmd.set_game(game)
        
        cmd.execute()
        
        self.assertEqual(game.solved_sudoku.dic[self.cell].value, game.user_sudoku.dic[self.cell].value)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()