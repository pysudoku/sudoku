'''
Created on Jul 23, 2013

@author: Administrator
'''
import unittest

from sudoku.reader.parser_factory import ParserFactory
from sudoku.reader.txtparser import TXTParser
from sudoku.reader.csvparser import CSVParser
from sudoku.reader.commandlineparser import CommandLineParser

class TestParserFactory(unittest.TestCase):


    def setUp(self):
        self.parser_factory = ParserFactory()

    def test_a_TXTParser_should_be_returned_when_a_text_file_parser_is_requested(self):
        self.assertIsInstance(self.parser_factory.get_parser('.txt'), TXTParser)

    def test_a_CSVParser_should_be_returned_when_a_csv_file_parser_is_requested(self):
        self.assertIsInstance(self.parser_factory.get_parser('.csv'), CSVParser)
             
    def test_a_CommandLineParser_should_be_returned_when_the_parameter_is_not_sudoku_file(self):
        puzzle_param = '067040002900730450405000000600080000000900320283500649070000003000657804006423597'
        self.assertIsInstance(self.parser_factory.get_parser(puzzle_param), CommandLineParser)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()