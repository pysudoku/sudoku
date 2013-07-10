'''
Created on Jul 10, 2013

@author: Jimena Terceros
'''

class Level(object):
    '''
    classdocs
    '''


    def __init__(self, levelName, minLevel, maxLevel):
        '''
        Constructor
        '''
        self.levelName = levelName
        self.minLevel = minLevel
        self.maxLevel = maxLevel
        
    def __eq__(self, otherLevel):
        if self.levelName == otherLevel.levelName and self.minLevel == otherLevel.minLevel and self.maxLevel == otherLevel.maxLevel:
            return True
        else:
            return False