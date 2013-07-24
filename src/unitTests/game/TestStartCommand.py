'''
Created on Jul 22, 2013

@author: Jimena Terceros
'''
import unittest
from sudoku.game.startCommand import StartCommand
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.model.sudokutable import SudokuBoard
from sudoku.game.Game import Game


class TestStartCommand(unittest.TestCase):


    def setUp(self):
        """
        self.user_sudoku = self.dic_with_data = {"A1":'1', "A2":'3', "A3":'2', 
                                                "B1":'2', "B2":'1', "B3":'0', 
                                                "C1":'0', "C2":'2', "C3":'0'}
        """

    def test_when_a_start_cmd_is_created_with_None_parameter_then_should_pass_validation(self):
        try:
            start_game_timer = StartCommand(None)
        except InvalidCmdParametersException:
            self.fail("The initializer should not raise an exception.")
            
    def test_when_a_start_cmd_is_created_with_clear_parameter_then_should_pass_validation(self):
        dict = {}
        try:
            start_game_timer = StartCommand(dict)
        except InvalidCmdParametersException:
            self.fail("The initializer should not raise an exception.")
            
    def test_when_a_start_cmd_is_created_with_no_clear_parameter_then_should_raise_an_exception(self):
        dict = {"param": '5'}
        try:
            start_game_timer = StartCommand(dict)
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
        
    def test_when_valid_parameters_and_none_game_and_none_user_sudoku_then_an_exception_should_be_trown(self):
        cmd = StartCommand(None)
        
        try:
            cmd.execute()
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
        
    def test_when_valid_parameters_none_game_and_there_is_a_valid_user_sudoku_then_an_exception_should_be_trown_saying_there_is_not_game(self):
        dict = {}
        cmd = StartCommand(dict)
        
        try:
            cmd.execute()
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
        
    def test_when_valid_parameters_and_valid_game_and_none_user_sudoku_then_should_an_exception_be_raised(self):
        cmd = StartCommand(None)
        game = Game()
        cmd.set_game(game)
        
        try:
            cmd.execute()
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    def test_when_valid_parameters_and_valid_game_and_a_valid_user_sudoku_then_should_the_game_be_started(self):
        user_sudoku = SudokuBoard(3)

        game = Game()
        game.started = False
        game.user_sudoku = user_sudoku
        
        cmd = StartCommand(None)
        cmd.set_game(game)
        cmd.execute()
        self.assertTrue(game.started)
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()