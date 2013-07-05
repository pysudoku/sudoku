'''
Created on Jul 4, 2013

@author: Ariel Mattos
'''

from sudoku.algorithm.Algorithm import Algorithm
from sudoku.algorithm.exceptions.InvalidSudokuException import InvalidSudokuException

class Recursive(Algorithm):
    '''Solves an Sudoku puzzle using a Recursive Algorithm '''
    puzzle_symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    column_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    row_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I']

    def same_row(self, index, other_index):
        '''Returns true if both indexes are in the same row of a 9 x 9 sudoku puzzle.'''
        return (index // 9 == other_index // 9)
    
    def same_col(self, index, other_index):
        '''Returns true if both indexes are in the same column of a 9 x 9 sudoku puzzle.'''
        return (index - other_index) % 9 == 0
    
    def same_block(self, index, other_index):
        '''Returns true if both indexes are in the same 3 x 3 block of a 9 x 9 sudoku puzzle.'''
        return (index // 27 == other_index // 27 and index % 9 // 3 == other_index % 9 // 3)

    def solve_puzzle(self, puzzle, solutions):
        '''Recursively calculates solutions for a sudoku puzzle.'''

        cell_to_fill = puzzle.find('0')
        if cell_to_fill == -1:
            solutions.append(puzzle)

        already_used_symbols = set()
        for cell in range(81):
            if self.same_row(cell_to_fill,cell) or self.same_col(cell_to_fill,cell) or self.same_block(cell_to_fill,cell):
                already_used_symbols.add(puzzle[cell])

        for symbol in self.puzzle_symbols:
            if symbol not in already_used_symbols:
                self.solve_puzzle(puzzle[:cell_to_fill] + symbol + puzzle[cell_to_fill + 1:], solutions)

    def is_valid_solution(self, candidate_solution):
        '''Returns True if a candidate solution is a valid solution.'''
        for i in range(81):
            if not (self._is_valid_value_in_cell(candidate_solution, i)):
                return False
        return True

    def _is_valid_value_in_cell(self, grid, cell_position):
        '''Returns True if the value in cell_position is unique in the row, 
        column and block it is member of.''' 
        is_unique_in_row = (sorted([grid[j] for j in range(81) if self.same_row(cell_position,j)])) == self.puzzle_symbols
        is_unique_in_column = (sorted([grid[j] for j in range(81) if self.same_col(cell_position,j)])) == self.puzzle_symbols
        is_unique_in_block = (sorted([grid[j] for j in range(81) if self.same_block(cell_position,j)])) == self.puzzle_symbols
        return is_unique_in_row and is_unique_in_column and is_unique_in_block

    def dict_to_str(self, grid):
        '''Takes a dictionary representation of a sudoku puzzle and returns a 
        string representation.'''
        string_representation = ''
        for row in self.row_labels:
            for column in self.column_labels:
                string_representation += '0' if grid[row + column] == '.' else grid[row + column]
        return string_representation

    def str_to_dict(self, grid):
        '''Takes a string representation of a sudoku puzzle and returns a 
        dictionary representation.'''
        dictionary_representation = {}
        index = 0
        for row in self.row_labels:
            for column in self.column_labels:
                dictionary_representation[row + column] = '.' if grid[index] == '0' else grid[index]
                index += 1
        return dictionary_representation

    def solve(self, grid_as_dict):
        '''Returns a list of solutions for the given Sudoku puzzle.'''
        grid_as_str = self.dict_to_str(grid_as_dict)
        candidate_solutions = []
        self.solve_puzzle(grid_as_str, candidate_solutions)
        solutions = [self.str_to_dict(solution) for solution in candidate_solutions if self.is_valid_solution(solution)]
        
        if len(solutions) == 0: raise InvalidSudokuException()
        
        return solutions[0]
