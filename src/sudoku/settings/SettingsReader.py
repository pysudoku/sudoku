'''
Created on Jul 9, 2013

@author: Jimena Terceros
'''
from xml.dom import minidom
from xml.parsers.expat import ExpatError 
from sudoku.settings.exceptions.InvalidXMLSettingsException import InvalidXMLSettingsException
from sudoku.settings.exceptions.FileNotFoundException import FileNotFoundException
from sudoku.settings.Settings import Settings
from sudoku.settings.Level import Level

class SettingsReader(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def read(self, fileName):
        settings = Settings(fileName)
        try:
            settingsdoc = minidom.parse(fileName)
            
            settings.outputType = self.readAttributeConfiguration('outputtype', settings.DEFAULT_OUTPUT_TYPE, settingsdoc)
            if(settings.outputType == "file"):
                settings.path = self.readAttributeConfiguration('path', "", settingsdoc)
            settings.algorithmName = self.readAttributeConfiguration('algorithmname', settings.DEFAULT_ALGORITHM_NAME, settingsdoc)
            settings.defaultLevel = self.readAttributeConfiguration('defaultlevel', settings.DEFAULT_LEVEL_NAME, settingsdoc)
            settings.levels = self.readlevels(settingsdoc, settings)
        except FileNotFoundError:
            raise FileNotFoundException(fileName)
        except ExpatError:
            raise InvalidXMLSettingsException(fileName)
        
        return settings

    def readlevels(self, settingsdoc, settings):
        allLevels = []
        lislevels = settingsdoc.getElementsByTagName("level")
        if(len(lislevels) > 0):
            for s in lislevels:
                levelName = s.attributes["name"].value
                minLevel = int(s.attributes["minLevel"].value)
                maxnLevel = int(s.attributes["maxLevel"].value)
                level = Level(levelName, minLevel, maxnLevel)
                allLevels.append(level)
        else:
            allLevels.append(Level(settings.DEFAULT_LEVEL_NAME, settings.DEFAULT_MIN, settings.DEFAULT_MAX))
        return allLevels
        
    def readAttributeConfiguration(self, attributeName, defaultValue, settingsdoc):
        attributeList = settingsdoc.getElementsByTagName(attributeName)
        if len(attributeList) > 0:
            return attributeList[0].firstChild.data
        else:
            return defaultValue