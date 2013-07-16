'''
Created on Jun 29, 2013

@author: Jimena Terceros
'''
import unittest
from sudoku.model.cell import cell
from sudoku.model.exception.CellNotEditableException import CellNotEditableException

class TestCell(unittest.TestCase):


    def setUp(self):
        self.validValue = 2
        self.invalidValue = 51
        self.defaultCell = cell()
        self.validCell = cell(self.validValue, False)
        self.validCellEdit = cell(self.validValue, True)

    def testIfThereIsNotParametersInTheCellThenshouldSetDefaultParametersTotheCell(self):
        self.assertEqual(0, self.defaultCell.value)
        self.assertEqual(True, self.defaultCell.edit)

    def testIfTheCellHasParametersThenshouldSetTheValuesProperly(self):
        self.assertEqual(self.validValue, self.validCell.value)
        self.assertEqual(False, self.validCell.edit)
    
    def testIfTryToSetValueWithAValidParameterWhenTheCellIsEditableThenShouldSetTheValueProperly(self):
        self.validCellEdit.set_value(self.validValue)
        self.assertEqual(self.validValue, self.validCellEdit.value)
    
    def testIfTryToSetValueWhenTheCellIsNotEditableThenShouldTrowAnException(self):
        try:
            self.validCell.set_value(9)
            self.fail("Didn't raise InvalidCellNotEditableException")
        except CellNotEditableException:
            self.assertEqual(self.validValue, self.validCellEdit.value)
    
    def testIfThParameterValueInTheCellHasAValidValueThenGetTheSameValue(self):
        value = self.validCellEdit.get_value()
        self.assertEqual(self.validValue, value)
    
    def testifCellIsEditableThenIsEditshouldReturnTrue(self):
        self.assertTrue(self.validCellEdit.isEdit())
    
    def testifCellIsNotEditableThenIsEditshouldReturnFalse(self):
        self.assertFalse(self.validCell.isEdit())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()