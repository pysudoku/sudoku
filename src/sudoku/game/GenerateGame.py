'''
Created on Jul 17, 2013

@author: Administrator
'''
from sudoku.game.SudokuCommand import SudokuCommand
from sudoku.model.sudokutable import SudokuBoard
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException

class GenerateGameCommand(SudokuCommand):
    '''
    classdocs
    '''
    LEVEL_NAME_PARAM = "level"

    def __init__(self, params):
        '''
        Constructor
        '''
        if params is None:
            params = {'level': 'DEFAULT_LEVEL_NAME'}
        
        SudokuCommand.__init__(self, params)
        
    def execute(self):
        '''
        Generates a Sudoku puzzle and sets up the SudokuBoard structure so a user can play.
        If game level is None, the game is generated using the default level specified in the Settings object.
        '''
        if self.game == None:
            raise InvalidCmdParametersException("The command needs a game.")
        if not (isinstance(self.readconfig_parameters[self.LEVEL_NAME_PARAM], str)):
            raise InvalidCmdParametersException("The command needs a level.")
        
        level = self.game.settings_manager.settings.getLevel(self.readconfig_parameters[self.LEVEL_NAME_PARAM])
        if level is None:
            level = self.game.settings_manager.settings.getLevel(self.game.settings_manager.settings.DEFAULT_LEVEL_NAME)

        puzzle = self.game.game_generator.generate_puzzle(level)
        self.game.initial_sudoku = SudokuBoard() 
        self.game.initial_sudoku.from_dictionary(puzzle)
        self.game.user_sudoku = SudokuBoard()
        self.game.user_sudoku.from_dictionary(puzzle)
    
    def validate(self):
        '''
        Validates that one parameter is received and that parameter must be a LEVEL_NAME_PARAM parameter.
        ''' 
        self.validate_parameter_number(1)
        self.valida_param(self.LEVEL_NAME_PARAM)
        
        