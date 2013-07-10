'''
Created on Jul 6, 2013

@author: Jimena Terceros
'''
class Settings(object):
    '''
    classdocs
    ''' 
    
    DEFAULT_OUTPUT_TYPE = "Console"
    DEFAULT_ALGORITHM_NAME = "Peter Norvic"
    DEFAULT_LEVEL_NAME = "Level 1"
    DEFAULT_MIN = 15
    DEFAULT_MAX = 20

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
        self.levels.append(self.DEFAULT_LEVEL_NAME)

    def getOutputType(self):
        return self.outputType
    
    def getalgorithmName(self):
        return self.algorithmName
    
    def getPath(self):
        return self.path
    
    def getdefaultLevel(self):
        return self.defaultLevel
    
    def getlevels(self):
        return self.levels
    
    def addlevel(self, level):
        self.levels.append(level)
        
    def getlevel(self, name):
        for level in self.levels:
            if level.name == name:
                return level