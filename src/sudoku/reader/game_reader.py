'''
Created on Jul 23, 2013

@author: Administrator
'''
import pickle
import os
from contextlib import contextmanager
from sudoku.reader.exception.fileformaterror import FileFormatError

class SudokuGameReader:
    '''
    Reads a Sudoku game file.
    '''

    extension = '.sgf'
    
    def read_game(self, file_name):
        '''
        Reads a Sudoku game file and returns a Sudoku game object.
        @param file_name: the name of the file.
        '''
        directory, name, extension = self._split_file_name(file_name)
        extension = self.extension if extension == '' else extension
        file_name = directory + os.sep + name + extension              
        
        if not file_name.endswith(self.extension):
            raise FileFormatError("Invalid file format. '{}' file expected.".format(self.extension))
        with self.open_sudoku_file(file_name, 'rb') as (input_file, error):
            if error:
                raise error
            else:
                return pickle.load(input_file)

    @contextmanager
    def open_sudoku_file(self, file_name, mode = 'r'):
        '''
        Opens a file using a context manager.
        @param file_name: the name of the file.
        @param mode: the mode used to open the file.
        '''
        try:
            puzzle_file = open(file_name, mode)
        except IOError as e:
            yield None, e
        else:
            try:
                yield puzzle_file, None
            finally:
                puzzle_file.close()
                
    def _split_file_name(self, file_name):
        '''
        Returns a tuple containing the directory, name, and extension of the given file name.
        @param file_name: the name of the file
        '''
        (directory, file) = os.path.split(os.path.normpath(os.path.realpath(file_name)))
        (name, extension) = os.path.splitext(os.path.basename(file))
        return directory, name, extension
