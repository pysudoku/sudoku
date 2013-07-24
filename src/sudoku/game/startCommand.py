'''
Created on Jul 18, 2013

@author: Jimena Terceros
'''
from sudoku.game.SudokuCommand import SudokuCommand
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException

class StartCommand(SudokuCommand):
    '''
    This command is defined to start_game_timer the game. It is inheriting of SudokuCommand class
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
        elif self.game.user_sudoku == None:
            raise InvalidCmdParametersException("The Sudoku was not loaded.")
        
        self.game.start_game_timer()
        
    def validate(self):
        '''
        Validate number of parameters and the parameter of the command
        '''
        self.validate_needed_parameters()