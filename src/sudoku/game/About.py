'''
Created on Jul 16, 2013

@author: Jimena Terceros
'''
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.game.SudokuCommand import SudokuCommand

class About(SudokuCommand):
    '''
    About class is defining the command about, showing information of pysudoku it is inheriting command of SudokuCommand class
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        SudokuCommand.__init__(self, params)
        
    def execute(self):
        '''
        @return: command
        '''
        about = ""
        about = about + "------------------------------------\n"
        about = about + "---------- About PySudoku ----------\n"
        about = about + "------------------------------------\n"
        about = about + "  Fundation Jala\n"
        about = about + "  Developed By:\n"
        about = about + "        Jimena Terceros\n"
        about = about + "        Ines Baina\n"
        about = about + "        Ariel Mattos\n"
        about = about + "------------------------------------\n"
        
        return about
        
    def validate(self):
        '''
        Validate number of parameters that the command has
        '''
        if self.readconfig_parameters != None and len(self.readconfig_parameters) != 0:
            raise InvalidCmdParametersException("The About command no need parameters.")