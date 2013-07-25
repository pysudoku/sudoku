'''
Created on Jul 17, 2013

@author: Jimena Terceros
'''
import unittest
import os
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.game.HintCommand import HintCommand
from sudoku.game.Game import Game
from sudoku.model.sudokutable import SudokuBoard
from sudoku.settings.SettingsManager import SettingsManager

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
        self.solved_sudoku = self.dic_with_data = {"A1":'1', "A2":'3', "A3":'2', 
                                                   "B1":'2', "B2":'1', "B3":'3', 
                                                   "C1":'3', "C2":'2', "C3":'1'}
        self.sudoku = self.dic_with_data =      {"A1":'0', "A2":'0', "A3":'2', 
                                                 "B1":'2', "B2":'0', "B3":'0', 
                                                 "C1":'0', "C2":'2', "C3":'0'}
        self.user_sudoku = self.dic_with_data = {"A1":'1', "A2":'3', "A3":'2', 
                                                 "B1":'2', "B2":'1', "B3":'0', 
                                                 "C1":'0', "C2":'2', "C3":'0'}

    def tearDown(self):
        try:
            os.remove('settings.xml')
        except IOError:
            pass
    
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
        settings_manager = SettingsManager('mySettings.xml')
        settings_manager.load()
        game = Game()
        game.set_settings_manager(settings_manager)
        game.started = True
        cmd = HintCommand(self.hint_parameters)
        cmd.set_game(game)
        
        try:
            cmd.execute()
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
        
    def test_when_valid_parameters_and_valid_game_and_the_game_is_not_started_then_an_exception_should_be_trown_saying_the_game_is_not_starting(self):
        cmd = HintCommand(self.hint_parameters)
        
        game = Game()
        game.user_sudoku = SudokuBoard(3)
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
        game.started = True
        game.initial_sudoku = initial_sudoku
        game.user_sudoku = user_sudoku
        game.solved_sudoku = solved_sudoku
        
        cmd = HintCommand(self.hint_parameters)
        cmd.set_game(game)
        
        cmd.execute()
        
        self.assertEqual(game.solved_sudoku.dic[self.cell].value, game.user_sudoku.dic[self.cell].value)

    def test_solution_is_load_in_solved_sudoku_when_solved_sudoku_is_None(self):
        puzzle = {
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
        
        settings_manager = SettingsManager('settings.xml')
        settings_manager.load()
        game = Game()
        game.started = True
        game.set_settings_manager(settings_manager)
        game.initial_sudoku = SudokuBoard()
        game.initial_sudoku.from_dictionary(puzzle, True)
        game.user_sudoku = SudokuBoard()
        game.user_sudoku.from_dictionary(puzzle, True)
        
        cmd = HintCommand(self.hint_parameters)
        cmd.set_game(game)

        cmd.execute()
        
        self.assertEqual(game.solved_sudoku.dic[self.cell].value, game.user_sudoku.dic[self.cell].value)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()