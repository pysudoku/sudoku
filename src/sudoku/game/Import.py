'''
Created on Jul 23, 2013

@author: Administrator
'''
from sudoku.game.SudokuCommand import SudokuCommand
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.reader.parser_factory import ParserFactory
from sudoku.model.sudokutable import SudokuBoard

class ImportCommand(SudokuCommand):
    '''
    Reads a Sudoku puzzle from a TXT, CSV or command line and loads the puzzle into the current game.
    '''

    INPUT_PARAM = "input"

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
        
        parser_factory = ParserFactory()
        parser = parser_factory.get_parser(self.readconfig_parameters[self.INPUT_PARAM])
        puzzle =  parser.parse_puzzle(self.readconfig_parameters[self.INPUT_PARAM])
        self.game.initial_sudoku = SudokuBoard()
        self.game.initial_sudoku.from_dictionary(puzzle, True)
        self.game.user_sudoku = SudokuBoard()
        self.game.user_sudoku.from_dictionary(puzzle, True)
        if self.game.is_started():
            self.game.stop_game_timer()
        
    def validate(self):
        '''
        Validate number of parameters and the parameter of the command
        '''
        self.validate_parameter_number(1)
        self.valida_param(self.INPUT_PARAM)