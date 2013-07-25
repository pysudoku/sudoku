'''
Created on Jul 25, 2013

@author: Administrator
'''
import unittest
import os
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.game.Import import ImportCommand
from sudoku.settings.SettingsManager import SettingsManager
from sudoku.game.Game import Game


class TestImportCommand(unittest.TestCase):


    def setUp(self):
        self.test_data = {
                          'well_formed_content' : "067040002\n" +
                                                  "900730450\n" +
                                                  "405000000\n" + 
                                                  "600080000\n" + 
                                                  "000900320\n" + 
                                                  "283500649\n" + 
                                                  "070000003\n" + 
                                                  "000657804\n" +
                                                  "006423597\n"
                        }
        
        with open('puzzle_file.txt', 'w') as test_file:
            test_file.write(self.test_data['well_formed_content'])

        self.valid_params = {'input':'puzzle_file.txt'}

    def tearDown(self):
        try:
            os.remove('puzzle_file.txt')
        except IOError:
            pass

        try:
            os.remove('mySettings.xml')
        except IOError:
            pass

    def test_an_InvalidCmdParametersException_should_be_raised_if_game_is_None(self):
        with self.assertRaises(InvalidCmdParametersException):
            cmd = ImportCommand(self.valid_params)
            cmd.execute()

    def test_a_game_should_be_imported(self):
        settings_manager = SettingsManager('mySettings.xml')
        settings_manager.load()
        game = Game()
        game.set_settings_manager(settings_manager)
        game.start_game_timer()
        import_command = ImportCommand(self.valid_params)
        import_command.set_game(game)
        import_command.execute()
        self.assertEqual((game.initial_sudoku.to_dictionary())['A1'], '.')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()