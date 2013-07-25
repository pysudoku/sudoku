from contextlib import contextmanager
from sudoku.reader.exception.fileformaterror import FileFormatError

class SudokuParser:
	puzzle_valid_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	column_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	row_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I']
	error_messages = {
		"invalid_number_of_rows" : str(len(row_labels)) +  
			" rows Sudoku puzzle expected.",
		"invalid_number_of_columns" : str(len(row_labels)) +  
			" columns Sudoku puzzle expected.",
		"invalid_number_of_rows_and_columns" : str(len(row_labels)) + " x " + 
			str(len(column_labels)) + " Sudoku puzzle expected.",
		"input_contains_whitespaces" : "Sudoku puzzle should not contain space characters.",
		"input_contains_invalid_chars" : "A row should contain any of the following characters: " +
		 ' '.join(puzzle_valid_symbols) 
	}

	def parse_puzzle(self, file_name):
		if not file_name.endswith(self.extension):
			raise FileFormatError("Invalid file format. '{}' file expected.".format(self.extension))
		with self.open_sudoku_file(file_name) as (input_file, error):
			if error:
				raise error
			else:
				return self.parse(self.scan(input_file.readlines()))

	def parse(self, tokens):
		dictionary_representation = {}
		for row in self.row_labels:
			for column in self.column_labels:
				dictionary_representation[row + column] = tokens.pop(0)
		return dictionary_representation

	def scan(self, source):
		"""Extracts Sudoku puzzle symbols from file content"""

	@contextmanager
	def open_sudoku_file(self, file_name, mode = 'r'):
		try:
			puzzle_file = open(file_name, mode)
		except IOError as e:
			yield None, e
		else:
			try:
				yield puzzle_file, None
			finally:
				puzzle_file.close()

