'''
Created on Jul 23, 2013

@author: Administrator
'''
import pickle
import time
import datetime
import os

from contextlib import contextmanager

class SudokuGameWriter:
    '''
    Writes a Sudoku game to a Sudoku game file
    '''
    extension = '.sgf'
    
    def write(self, game, file_name):
        '''
        Writes a Sudoku game object to a Sudoku game file.
        @param game: the Sudoku game object.
        @param file_name: the name of the file.
        '''
        directory, name, extension = self._split_file_name(file_name)
        file_name = file_name + self.extension if extension == '' else file_name            
        timestamp_suffix = self._get_timestamp_sufix() if os.path.isfile(file_name) else ''            
        file_name = directory + os.sep + name + timestamp_suffix + self.extension
        
        with self.open_sudoku_file(file_name, 'wb') as (output_file, error):
            if error:
                raise error
            else:
                pickle.dump(game, output_file, pickle.HIGHEST_PROTOCOL)
        return file_name
                
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
                
    def _get_timestamp_sufix(self):
        '''
        Returns timestamp string to be append to the name of the file.
        '''
        return datetime.datetime.fromtimestamp(time.time()).strftime('-%Y%m%d%H%M%S')
    
    def _split_file_name(self, file_name):
        '''
        Returns a tuple containing the directory, name, and extension of the given file name.
        @param file_name: the name of the file
        '''        
        (directory, file) = os.path.split(os.path.normpath(os.path.realpath(file_name)))
        (name, extension) = os.path.splitext(os.path.basename(file))
        return directory, name, extension
