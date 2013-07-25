'''
Created on Jul 19, 2013

@author: Ariel Mattos
'''
from sudoku.game.SudokuCommand import SudokuCommand
from sudoku.model.sudokutable import SudokuBoard
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.algorithm.AlgorithmFactory import AlgorithmFactory

class SolveGameCommand(SudokuCommand):
    '''
    Solves the Sudoku puzzle loaded in the user SudokuBoard object and fills it with the solution 
    '''
    ALGORITHM_PARAM = "algorithm"

    def __init__(self, params=None):
        '''
        Constructor
        '''
        if params is None:
            params = {'algorithm': 'DEFAULT_ALGORITHM_NAME'}
        
        SudokuCommand.__init__(self, params)

    def execute(self):
        '''
        Solves a the Sudoku puzzle loaded in 'game.initial_sudoku' and loads the results
        in the 'game.solved_sudoku' SudokuBoard object.
        If the solving algorithm is None, the puzzle is solved using the default algorithm
        specified in the Settings object.
        '''
        if self.game == None:
            raise InvalidCmdParametersException("The command needs a game.")
        if self.game.initial_sudoku == None:
            raise InvalidCmdParametersException("The Sudoku was not loaded.")
        if not (isinstance(self.readconfig_parameters[self.ALGORITHM_PARAM], str)):
            raise InvalidCmdParametersException("The command needs an algorithm.")
        
        algorithm_factory = AlgorithmFactory(self.readconfig_parameters[self.ALGORITHM_PARAM])
        if (algorithm_factory.getAlgorithm()) is None:
            algorithm_factory.settings = self.game.settings_manager.settings.getAlgorithmName()
        
        solving_algorithm = algorithm_factory.getAlgorithm()
        
        solution = solving_algorithm.solve(self.game.initial_sudoku.to_dictionary())
        self.game.solved_sudoku = SudokuBoard() 
        self.game.solved_sudoku.from_dictionary(solution, True)
        self.game.user_sudoku = SudokuBoard() 
        self.game.user_sudoku.from_dictionary(solution, True)
        if self.game.is_started():
            self.game.stop_game_timer()
    
    def validate(self):
        '''
        Validates that one parameter is received and that parameter must be an ALGORITHM_PARAM parameter.
        ''' 
        self.validate_parameter_number(1)
        self.valida_param(self.ALGORITHM_PARAM)