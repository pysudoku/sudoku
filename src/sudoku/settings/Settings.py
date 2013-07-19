'''
Created on Jul 6, 2013

@author: Jimena Terceros
'''
from sudoku.settings.Level import Level
class Settings(object):
    '''
    classdocs
    ''' 
    
    DEFAULT_OUTPUT_TYPE = "Console"
    DEFAULT_ALGORITHM_NAME = "Peter Norvic"
    DEFAULT_LEVEL_NAME = "EASY"
    DEFAULT_MIN = 36
    DEFAULT_MAX = 49

    def __init__(self, fileName):
        '''
        Constructor
        '''
        self.fileName = fileName
        self.outputType = ""
        self.path = ""
        self.algorithmName = ""
        self.defaultLevel = ""
        self.levels = []

    def createDefaultSettings(self):
        self.outputType = self.DEFAULT_OUTPUT_TYPE
        self.algorithmName = self.DEFAULT_ALGORITHM_NAME
        self.defaultLevel = self.DEFAULT_LEVEL_NAME
        self.levels.append(Level(self.DEFAULT_LEVEL_NAME, self.DEFAULT_MIN, self.DEFAULT_MAX))
        self.levels.append(Level('MODERATE', 32, 35))
        self.levels.append(Level('HARD', 28, 31))

    def getOutputType(self):
        return self.outputType
        
    def getAlgorithmName(self):
        return self.algorithmName
    
    def getPath(self):
        return self.path
    
    def getDefaultLevel(self):
        return self.defaultLevel
    
    def getLevels(self):
        return self.levels
    
    def addLevel(self, level):
        self.levels.append(level)
        
    def getLevel(self, name):
        for level in self.levels:
            if level.levelName == name:
                return level
            
    def setOutputType(self, outputType):
        self.outputType = outputType
        
    def setAlgorithmName(self, algorithmName):
        self.algorithmName = algorithmName
        
    def setDefaultLevel(self, defaultLevel):
        self.defaultLevel = defaultLevel
        
    def setPath(self, path):
        self.path = path