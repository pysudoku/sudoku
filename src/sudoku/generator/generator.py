from sudoku.algorithm.recursive import Recursive
import random

class Generator(Recursive):
	
	def _create_terminal_pattern(self):
		'''Creates a pattern of solution by means of a randomized algorithm'''
		puzzle = ['0'] * 81
		cell = 0
		while cell < 81:
			available_symbols = self._get_available_symbols(puzzle, cell)
			if len(available_symbols) > 0:
				puzzle[cell] = random.choice(available_symbols)
				cell += 1
			else:
				self._fill_list(puzzle, '0', 0, cell)
				cell = 0
		return puzzle

	def _fill_list(self, list_to_fill, value, start, stop):
		'''Fill a list from start to stop using the specified value
		@param list_to_fill: the list on which the values are going to be filled.
		@param value: the value to fill the list with.
		@param start: the start index.
		@param stop: the stop index.
		'''
		for index in range(start, stop if stop < len(list_to_fill) else len(list_to_fill)):
			list_to_fill[index] = value

	def _dig_holes(self, puzzle, givens):
		'''Randomly removes cells. Verifies that the Sudoku puzzle has
		one solution while cells are removed. Return a valid Sudoku puzzle.
		@param puzzle: the Sudoku puzzle as list of int representation.
		@param givens: the number of givens. Value should be defined by game level.
		'''
		can_be_dug_cells = list(range(81))
		given_cells = []
		while ((len(can_be_dug_cells) + len(given_cells)) > givens) and (len(can_be_dug_cells) > 0):
			cell_to_dig = random.choice(can_be_dug_cells)
			if self._can_be_dug_up(puzzle, cell_to_dig):
				puzzle[cell_to_dig] = '0'
			else:
				given_cells.append(cell_to_dig)
			can_be_dug_cells.remove(cell_to_dig)
		return puzzle

	def _can_be_dug_up(self, puzzle, cell):
		'''Returns 'True' if a cell can be dug up keeping one possible 
		solution for the puzzle.
		@param puzzle: the Sudoku puzzle as list of int representation.
		@param cell: the cell to test.
		'''
		solutions = []
		self.solve_puzzle(''.join(puzzle[:cell]) + '0' + ''.join(puzzle[cell + 1:]), solutions)
		return len(solutions) == 1

	def generate_puzzle(self, level):
		'''Generates a valid Sudoku puzzle for the given level. 
		The Sudoku puzzle is returned as a dictionary.
		@param level: the level to use in order to generate the puzzle.
		'''
		terminal_pattern = self._create_terminal_pattern()
		puzzle = self._dig_holes(terminal_pattern, random.randint(level.minLevel, level.maxLevel))
		return self.str_to_dict(''.join(puzzle))

