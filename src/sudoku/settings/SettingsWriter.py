'''
Created on Jul 10, 2013

@author: Jimena Terceros
'''

import xml.etree.cElementTree as ET

class SettingsWriter(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def write(self, settings, fileName):
        data = ET.Element("data")
        
        self.writeAttributeConfiguration(data, "outputtype", settings.outputType)
        self.writeAttributeConfiguration(data, "algorithmname", settings.algorithmName)
        self.writeAttributeConfiguration(data, "defaultlevel", settings.defaultLevel)
        self.writeAttributeConfiguration(data, "path", settings.path)
        
        self.writeLevels(data, settings)
        
        tree = ET.ElementTree(data)
        tree.write(fileName)
        
    def writeLevels(self, data, settings):
        levels = ET.SubElement(data, "levels")
        for level in settings.levels:
            levelNode = ET.SubElement(levels, "level")
            levelNode.set("name", level.levelName)
            levelNode.set("minLevel", str(level.minLevel))
            levelNode.set("maxLevel", str(level.maxLevel))
        
    def writeAttributeConfiguration(self, data, attributeName, value):
        attributeConfiguration = ET.SubElement(data, attributeName)
        attributeConfiguration.text = value