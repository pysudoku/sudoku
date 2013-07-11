import unittest
from sudoku.reader.commandlineparser import CommandLineParser

class TestCommandLineParser(unittest.TestCase):
	def setUp(self):
		self.test_data = {
			'well_formed_content' :	"067040002" + 
									"900730450" +
									"405000000" + 
									"600080000" + 
									"000900320" + 
									"283500649" + 
									"070000003" + 
									"000657804" +
									"006423597",

			'content_with_spaces' :	"06704000 " + 
									"900730450" +
									"405000000" + 
									"600080000" + 
									"000900320" + 
									"283500649" + 
									"070000003" + 
									"000657804" +
									"006423597",

			'content_with_chars' :	".67.4...2" + 
									"9..73.45." +
									"4.5......" + 
									"6...8...." + 
									"...9..32." + 
									"2835..649" + 
									".7......3" + 
									"...6578.4" +
									"..6423597",

			'content_contains_more_than_9_lines' :	"067040002" + 
													"900730450" +
													"405000000" + 
													"600080000" + 
													"000900320" + 
													"283500649" + 
													"070000003" + 
													"000657804" +
													"006423597" +
													"006423597",

			'content_contains_less_than_9_lines' :	"067040002" + 
													"900730450" +
													"000657804" +
													"006423597"
		}
		self.cliparser = CommandLineParser()

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

	def tearDown(self):
		pass

	def test_well_formed_parameter_should_be_parsed(self):
		actual_results = self.cliparser.parse_puzzle(self.test_data['well_formed_content'])
		expected_results = self.puzzle
		self.assertEqual(expected_results, actual_results)

	def test_a_SyntaxError_should_be_raised_if_parameter_contains_spaces(self):
		with self.assertRaises(SyntaxError):
			self.cliparser.parse_puzzle(self.test_data['content_with_spaces'])

	def test_a_SyntaxError_should_be_raised_if_parameter_contains_non_digit_characters(self):
		with self.assertRaises(SyntaxError):
			self.cliparser.parse_puzzle(self.test_data['content_with_chars'])

	def test_a_SyntaxError_should_be_raised_if_parameter_contains_more_than_nine_lines(self):
		with self.assertRaises(SyntaxError):
			self.cliparser.parse_puzzle(self.test_data['content_contains_more_than_9_lines'])

	def test_a_SyntaxError_should_be_raised_if_parameter_contains_less_than_nine_columns(self):
		with self.assertRaises(SyntaxError):
			self.cliparser.parse_puzzle(self.test_data['content_contains_less_than_9_lines'])

if __name__ == '__main__':
	unittest.main()