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
from sudoku.game.startCommand import StartCommand
from sudoku.game.stopCommand import StopCommand
from sudoku.game.pauseCommand import PauseCommand
from sudoku.game.SolveGame import SolveGameCommand
from sudoku.game.Import import ImportCommand
from sudoku.game.Export import ExportCommand
from sudoku.game.SaveGame import SaveGameCommand
from sudoku.game.OpenGame import OpenGameCommand
from sudoku.game.Quit import QuitCommand
from sudoku.game import PrintCommand
from sudoku.game.PrintCommand import PrintBoardCommand



class TestCommandFactory(unittest.TestCase):

    def setUp(self):
        self.readconfig_parameters = {'fileName':"test.xml"}
        self.hint_parameters = {"row": 'B', "column": 3}
        self.set_value_parameters = {"row": 'B', "column": 3, "value": 5}
        self.import_parameter = {"input":""}
        self.export_parameter = {"output":""}
        self.open_game_parameter = {"file":""}
        self.save_game_parameter = {"file":""}

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
        cmd = factory.getCommand("readConfig", self.readconfig_parameters)
        
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
    
    def test_given_cmd_start_then_should_get_the_start_cmd_properly(self):
        game = Game()
        factory = CommandFactory(game)
        cmd = factory.getCommand("start", None)
        
        self.assertTrue(isinstance(cmd, StartCommand))
        
    def test_given_cmd_stop_then_should_get_the_stop_cmd_properly(self):
        game = Game()
        factory = CommandFactory(game)
        cmd = factory.getCommand("stop", None)
        
        self.assertTrue(isinstance(cmd, StopCommand))
        
    def test_given_cmd_pause_then_should_get_the_pause_cmd_properly(self):
        game = Game()
        factory = CommandFactory(game)
        cmd = factory.getCommand("pause", None)
        
        self.assertTrue(isinstance(cmd, PauseCommand))
    def test_given_cmd_quit_then_should_get_the_quit_cmd_properly(self):
        game = Game()
        factory = CommandFactory(game)
        cmd = factory.getCommand("quit", None)
        
        self.assertTrue(isinstance(cmd, QuitCommand))
    def test_given_cmd_print_then_should_get_the_print_cmd_properly(self):
        game = Game()
        factory = CommandFactory(game)
        cmd = factory.getCommand("print", None)
        
        self.assertTrue(isinstance(cmd, PrintBoardCommand))
        
    def test_a_SolveGameCommand_instance_should_be_returned_when_the_command_is_requested_to_the_factory(self):
        game = Game()
        factory = CommandFactory(game)
        cmd = factory.getCommand("solve", None)
        
        self.assertTrue(isinstance(cmd, SolveGameCommand))

    def test_an_ImportCommand_instance_should_be_returned_when_the_command_is_requested_to_the_factory(self):
        game = Game()
        factory = CommandFactory(game)
        cmd = factory.getCommand("import", self.import_parameter)
        
        self.assertTrue(isinstance(cmd, ImportCommand))

    def test_an_ExportCommand_instance_should_be_returned_when_the_command_is_requested_to_the_factory(self):
        game = Game()
        factory = CommandFactory(game)
        cmd = factory.getCommand("export", self.export_parameter)
        
        self.assertTrue(isinstance(cmd, ExportCommand))

    def test_a_SaveCommand_instance_should_be_returned_when_the_command_is_requested_to_the_factory(self):
        game = Game()
        factory = CommandFactory(game)
        cmd = factory.getCommand("save", self.save_game_parameter)
        
        self.assertTrue(isinstance(cmd, SaveGameCommand))

    def test_an_OpenCommand_instance_should_be_returned_when_the_command_is_requested_to_the_factory(self):
        game = Game()
        factory = CommandFactory(game)
        cmd = factory.getCommand("open", self.open_game_parameter)
        
        self.assertTrue(isinstance(cmd, OpenGameCommand))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()