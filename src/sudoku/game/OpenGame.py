'''
Created on Jul 23, 2013

@author: Administrator
'''
import os
from sudoku.game.SudokuCommand import SudokuCommand
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.reader.game_reader import SudokuGameReader

class OpenGameCommand(SudokuCommand):
    '''
    Opens a Sudoku game file and loads it to the current game
    '''

    INPUT_PARAM = "file"
    
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
        
        game_reader = SudokuGameReader()
        working_directory = self.game.settings_manager.settings.getPath()        
        if working_directory == '':
            working_directory = os.getcwd()        
        
        file_name = self.readconfig_parameters[self.INPUT_PARAM]
        if os.path.dirname(file_name) == '':
            file_name = working_directory + os.sep + file_name

        read_game = game_reader.read_game(file_name)
        self.game.copy(read_game)
        if self.game.is_started():
            self.game.stop_game_timer()

    def validate(self):
        '''
        Validate number of parameters and the parameter of the command
        '''
        self.validate_parameter_number(1)
        self.valida_param(self.INPUT_PARAM)
