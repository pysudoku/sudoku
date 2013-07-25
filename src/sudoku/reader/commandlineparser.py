from sudoku.reader.sudokuparser import SudokuParser
from sudoku.reader.exception.fileformaterror import FileFormatError

class CommandLineParser(SudokuParser):
	def parse_puzzle(self, parameter):
		return self.parse(self.scan(parameter))

	def scan(self, param):
		if param.rfind('.') != -1:
			raise FileFormatError("Invalid file format. A '{}' file was not expected.".format(param[param.rfind('.'):]))
		elif len(param) != (len(self.row_labels) * len(self.column_labels)):
			raise SyntaxError(self.error_messages['invalid_number_of_rows_and_columns'])
		elif param.find(' ') != -1 or param.find('\t') != -1:
			raise SyntaxError(self.error_messages['input_contains_whitespaces'])
		elif not param.isdigit():
			raise SyntaxError(self.error_messages['input_contains_invalid_chars'])
		else:
			return list(param.replace('0', '.'))
