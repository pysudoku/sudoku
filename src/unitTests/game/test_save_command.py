'''
Created on Jul 25, 2013

@author: Administrator
'''
import unittest
import pickle
import os
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.game.SaveGame import SaveGameCommand
from sudoku.game.Game import Game
from sudoku.model.sudokutable import SudokuBoard
from sudoku.settings.SettingsManager import SettingsManager


class TestSaveGameCommand(unittest.TestCase):

    def setUp(self):
        self.puzzle = {
                       "A1":'.', "A2":'6', "A3":'7', "A4":'.', "A5":'4', "A6":'.', "A7":'.', "A8":'.', "A9":'2',
                       "B1":'9', "B2":'.', "B3":'.', "B4":'7', "B5":'3', "B6":'.', "B7":'4', "B8":'5', "B9":'.',
                       "C1":'4', "C2":'.', "C3":'5', "C4":'.', "C5":'.', "C6":'.', "C7":'.', "C8":'.', "C9":'.',
                       "D1":'6', "D2":'.', "D3":'.', "D4":'.', "D5":'8', "D6":'.', "D7":'.', "D8":'.', "D9":'.',
                       "E1":'.', "E2":'.', "E3":'.', "E4":'9', "E5":'.', "E6":'.', "E7":'3', "E8":'2', "E9":'.',
                       "F1":'2', "F2":'8', "F3":'3', "F4":'5', "F5":'.', "F6":'.', "F7":'6', "F8":'4', "F9":'9',
                       "G1":'.', "G2":'7', "G3":'.', "G4":'.', "G5":'.', "G6":'.', "G7":'.', "G8":'.', "G9":'3',
                       "H1":'.', "H2":'.', "H3":'.', "H4":'6', "H5":'5', "H6":'7', "H7":'8', "H8":'.', "H9":'4',
                       "I1":'.', "I2":'.', "I3":'6', "I4":'4', "I5":'2', "I6":'3', "I7":'5', "I8":'9', "I9":'7'
                      }

        self.valid_params = {'file':'game.sgf'}


    def tearDown(self):
        try:
            os.remove('game.sgf')
        except IOError:
            pass

        try:
            os.remove('mySettings.xml')
        except IOError:
            pass

    def test_an_InvalidCmdParametersException_should_be_raised_if_game_is_None(self):
        with self.assertRaises(InvalidCmdParametersException):
            cmd = SaveGameCommand(self.valid_params)
            cmd.execute()
            
    def test_a_game_should_be_saved(self):
        settings_manager = SettingsManager('mySettings.xml')
        settings_manager.load()
        game = Game()
        game.set_settings_manager(settings_manager)
        game.initial_sudoku = SudokuBoard()
        game.initial_sudoku.from_dictionary(self.puzzle, True)
        game.start_game_timer()
        save_game_command = SaveGameCommand(self.valid_params)
        save_game_command.set_game(game)
        save_game_command.execute()
        game_file = open('game.sgf', 'rb')
        read_game = pickle.load(game_file)
        self.assertEqual(game.initial_sudoku.to_dictionary(), read_game.initial_sudoku.to_dictionary())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()