'''
Created on Jul 17, 2013

@author: Jimena Terceros
'''
import unittest
from sudoku.game.CommandFactory import CommandFactory
from sudoku.game.Game import Game
from sudoku.game.About import About
from sudoku.game.RestartGameCommand import RestartGameCommand
from sudoku.game.ReadConfigurationCommand import ReadConfigurationCommand
from sudoku.game.HintCommand import HintCommand
from sudoku.game.SetValueCommand import SetValueCommand


class TestCommandFactory(unittest.TestCase):

    def setUp(self):
        self.readconfig_parameters = {'fileName':"test.xml"}
        self.hint_parameters = {"row": 'B', "column": 3}
        self.set_value_parameters = {"row": 'B', "column": 3, "value": 5}

    def test_given_cmd_about_then_should_get_the_about_cmd_properly(self):
        game = Game()
        factory = CommandFactory(game)
        cmd = factory.getCommand("about", {})
        
        self.assertTrue(isinstance(cmd, About))

    def test_given_cmd_restart_then_should_get_the_restart_cmd_properly(self):
        game = Game()
        factory = CommandFactory(game)
        cmd = factory.getCommand("restart", {})
        
        self.assertTrue(isinstance(cmd, RestartGameCommand))
        
    def test_given_cmd_readconfigration_then_should_get_the_readconfiguration_cmd_properly(self):
        game = Game()
        factory = CommandFactory(game)
        cmd = factory.getCommand("readConfiguration", self.readconfig_parameters)
        
        self.assertTrue(isinstance(cmd, ReadConfigurationCommand))
        
    def test_given_cmd_hint_then_should_get_the_hint_cmd_properly(self):
        game = Game()
        factory = CommandFactory(game)
        cmd = factory.getCommand("hint", self.hint_parameters)
        
        self.assertTrue(isinstance(cmd, HintCommand))
        
    def test_given_cmd_setValue_then_should_get_the_setValue_cmd_properly(self):
        game = Game()
        factory = CommandFactory(game)
        cmd = factory.getCommand("setValue", self.set_value_parameters)
        
        self.assertTrue(isinstance(cmd, SetValueCommand))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()