'''
Created on Jul 16, 2013

@author: Ines Baina
'''
import os
import sys
import unittest

from sudoku.console.console import Console
from sudoku.game.GenerateGame import GenerateGameCommand
from sudoku.game.RestartGameCommand import RestartGameCommand
from sudoku.game.SetValueCommand import SetValueCommand
from sudoku.game.HintCommand import HintCommand
from sudoku.game.About import About
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.game.Game import Game
from sudoku.game.Quit import QuitCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        pass
    
    

    def test_to_verify_if_command_is_not_parsed_correct_an_exception_is_raised(self): 
        try:
            self.command= "generate Incorrect"
            console=Console()
            result = console.parse_command(self.command)
            self.assertTrue(True)
        except Exception as e:
            self.fail("Exception has been raised",e)
            
    def test_to_verify_if_parameter_is_not_parsed_correct_with_equal_character_an_exception_is_raised(self): 
        
        try:
            self.command= "generate /Incorrect"
            console=Console()
            result = console.parse_command(self.command)
            self.assertTrue(True)
        except Exception as e:
            self.fail("Exception has been raised",e)
        
            
    def test_to_verify_if_parameter_is_parsed_correct_if_it_comes_with_special_charater_slash_(self): 
        
        self.parameters= "/level=EASY"
        console=Console()
        params={'level':'EASY'}
        result = console.parse_parameter(self.parameters,params)
        self.assertEqual(params,result)
        
    def test_to_verify_if_parameter_is_parsed_correct_if_it_comes_with_special_charater_slash_and_equal(self): 
        
        self.parameters= "/level=HARD"
        console=Console()
        params={'level':'HARD'}
        result = console.parse_parameter(self.parameters,params)
        self.assertEqual(params,result)    
   
    def test_to_verify_if_generate_command_with_params_is_a_generate_command_object(self):
        self.command= "generate /level=EASY"
        console=Console()
        
        self.assertIsInstance(console.parse_command(self.command), GenerateGameCommand,"Is not instance")
        
    def test_to_verify_if_restart_command_with_params_is_a_restart_command_object(self):
        self.command= "restart"
        console=Console()
          
        self.assertIsInstance(console.parse_command(self.command), RestartGameCommand,"Is not instance")
        
    def test_to_verify_if_setValue_command_with_params_is_a_setValue_command_object(self):
        self.command= "setValue /row=A /column=2 /value=3"
        console=Console()
          
        self.assertIsInstance(console.parse_command(self.command), SetValueCommand,"Is not instance")
        
    def test_to_verify_if_Hint_command_with_params_is_a_Hint_command_object(self):
        self.command= "hint /row=A /column=2"
        console=Console()
          
        self.assertIsInstance(console.parse_command(self.command), HintCommand,"Is not instance")
        
    def test_to_verify_that_parse_command_raise_an_exception_if_command_is_not_in_Commands_application(self):   
        try:
            self.command= "Generate"
            console = Console()
            result = console.parse_command(self.command)
            self.fail("Expected InvalidCmdParametersException was not raised.")
        except InvalidCmdParametersException:
            pass
        
    def test_to_verify_if_execute_command_function_execute_a_command(self):
        console = Console()
        cmd = About(None)
        result = console.execute_command(cmd)     
        self.assertEqual(None, None)
        
    def test_to_verify_if_execute_command_function_does_not_execute_a_command(self):
        console = Console()
        cmd = None
        result = console.execute_command(cmd) 
        self.assertEqual(None, result)
    
   
       
if __name__ == '__main__':

    unittest.main()