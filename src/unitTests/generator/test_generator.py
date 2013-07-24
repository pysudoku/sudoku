import unittest
from sudoku.settings.Level import Level
from sudoku.generator.generator import Generator

class TestGenerator(unittest.TestCase):
	'''Given, the generator uses a random algorithm, tests are 
	limited to verify that the puzzle has one valid solution and the 
	number of holes are within the range the difficulty level 
	speficies.'''
	
	def setUp(self):
		self.generator = Generator()
		self.string_dict = {'A1': '0', 'A2': '1', 'A3': '2', 'A4': '3', 'A5': '4', 'A6': '5'}
		self.int_dict = {'A1': 0, 'A2': 1, 'A3': 2, 'A4': 3, 'A5': 4, 'A6': 5}

	def test_generator_should_generate_an_easy_level_puzzle_within_the_givens_bounds(self):
		EASY_LEVEL = Level("EASY", 36, 49)
		puzzle = self.generator.generate_puzzle(EASY_LEVEL)
		givens = len((self.generator.dict_to_str(puzzle)).replace('0', ''))
		self.assertTrue(givens >= EASY_LEVEL.minLevel and givens <= EASY_LEVEL.maxLevel)

	def test_generator_should_generate_an_medium_level_puzzle_within_the_givens_bounds(self):
		MEDIUM_LEVEL = Level("MEDIUM", 32, 35)
		puzzle = self.generator.generate_puzzle(MEDIUM_LEVEL)
		givens = len((self.generator.dict_to_str(puzzle)).replace('0', ''))
		self.assertTrue(givens >= MEDIUM_LEVEL.minLevel and givens <= MEDIUM_LEVEL.maxLevel)

	def test_generator_should_generate_an_hard_level_puzzle_within_the_givens_bounds(self):
		HARD_LEVEL = Level("HARD", 36, 49)
		puzzle = self.generator.generate_puzzle(HARD_LEVEL)
		givens = len((self.generator.dict_to_str(puzzle)).replace('0', ''))
		self.assertTrue(givens >= HARD_LEVEL.minLevel and givens <= HARD_LEVEL.maxLevel)

	def test_generator_should_generate_a_valid_easy_level_sudoku_puzzle(self):
		EASY_LEVEL = Level("EASY", 36, 49)
		puzzle = self.generator.generate_puzzle(EASY_LEVEL)
		self.assertTrue(len(self.generator.find_all_solutions(puzzle)) == 1)

	def test_generator_should_generate_a_valid_medium_level_sudoku_puzzle(self):
		MEDIUM_LEVEL = Level("MEDIUM", 32, 35)
		puzzle = self.generator.generate_puzzle(MEDIUM_LEVEL)
		self.assertTrue(len(self.generator.find_all_solutions(puzzle)) == 1)

	def test_generator_should_generate_a_valid_hard_level_sudoku_puzzle(self):
		HARD_LEVEL = Level("HARD", 36, 49)
		puzzle = self.generator.generate_puzzle(HARD_LEVEL)
		self.assertTrue(len(self.generator.find_all_solutions(puzzle)) == 1)

if __name__ == '__main__':
	unittest.main()