'''
Created on Jul 16, 2013

@author: Jimena Terceros
'''
import os
from sudoku.settings.SettingsManager import SettingsManager
from sudoku.game.SudokuCommand import SudokuCommand

class ReadConfigurationCommand(SudokuCommand):
    '''
    ReadConfigurationCommand class is defining the command readConfiguration
    @var FILE_NAME_PARAM: the value for fileName. This variable is constant
    '''
    FILE_NAME_PARAM = "fileName"

    def __init__(self, params):
        '''
        Constructor
        '''
        SudokuCommand.__init__(self, params)
        
    def execute(self):
        '''
        execute the command taking account the parameters of the command
        '''
        setting_manager = SettingsManager(self.readconfig_parameters[self.FILE_NAME_PARAM])
        self.game.set_settings_manager(setting_manager)
        self.game.settings_manager.load()
        
    def validate(self):
        '''
        Validate number of parameters and the parameter of the command
        '''
        self.validate_parameter_number(1)
        self.valida_param(self.FILE_NAME_PARAM)