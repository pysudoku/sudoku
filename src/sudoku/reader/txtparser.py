from sudoku.reader.sudokuparser import SudokuParser

class TXTParser(SudokuParser):
	extension = '.txt'

	def scan(self, source):
		tokens = []
		if len(source) != len(self.row_labels):
			raise SyntaxError(self.error_messages['invalid_number_of_rows'])
		for line in source:
			row = line.rstrip('\n')
			if row.find(' ') != -1 or row.find('\t') != -1:
				raise SyntaxError(self.error_messages['input_contains_whitespaces'])
			elif not row.isdigit():
				raise SyntaxError(self.error_messages['input_contains_invalid_chars'])
			elif len(row) != len(self.column_labels) :
				raise SyntaxError(self.error_messages['invalid_number_of_columns'])
			else:
				tokens.extend(list(row.replace('0', '.')))
		return tokens
