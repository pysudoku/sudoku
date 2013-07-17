'''
Created on Jul 16, 2013

@author: Jimena Terceros
'''
class Game(object):
    '''
    Game class create the game empty. all commands update the fields of this class 
    '''

    def __init__(self):
        '''
        Constructor
        @var settings_manager: the value for all application settings that by default is none
        @var initial_sudoku: the value for initial Sudoku Board by defaul is none
        @var user_sudoku: the value for user Sudoku Board attribute by default is none
        @var solved_sudoku: the value for solved Sudoku attribute by default is none
        '''
        self.settings_manager = None
        self.initial_sudoku = None
        self.user_sudoku = None
        self.solved_sudoku = None

    
    def set_settings_manager(self, settingsManager):
        '''
        Sets the setting manager value
        '''
        self.settings_manager = settingsManager