'''
Created on Jul 16, 2013

@author: Jimena Terceros
'''
import unittest
from sudoku.game.Game import Game
from sudoku.model.sudokutable import SudokuBoard

class TestGame(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_if_a_game_is_created_then_should_create_with_default_attribute_values(self):
        game = Game()
        
        self.assertIsNone(game.settings_manager)
        self.assertIsNone(game.initial_sudoku)
        self.assertIsNone(game.user_sudoku)
        self.assertIsNone(game.solved_sudoku)
        
    def test_game_attributes_should_be_copied_when_a_game_is_copied(self):
        puzzle = {
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
        game = Game()
        game.initial_sudoku = SudokuBoard()
        game.initial_sudoku.from_dictionary(puzzle)
        game.user_sudoku = SudokuBoard()
        game.user_sudoku.from_dictionary(puzzle)
        game.solved_sudoku = SudokuBoard()
        game.solved_sudoku.from_dictionary(puzzle)
        game.currentTime = 1.0
        game.started = True
        game.paused = True
        
        other_game = Game()
        other_game.copy(game)
        self.assertEqual(game.initial_sudoku.to_dictionary(), other_game.initial_sudoku.to_dictionary())
        self.assertEqual(game.user_sudoku.to_dictionary(), other_game.user_sudoku.to_dictionary())
        self.assertEqual(game.solved_sudoku.to_dictionary(), other_game.solved_sudoku.to_dictionary())
        self.assertEqual(game.currentTime, other_game.currentTime)
        self.assertEqual(game.started, other_game.started)
        self.assertEqual(game.paused, other_game.paused)
        
        
        
        
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()