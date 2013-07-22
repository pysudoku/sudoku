'''
Created on Jul 10, 2013

@author: Jimena Terceros
'''
import unittest
from sudoku.settings.Level import Level
from sudoku.settings.SettingsWriter import SettingsWriter
from sudoku.settings.Settings import Settings


class TestSettingsWriter(unittest.TestCase):


    def setUp(self):
        self.fileName = "settings.xml"
        self.outputType = "file"
        self.algorithmName = "Peter Norving"
        self.defaultLevel = "Level 2"
        self.levels = [Level("Level 1", 5, 10), Level("Level 2", 11, 20), Level("Level 3", 21, 30)]
        self.path = "c:\\test"
        
        self.settings = Settings(self.fileName)
        self.settings.setOutputType(self.outputType)
        self.settings.setAlgorithmName(self.algorithmName)
        self.settings.setPath(self.path)
        self.settings.setDefaultLevel(self.defaultLevel)
        
        for level in self.levels:
            self.settings.addLevel(level)

    def tearDown(self):
        pass
    
    def readFile(self, fileName):
        file = open(self.fileName)
        result = ""
        line = file.readline()
        while line != "":
            result = result + line
            line = file.readline()
            
        return result

    def test_given_the_ouputtype_parameter_then_should_be_set_the_ouputtype_parameter_in_the_file_when_it_is_saved(self):
        outputType = "console"
        
        writer = SettingsWriter()
        self.settings.setOutputType(outputType)
        writer.write(self.settings, self.fileName)
        
        actualValue = self.readFile(self.fileName)
        excpectedValue = "<data><outputtype>console</outputtype><algorithmname>Peter Norving</algorithmname><defaultlevel>Level 2</defaultlevel><path>c:\\test</path><levels><level maxLevel=\"10\" minLevel=\"5\" name=\"Level 1\" /><level maxLevel=\"20\" minLevel=\"11\" name=\"Level 2\" /><level maxLevel=\"30\" minLevel=\"21\" name=\"Level 3\" /></levels></data>"
        self.maxDiff = None
        self.assertEqual(excpectedValue, actualValue)

    
    def test_given_the_algorithmName_parameter_then_should_be_set_the_algorithmName_parameter_in_the_file_when_it_is_saved(self):
        algorithmName = "Recursive"
        
        writer = SettingsWriter()
        self.settings.setAlgorithmName(algorithmName)
        writer.write(self.settings, self.fileName)
        
        actualValue = self.readFile(self.fileName)
        excpectedValue = "<data><outputtype>file</outputtype><algorithmname>Recursive</algorithmname><defaultlevel>Level 2</defaultlevel><path>c:\\test</path><levels><level maxLevel=\"10\" minLevel=\"5\" name=\"Level 1\" /><level maxLevel=\"20\" minLevel=\"11\" name=\"Level 2\" /><level maxLevel=\"30\" minLevel=\"21\" name=\"Level 3\" /></levels></data>"
        self.maxDiff = None
        self.assertEqual(excpectedValue, actualValue)
    
    def test_given_the_defaultLevel_parameter_then_should_be_set_the_defaultLevel_parameter_in_the_file_when_it_is_saved(self):
        defaultLevel = "Level 1"
        
        writer = SettingsWriter()
        self.settings.setDefaultLevel(defaultLevel)
        writer.write(self.settings, self.fileName)
        
        actualValue = self.readFile(self.fileName)
        excpectedValue = "<data><outputtype>file</outputtype><algorithmname>Peter Norving</algorithmname><defaultlevel>Level 1</defaultlevel><path>c:\\test</path><levels><level maxLevel=\"10\" minLevel=\"5\" name=\"Level 1\" /><level maxLevel=\"20\" minLevel=\"11\" name=\"Level 2\" /><level maxLevel=\"30\" minLevel=\"21\" name=\"Level 3\" /></levels></data>"
        self.maxDiff = None
        self.assertEqual(excpectedValue, actualValue)
    
    def test_given_the_path_parameter_then_should_be_set_the_path_parameter_in_the_file_when_it_is_saved(self):
        path = "h:\\test\\test2"
        
        writer = SettingsWriter()
        self.settings.setPath(path)
        writer.write(self.settings, self.fileName)
        
        actualValue = self.readFile(self.fileName)
        excpectedValue = "<data><outputtype>file</outputtype><algorithmname>Peter Norving</algorithmname><defaultlevel>Level 2</defaultlevel><path>h:\\test\\test2</path><levels><level maxLevel=\"10\" minLevel=\"5\" name=\"Level 1\" /><level maxLevel=\"20\" minLevel=\"11\" name=\"Level 2\" /><level maxLevel=\"30\" minLevel=\"21\" name=\"Level 3\" /></levels></data>"
        self.maxDiff = None
        self.assertEqual(excpectedValue, actualValue)
    
    def test_given_the_levels_parameter_then_should_be_added_the_levels_parameter_in_the_file_when_it_is_saved(self):
        level = Level("Level 4", 7, 40)
        
        self.settings.addLevel(level)
        writer = SettingsWriter()
        writer.write(self.settings, self.fileName)
        
        actualValue = self.readFile(self.fileName)
        excpectedValue = "<data><outputtype>file</outputtype><algorithmname>Peter Norving</algorithmname><defaultlevel>Level 2</defaultlevel><path>c:\\test</path><levels><level maxLevel=\"10\" minLevel=\"5\" name=\"Level 1\" /><level maxLevel=\"20\" minLevel=\"11\" name=\"Level 2\" /><level maxLevel=\"30\" minLevel=\"21\" name=\"Level 3\" /><level maxLevel=\"40\" minLevel=\"7\" name=\"Level 4\" /></levels></data>"

        self.maxDiff = None
        self.assertEqual(excpectedValue, actualValue)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()