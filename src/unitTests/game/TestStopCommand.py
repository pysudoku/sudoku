'''
Created on Jul 22, 2013

@author: Jimena Terceros
'''
import unittest
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.game.stopCommand import StopCommand
from sudoku.model.sudokutable import SudokuBoard
from sudoku.game.Game import Game
import time


class TestStopCommand(unittest.TestCase):


    def setUp(self):
        """
        self.user_sudoku = self.dic_with_data = {"A1":'1', "A2":'3', "A3":'2',
                                                "B1":'2', "B2":'1', "B3":'0',
                                                "C1":'0', "C2":'2', "C3":'0'}
        """

    def test_when_a_stop_cmd_is_created_with_None_parameter_then_should_pass_validation(self):
        try:
            stop_game_timer = StopCommand(None)
        except InvalidCmdParametersException:
            self.fail("The initializer should not raise an exception.")
            
    def test_when_a_stop_cmd_is_created_with_clear_parameter_then_should_pass_validation(self):
        dict = {}
        try:
            stop_game_timer = StopCommand(dict)
        except InvalidCmdParametersException:
            self.fail("The initializer should not raise an exception.")
            
    def test_when_a_stop_cmd_is_created_with_no_clear_parameter_then_should_raise_an_exception(self):
        dict = {"param": '5'}
        try:
            stop_game_timer = StopCommand(dict)
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    def test_when_valid_parameters_and_none_game_then_an_exception_should_be_trown(self):
        cmd = StopCommand(None)
        try:
            cmd.execute()
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
        
    def test_when_valid_parameters_and_valid_game_and_the_game_is_not_started_then_an_exception_should_be_trown_saying_the_game_is_not_starting(self):
        dict = {}
        game = Game()
        game.started = False
        cmd = StopCommand(dict)
        cmd.set_game(game)
        
        try:
            cmd.execute()
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
        
    def test_when_valid_parameters_and_valid_game_and_the_game_is_started_then_should_the_game_be_stopped(self):
        user_sudoku = SudokuBoard(3)

        game = Game()
        game.started = True
        game.startTime = time.clock()
        game.currentTime = 0
        game.user_sudoku = user_sudoku
        
        cmd = StopCommand(None)
        cmd.set_game(game)
        timee = cmd.execute()

        self.assertFalse(game.started)
        self.assertTrue(timee != 0.0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()