'''
Created on Jun 30, 2013

@author: Jimena Terceros
'''
from sudoku.model.cell import Cell
from sudoku.model.exception.Invalid_row_exception import InvalidRowException
from sudoku.model.exception.Invalid_column_exception import InvalidColumnException
from sudoku.model.exception.InvalidParameterValueException import InvalidParameterValueException
from sudoku.model.exception.Invalid_dictionary_size_exception import InvalidDictionarySizeException

class SudokuBoard:
    """
    Creating this class, we are creating sudoku table that has the following parameters
    """
    def __init__(self, size = 9):
        '''
        Constructor
        @param size: means the size of the sudoku table
        @param dic: mans that the data will be manage in a dictionary it is empty starting
        '''
        self.size = size
        self.dic = {}
        self.initialize()
        
    def initialize(self):
        '''
        Initialize values of columns, rows and valid values for Sudoku table
        according the Sudoku'size
        '''
        max_size = (self.size + 1)
        self.cols = range(1, max_size)
        self.rows = []
        self.valid_values = range(0, max_size)
        for r in range(0, self.size):
            self.rows.append(chr(65 + r))
            
        for r in self.rows:
            for c in self.cols:
                self.dic[r+str(c)] = Cell(0, True)
                
    def set_value(self, row, col, value):
        '''
        Sets the value attribute in the sudoku table
        @param row: the value for row attribute
        @param col: the value for column attribute
        @param value: the value for value attribute
        @raise InvalidParameterValueException: when you try to set an invalid value
        '''
        self.validate_cell(row, col)
        if not value in self.valid_values:
            raise InvalidParameterValueException("value")
        
        self.dic[row + str(col)].set_value(value)
        
    
    def get_value(self, row, col):
        '''
        Gets the value attribute of the sudoku table
        @param row: the value for row attribute
        @param col: the value for column attribute
        @return: return the value
        '''
        self.validate_cell(row, col)
        
        return self.dic[row + str(col)].get_value()
    
    def set_editable(self, row, col, editable):
        '''
        Sets the value in the editable attribute
        @param row: the value for row attribute
        @param col: the value for column attribute
        @param editable: the value for editable attribute 
        '''
        self.validate_cell(row, col)
        
        self.dic[row + str(col)].set_editable(editable)
        
    def validate_cell(self, row, col):
        '''
        Validates the value of row and the value of column 
        @param row: the value for row attribute
        @param col: the value for column attribute
        @raise InvalidRowException: when the row's value is out of the range for rows.
        @raise InvalidColumnException: when the column's value is out of the range for columns.
        '''
        if not row in self.rows:
            raise InvalidRowException()
        if not col in self.cols:
            raise InvalidColumnException()
        
    def from_dictionary(self, dictionary):
        '''
        Converts a dictionary to sudoku table where the key represents the Cell's name of the table as 'A1', 'A2',.. 
        and the value is the value that is in the Cell. 
        @param dictionary: the value for dictionary attribute 
        @raise InvalidDictionarySizeException: when try convert an invalid dictionary to sudoku table 
        '''
        if len(self.dic) != len(dictionary):
            raise InvalidDictionarySizeException()
        
        for row in self.rows:
            for col in self.cols:
                self.set_value(row, col, dictionary[row + str(col)])
                
    def to_dictionary(self):
        '''
        Converts sudoku table to a dictionary with keys that represents the Cell's name
        of the table as 'A1', 'A2', ..., and the value is the value that is in the Cell.
        '''
        dictionary = {}
        
        for row in self.rows:
            for col in self.cols:
                dictionary[row + str(col)] = self.get_value(row, col)
        
        return dictionary