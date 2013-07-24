'''
Created on Jul 18, 2013

@author: Jimena Terceros
'''
from sudoku.game.SudokuCommand import SudokuCommand
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException

class PauseCommand(SudokuCommand):
    '''
    This command is defined to pause_game_timer the game. It is inheriting of SudokuCommand class
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        SudokuCommand.__init__(self, params)
        
    def execute(self):
        '''
        execute the command taking account the parameters of the command
        '''
        if self.game == None:
            raise InvalidCmdParametersException("The command needs a game.")
        if not self.game.is_started():
            raise InvalidCmdParametersException("It is not possible to pause a non started game.")
        
        self.game.pause_game_timer()
        return "Time> " + str(self.game.get_current_time()) + " seg."
        
    def validate(self):
        '''
        Validate number of parameters and the parameter of the command
        '''
        self.validate_needed_parameters()