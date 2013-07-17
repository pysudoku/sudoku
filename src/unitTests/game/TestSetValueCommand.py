'''
Created on Jul 16, 2013

@author: Jimena Terceros
'''
import unittest
from sudoku.game.Game import Game
from sudoku.model.sudokutable import SudokuBoard
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.game.SetValueCommand import SetValueCommand


class TestSetValueCommand(unittest.TestCase):

    def setUp(self):
        self.valid_value = 5
        self.cell = "B3"
        self.clear_params = {}
        self.hint_parameters = {"row": 'B', "column": 3, "value": self.valid_value}
        self.invalid_number_of_params = {"row": 'B', "column": 3}
        self.invalid_row_params = {"roww": 'B', "column": 3, "value": self.valid_value}
        self.invalid_column_params = {"row": 'B', "columnw": 3, "value": self.valid_value}
        self.invalid_value_params = {"row": 'B', "column": 3, "wvalue": self.valid_value}
        self.none_row_params = {"row": None, "column": 3, "value": self.valid_value}
        self.none_column_params = {"row": 'B', "column": None, "value": self.valid_value}
        self.none_value_params = {"row": 'B', "column": 3, "value": None}

    def test_given_a_none_parameter_then_should_raise_an_exception(self):
        try:
            cmd = SetValueCommand(None)
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass

    def test_given_a_clear_parameter_then_should_raise_an_exception(self):
        try:
            cmd = SetValueCommand(self.clear_params)
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    
    def test_given_a_invalid_number_of_parameters_then_should_raise_an_exception(self):
        try:
            cmd = SetValueCommand(self.invalid_number_of_params)
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    
    def test_given_a_parameters_without_row_then_should_raise_an_exception(self):
        try:
            cmd = SetValueCommand(self.invalid_row_params)
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    
    def test_given_a_parameters_without_col_then_should_raise_an_exception(self):
        try:
            cmd = SetValueCommand(self.invalid_column_params)
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    
    def test_given_a_parameters_without_value_then_should_raise_an_exception(self):
        try:
            cmd = SetValueCommand(self.invalid_value_params)
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    
    def test_given_a_parameters_with_none_as_row_then_should_raise_an_exception(self):
        try:
            cmd = SetValueCommand(self.none_row_params)
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    
    def test_given_a_parameters_with_none_as_col_then_should_raise_an_exception(self):
        try:
            cmd = SetValueCommand(self.none_column_params)
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    
    def test_given_a_parameters_with_none_as_value_then_should_raise_an_exception(self):
        try:
            cmd = SetValueCommand(self.none_value_params)
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
        
    def test_given_a_valid_parameters_and_none_game_then_should_raise_an_exception(self):
        cmd = SetValueCommand(self.hint_parameters)
        
        try:
            cmd.execute()
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    
    def test_given_a_valid_parameters_and_none_user_sudoku_then_should_raise_an_exception(self):
        game = Game()
        cmd = SetValueCommand(self.hint_parameters)
        cmd.set_game(game)
        
        try:
            cmd.execute()
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    
    def test_given_a_valid_parameters_then_should_set_the_value_in_the_soduko_board(self):
        game = Game()
        game.user_sudoku = SudokuBoard(9)
        cmd = SetValueCommand(self.hint_parameters)
        cmd.set_game(game)
        cmd.execute()
        
        self.assertEqual(self.valid_value, game.user_sudoku.dic[self.cell].value)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()