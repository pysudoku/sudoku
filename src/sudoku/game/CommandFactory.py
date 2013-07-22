'''
Created on Jul 17, 2013

@author: Jimena Terceros
'''
from sudoku.game.About import About
from sudoku.game.RestartGameCommand import RestartGameCommand
from sudoku.game.ReadConfigurationCommand import ReadConfigurationCommand
from sudoku.game.HintCommand import HintCommand
from sudoku.game.SetValueCommand import SetValueCommand
from sudoku.game.PrintCommand import PrintBoardCommand
from sudoku.game.Quit import QuitCommand
from sudoku.game.GenerateGame import GenerateGameCommand

class CommandFactory(object):
    '''
    CommandFactory class create commands
    '''
    ABOUT_COMMAND = "about"
    RESTART_GAME_COMMAND = "restart"
    READ_CONFIGURATION_COMMAND = "readConfiguration"
    HINT_COMMAND = "hint"
    SET_VALUE_COMMAND = "setValue"
    PRINT_COMMAND = "print"
    QUIT_COMMAND = "quit"
    GENERATE_COMMAND = "generate"

    def __init__(self, game):
        '''
        Constructor
        @param game: The value for game attribute
        '''
        self.game = game
    
    def getCommand(self, cmdName, params):
        '''
        @return: return the command
        '''
        if self.ABOUT_COMMAND == cmdName:
            cmd = About(params)
        elif self.RESTART_GAME_COMMAND == cmdName:
            cmd = RestartGameCommand(params)
        elif self.READ_CONFIGURATION_COMMAND == cmdName:
            cmd = ReadConfigurationCommand(params)
        elif self.HINT_COMMAND == cmdName:
            cmd = HintCommand(params)
        elif self.SET_VALUE_COMMAND == cmdName:
            cmd = SetValueCommand(params)
        elif self.PRINT_COMMAND == cmdName:
            cmd = PrintBoardCommand(params)
        elif self.QUIT_COMMAND == cmdName:
            cmd = QuitCommand(params)
        elif self.GENERATE_COMMAND == cmdName:
            cmd = GenerateGameCommand(params)
        
        cmd.set_game(self.game)
        return cmd