'''
Created on Jul 17, 2013

@author: Jimena Terceros
'''
from sudoku.game.SudokuCommand import SudokuCommand
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException

class HintCommand(SudokuCommand):
    '''
    HintCommand class is defining the command hint, to help to user when the game is started it is inheriting command of SudokuCommand class
    @var ROW_PARAM: the value for row. This variable is constant
    @var COLUMN_PARAM: the value for column. This variable is constant
    '''
    ROW_PARAM = "row"
    COLUMN_PARAM = "column"
    
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
        
        if self.game.user_sudoku.is_editable(self.readconfig_parameters[self.ROW_PARAM], self.readconfig_parameters[self.COLUMN_PARAM]):
            value = self.game.solved_sudoku.get_value(self.readconfig_parameters[self.ROW_PARAM], self.readconfig_parameters[self.COLUMN_PARAM])
            self.game.user_sudoku.set_value(self.readconfig_parameters[self.ROW_PARAM], self.readconfig_parameters[self.COLUMN_PARAM], value)
        
        
    def validate(self):
        '''
        Validate number of parameters and the parameter of the command
        '''
        self.validate_parameter_number(2)
        self.valida_param(self.ROW_PARAM)
        self.valida_param(self.COLUMN_PARAM)