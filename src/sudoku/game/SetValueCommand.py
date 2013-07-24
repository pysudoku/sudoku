'''
Created on Jul 17, 2013

@author: Jimena Terceros
'''
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.game.SudokuCommand import SudokuCommand

class SetValueCommand(SudokuCommand):
    '''
    SetValueCommand class is defining the command setValue
    @var ROW_PARAM: the value for row. This variable is constant
    @var COLUMN_PARAM: the value for column. This variable is constant
    @var VALUE_PARAM: the value for value. This variable is constant
    '''
    ROW_PARAM = "row"
    COLUMN_PARAM = "column"
    VALUE_PARAM = "value"

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
        if not self.game.is_started():
            raise InvalidCmdParametersException("It is not possible to set a value if the game is not started.")
        
        self.game.user_sudoku.set_value(self.readconfig_parameters[self.ROW_PARAM], int( self.readconfig_parameters[self.COLUMN_PARAM]), self.readconfig_parameters[self.VALUE_PARAM])
        
    def validate(self):
        '''
        Validate number of parameters and the parameter of the command
        '''
        self.validate_parameter_number(3)
        self.valida_param(self.ROW_PARAM)
        self.valida_param(self.COLUMN_PARAM)
        self.valida_param(self.VALUE_PARAM)
    