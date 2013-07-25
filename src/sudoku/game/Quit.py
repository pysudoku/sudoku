'''
Created on Jul 16, 2013

@author: Ines Baina
'''
import os
import sys

from sudoku.game.SudokuCommand import SudokuCommand
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException

class QuitCommand(SudokuCommand):
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
        SudokuCommand.__init__(self, params)
    
    def execute(self):
        '''
        Execute the command to leave the application console
        '''
        os.system('cls')
        sys.exit(0)
        return True
        
    def validate(self):
        '''
        Validate number of parameters and the parameter of the command
        '''
        self.validate_needed_parameters()