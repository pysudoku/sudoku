'''
Created on Jul 16, 2013

@author: Jimena Terceros
'''
import unittest
from sudoku.game.Game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        pass

    def test_if_a_game_is_created_then_should_create_with_default_attribute_values(self):
        game = Game()
        
        self.assertIsNone(game.settings_manager)
        self.assertIsNone(game.initial_sudoku)
        self.assertIsNone(game.user_sudoku)
        self.assertIsNone(game.solved_sudoku)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()