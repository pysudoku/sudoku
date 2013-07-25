'''
Created on Jul 19, 2013

@author: Ines Baina
'''
import unittest
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.game.SudokuCommand import SudokuCommand
from sudoku.model.sudokutable import SudokuBoard
from sudoku.game.PrintCommand import PrintBoardCommand
from sudoku.game.Game import Game


class TestPrintBoardCommand(unittest.TestCase):

    def setUp(self):
        pass
    def test_if_print_has_not_raised_exceptionin_console(self):
        dict = {}
        
        
        try:
            print_command = PrintBoardCommand(dict)
            result = print_command.validate()
            self.assertTrue(True)
        except InvalidCmdParametersException:
            self.fail("Exception has been raised")
            
    def test_if_execute_printcommand_doesnt_raise_exception_when_a_good_formater_dictionary_is_given(self):
        dict = {}
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
        
        try:
            game=Game()
            game.user_sudoku= SudokuBoard()
            game.user_sudoku.from_dictionary(puzzle,True)
            
            print_command = PrintBoardCommand(dict)
            print_command.game=game
            
            #print_command.game.user_sudoku.from_dictionary(puzzle)
            result = print_command.execute()
            self.assertTrue(True)
        except Exception as e:
            self.fail("Exception has been raised",e)
            
    def test_when_an_print_cmd_is_created_with_None_parameter_then_should_pass_validation(self):
        try:
            restart = PrintBoardCommand(None)
        except InvalidCmdParametersException:
            self.fail("The initializer should not raise an exception.")
            
    def test_given_a_valid_parameters_and_none_game_then_should_raise_an_exception(self):
        cmd = PrintBoardCommand(None)
        
        try:
            cmd.execute()
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
    
    def test_given_a_valid_parameters_and_none_user_sudoku_then_should_raise_an_exception(self):
        game = Game()
        game.started = True
        cmd = PrintBoardCommand(None)
        cmd.set_game(game)
        
        try:
            cmd.execute()
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()