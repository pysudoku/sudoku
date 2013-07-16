'''
Created on Jun 29, 2013

@author: Jimena Terceros
'''
from sudoku.model.exception.CellNotEditableException import CellNotEditableException

class Cell:
    '''
    Creating this class, we are creating Cell of the sudoku table that has the following parameters 
    '''

    def __init__(self, val = 0, editable = True):
        '''
        Constructor.
        @param val: parameter means the value of the Cell it can go from 0 to 9 in a sudoku of 9 x 9
        @param editable: parameter means that the Cell is editable by default 
        '''
        self.value = val
        self.editable = editable
        
    def set_value(self, value):
        '''
        Sets the value attribute.
        @param value: the value for value attribute.
        @raise CellNotEditableException: when try to set value in a non editable Cell. 
        '''
        if not self.is_editable():
            raise CellNotEditableException()
        self.value = value
            
    def get_value(self):
        '''
        Gets the value attribute
        @return the value.
        '''
        return self.value
    
    def is_editable(self):
        '''
        Gets the value for editable attribute.
        @param editable: the value for editable attribute
        '''
        return self.editable
    
    def set_editable(self, editable):
        '''
        Sets the value of the editable attribute
        @param editable: the value for editable attribute 
        '''
        self.editable = editable