'''
Created on Jul 16, 2013

@author: Jimena Terceros
'''
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException

class SudokuCommand(object):
    '''
    sudokucommand class is abstract that has as parameter parameters of the command
    '''

    def __init__(self, params):
        '''
        Constructor
        @param readconfig_parameters: the value for readconfig_parameters attribute
        @param game: the value for game attribute by default is in None  
        '''
        self.readconfig_parameters = params
        self.game = None
        
        self.validate()
        
    def set_game(self, game):
        self.game = game
        
    def execute(self):
        '''
        Abstract function that will execute the command. It will be implemented in every command
        '''
        
    def validate(self):
        '''
        Abstract function that will validate the parameters of the command. It will be implemented in every command
        '''
        
    def validate_parameter_number(self, number):
        '''
        Validate the number of parameters that is given in the command
        '''
        if self.readconfig_parameters == None:
            raise InvalidCmdParametersException("The command should have valid parameters.")
        elif len(self.readconfig_parameters) != number:
            raise InvalidCmdParametersException("The read configuration command support only " + str(number) + " parameters.")
    
    def valida_param(self, paramName):
        '''
        Validate the parameter given in the command
        '''
        if not self.readconfig_parameters.__contains__(paramName):
            raise InvalidCmdParametersException("The read configuration command needs " + paramName + " parameter.")
        elif self.readconfig_parameters[paramName] == None:
            raise InvalidCmdParametersException("The read configuration command should have a valid " + paramName + " parameter.")