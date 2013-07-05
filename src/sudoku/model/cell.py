'''
Created on Jun 29, 2013

@author: Jimena Terceros
'''
from sudoku.model.exception.InvalidParameterValueException import InvalidParameterValueException
from sudoku.model.exception.CellNotEditableException import CellNotEditableException

class cell:
    '''
    classdocs
    '''
    value = 0
    edit = True

    def __init__(self, val = 0, edit = True):
        '''
        Constructor.
        @param val:
        @param edit: 
        '''
        self.setValue(val)
        self.edit = edit
        
    def setValue(self, value):
        if not self.isEdit():
            raise CellNotEditableException()
        if value < 0 or value > 9:
            raise InvalidParameterValueException("value")
        else:
            self.value = value
            
    def getValue(self):
        return self.value
    
    def isEdit(self):
        return self.edit