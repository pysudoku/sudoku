'''
Created on Jul 24, 2013

@author: Administrator
'''
from sudoku.game.SudokuCommand import SudokuCommand
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.writer.WriterFactory import WriterFactory

class ExportCommand(SudokuCommand):
    '''
    Writes a Sudoku puzzle to a TXT file.
    '''
    OUTPUT_PARAM = "output"

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
        elif self.game.initial_sudoku == None:
            raise InvalidCmdParametersException("The Sudoku was not loaded.")

        writer_factory = WriterFactory('txt')
        writer = writer_factory.getWriter()
        writer.write(self.game.initial_sudoku.to_dictionary(), self.readconfig_parameters[self.OUTPUT_PARAM])
                
    def validate(self):
        '''
        Validate number of parameters and the parameter of the command
        '''
        self.validate_parameter_number(1)
        self.valida_param(self.OUTPUT_PARAM)