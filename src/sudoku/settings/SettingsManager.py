'''
Created on Jul 11, 2013

@author: Jimena Terceros
'''
from sudoku.settings.Settings import Settings
from sudoku.settings.SettingsReader import SettingsReader
from sudoku.settings.exceptions.FileNotFoundException import FileNotFoundException
from sudoku.settings.SettingsWriter import SettingsWriter

class SettingsManager(object):
    '''
    SettingsManager class manage configuration file, reading and writing settings
    '''

    def __init__(self, fileName):
        "Initialize all the variables use to manage settings of the configuration file"
        self.settings = Settings(fileName)
        self.fileName = fileName

    def load(self):
        '''
        Settings are read of the configuration file given a file_name
        '''
        reader = SettingsReader()
        try:
            self.settings = reader.read(self.fileName)
        except FileNotFoundException:
            self.settings.createDefaultSettings()
            self.save()
            
    def save(self):
        '''
        Settings are save\wrote in the configuration file
        '''
        writer = SettingsWriter()
        writer.write(self.settings, self.fileName)

    def getSettings(self):
        '''
        return settings of the configuration file
        '''
        return self.settings