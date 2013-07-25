'''
Created on Jul 19, 2013

@author: Ines Baina
'''
import unittest
import sys
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.game.Quit  import QuitCommand



class TestQuit(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_when_a_quit_cmd_is_executed_user_leave_the_application(self):
        pass
            
    def test_when_an_quit_cmd_is_created_with_None_parameter_then_should_pass_validation(self):
        try:
            result = QuitCommand(None)
        except InvalidCmdParametersException:
            self.fail("The initializer should not raise an exception.")  
            
  
if __name__ == "__main__":
    unittest.main()