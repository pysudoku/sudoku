'''
Created on Jul 17, 2013

@author: Jimena Terceros
'''
from sudoku.game.SudokuCommand import SudokuCommand
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.model.sudokutable import SudokuBoard

class RestartGameCommand(SudokuCommand):
    '''
    RestartGameCommand class is defining the command restart
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
        elif self.game.initial_sudoku == None:
            raise InvalidCmdParametersException("The Sudoku was not loaded.")
        
        self.game.user_sudoku=SudokuBoard(self.game.user_sudoku.size)  
        self.game.user_sudoku.from_dictionary(self.game.initial_sudoku.to_dictionary(),True)
        
    def validate(self):
        '''
        Validate number of parameters and the parameter of the command
        '''
        if self.readconfig_parameters != None and len(self.readconfig_parameters) != 0:
            raise InvalidCmdParametersException("The command no need parameters.")
