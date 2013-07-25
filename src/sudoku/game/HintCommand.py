'''
Created on Jul 17, 2013

@author: Jimena Terceros
'''
from sudoku.game.SudokuCommand import SudokuCommand
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.algorithm.AlgorithmFactory import AlgorithmFactory
from sudoku.model.sudokutable import SudokuBoard


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
        if not self.game.is_started():
            raise InvalidCmdParametersException("It is not possible to hint if the game is not started.")
        
        if self.game.solved_sudoku is None:
            algorithm_factory = AlgorithmFactory(self.game.settings_manager.settings.getAlgorithmName())
            solving_algorithm = algorithm_factory.getAlgorithm()        
            solution = solving_algorithm.solve(self.game.initial_sudoku.to_dictionary())
            self.game.solved_sudoku = SudokuBoard() 
            self.game.solved_sudoku.from_dictionary(solution, True)            
                            
        if self.game.user_sudoku.is_editable(self.readconfig_parameters[self.ROW_PARAM], int(self.readconfig_parameters[self.COLUMN_PARAM])):
            value = self.game.solved_sudoku.get_value(self.readconfig_parameters[self.ROW_PARAM], int(self.readconfig_parameters[self.COLUMN_PARAM]))
            self.game.user_sudoku.set_value(self.readconfig_parameters[self.ROW_PARAM], int(self.readconfig_parameters[self.COLUMN_PARAM]), value)
        
        
    def validate(self):
        '''
        Validate number of parameters and the parameter of the command
        '''
        self.validate_parameter_number(2)
        self.valida_param(self.ROW_PARAM)
        self.valida_param(self.COLUMN_PARAM)
