'''
Created on Jun 29, 2013

@author: Jimena Terceros
'''
from sudoku.model.exception.CellNotEditableException import CellNotEditableException

class cell:
    '''
    Creating this class, we are creating cell of the sudoku table that has the following parameters 
    '''

    def __init__(self, val = 0, edit = True):
        '''
        Constructor.
        @param val: parameter means the value of the cell it can go from 0 to 9 in a sudoku of 9 x 9
        @param edit: parameter means that the cell is editable by default 
        '''
        self.value = val
        self.edit = edit
        
    def set_value(self, value):
        '''
        Sets the value attribute.
        @param value: the value for value attribute.
        @raise CellNotEditableException: when try to set value in a non editable cell. 
        '''
        if not self.isEdit():
            raise CellNotEditableException()
        self.value = value
            
    def get_value(self):
        '''
        Gets the value attribute
        @return the value.
        '''
        return self.value
    
    def isEdit(self):
        '''
        Verify if the edit attribute is editable
        @param edit: the value for edit attribute
        '''
        return self.edit
    
    def set_editable(self, editable):
        '''
        Sets the value of the editable attribute
        @param editable: the value for editable attribute 
        '''
        self.edit = editable