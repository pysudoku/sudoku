'''
Created on Jul 22, 2013

@author: Administrator
'''
from sudoku.reader.parser_type import ParserType
from sudoku.reader.txtparser import TXTParser
from sudoku.reader.csvparser import CSVParser
from sudoku.reader.commandlineparser import CommandLineParser

class ParserFactory:
    '''
    A Sudoku parser factory that is used to create reader objects for the supported file formats 
    '''
    def get_parser(self, file_name):
        '''
        Returns a SudokuParser for the given file extension.
        @param file_name: the name of the file.
        '''
        if file_name.endswith(ParserType.TXT):
            return TXTParser()
        if file_name.endswith(ParserType.CSV):
            return CSVParser()
        else:
            return CommandLineParser()
