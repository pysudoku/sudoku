'''
Created on Jul 5, 2013

@author: Jimena Terceros
'''
import unittest
from sudoku.settings.exceptions.InvalidXMLSettingsException import InvalidXMLSettingsException
from sudoku.settings.exceptions.FileNotFoundException import FileNotFoundException
from sudoku.settings.SettingsReader import SettingsReader
from sudoku.settings.Level import Level

class TestSettingsReader(unittest.TestCase):

    def setUp(self):
        self.notExistFileName = "settings2.xml"

        self.createValidXMLConfigFile()
        self.createInvalidXMLConfigFile()
        self.createCorruptedXMlConfigFile()
    
    def tearDown(self):
        pass
        
    def createCorruptedXMlConfigFile(self):
        self.corruptedFileName = "corruptedSettings.xml"
        
        file = open(self.corruptedFileName, "w")
        file.write("<data>\n")
        file.write("<data>\n")
        file.close()
        
    def createInvalidXMLConfigFile(self):
        self.invaliFileName = "invalidSettings.xml"
        
        file = open(self.invaliFileName, "w")
        file.write("<data>\n")
        file.write("</data>\n")
        file.close()
        
    def createValidXMLConfigFile(self):
        self.fileName = "settings.xml"
        self.outputType = "file"
        self.algorithmName = "Peter Norving"
        self.defaultLevel = "Level 2"
        self.levels = [Level("Level 1", 5, 10), Level("Level 2", 11, 20), Level("Level 3", 21, 30)]
        self.path = "c:\test"
        
        file = open(self.fileName, "w")
        file.write("<data>\n")
        file.write("<outputtype>file</outputtype>\n")
        file.write("<path>c:\test</path>\n")
        file.write("<algorithmname>Peter Norving</algorithmname>\n")
        file.write("<defaultlevel>Level 2</defaultlevel>\n")
        file.write("<levels>\n")
        file.write("<level name='Level 1' minLevel='5' maxLevel='10'></level>\n")
        file.write("<level name='Level 2' minLevel='11' maxLevel='20'></level>\n")
        file.write("<level name='Level 3' minLevel='21' maxLevel='30'></level>\n")
        file.write("</levels>\n")
        file.write("</data>\n")
        file.close()

    def test_Given_a_valid_xml_file_then_read_output_type_properly(self):
        reader = SettingsReader()
        settings = reader.read(self.fileName)
        outputType = settings.getOutputType()
        expectedOutputType = self.outputType
        self.assertEqual(expectedOutputType, outputType)
        
    def test_Given_a_valid_xml_file_then_read_path_properly(self):
        reader = SettingsReader()
        settings = reader.read(self.fileName)
        path = settings.getPath()
        expectedPath = self.path
        self.assertEqual(expectedPath, path)
        
    def test_Given_a_valid_xml_file_then_read_default_algorithm_properly(self):
        reader = SettingsReader()
        settings = reader.read(self.fileName)
        algorithmName = settings.getAlgorithmName()
        expectedAlgorithmName = self.algorithmName
        self.assertEqual(expectedAlgorithmName, algorithmName)
    
    def test_Given_a_valid_xml_file_then_read_default_level_properly(self):
        reader = SettingsReader()
        settings = reader.read(self.fileName)
        defaultLevel = settings.getDefaultLevel()
        expectedDefaultLevel = self.defaultLevel
        self.assertEqual(expectedDefaultLevel, defaultLevel)    
    
    def test_Given_a_valid_xml_file_then_read_dificult_levels_properly(self):
        reader = SettingsReader()
        settings = reader.read(self.fileName)
        levels = settings.getLevels()
        expectedlevels = self.levels
        self.assertListEqual(expectedlevels, levels)
     
    def test_Given_an_xmlconfig_without_OutputType_Value_then_the_default_value_should_be_used(self):
        reader = SettingsReader()
        settings = reader.read(self.invaliFileName)
        outputType = settings.getOutputType()
        expectedOutputType = settings.DEFAULT_OUTPUT_TYPE
        self.assertEqual(expectedOutputType, outputType)
    
    def test_Given_an_xmlconfig_without_AlgorithmName_Value_then_the_default_value_should_be_used(self):
        reader = SettingsReader()
        settings = reader.read(self.invaliFileName)
        algorithmName = settings.getAlgorithmName()
        expectedalgorithmName = settings.DEFAULT_ALGORITHM_NAME
        self.assertEqual(expectedalgorithmName, algorithmName)
        
    def test_Given_an_xmlconfig_without_DefaultLevel_Value_then_the_default_value_should_be_used(self):
        reader = SettingsReader()
        settings = reader.read(self.invaliFileName)
        defaultLevel = settings.getDefaultLevel()
        expectedDefaultLevel = settings.DEFAULT_LEVEL_NAME
        self.assertEqual(expectedDefaultLevel, defaultLevel)
        
    def test_Given_an_xmlconfig_without_levels_then_a_default_level_should_be_created(self):
        reader = SettingsReader()
        settings = reader.read(self.invaliFileName)
        levels = settings.getLevels()
        
        expectedSize = 1
        expectedLevelName = Level(settings.DEFAULT_LEVEL_NAME, settings.DEFAULT_MIN, settings.DEFAULT_MAX)
        self.assertEqual(expectedSize, len(levels))
        self.assertEqual(expectedLevelName, levels[0])

    def test_Given_a_bad_xml_file_then_verify_that_raise_an_exception(self):
        try:
            reader = SettingsReader()
            reader.read(self.corruptedFileName)
            self.fail("Didn't raise an expected exception.")
        except InvalidXMLSettingsException:
            pass
        
    def test_if_the_xml_config_file_is_not_found_then_should_be_created_one_with_default_values(self):
        try:
            reader = SettingsReader()
            reader.read("Mytest.xml")
            self.fail("Didn't raise an expected exception.")
        except FileNotFoundException:
            pass
    
    def test_If_there_is_not_settings_file_the_should_create_default_settings_file(self):
        pass

if __name__ == "__main__":
    unittest.main()