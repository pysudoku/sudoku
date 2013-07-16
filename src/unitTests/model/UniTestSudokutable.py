'''
Created on Jun 30, 2013

@author: Jimena Terceros
'''
import unittest
from sudoku.model.sudokutable import Sudoku_Table
from sudoku.model.exception.Invalid_row_exception import Invalid_row_exception
from sudoku.model.exception.Invalid_column_exception import Invalid_column_exception
from sudoku.model.exception.CellNotEditableException import CellNotEditableException
from sudoku.model.exception.InvalidParameterValueException import InvalidParameterValueException
from sudoku.model.exception.Invalid_dictionary_size_exception import Invalid_dictionary_size_exception

class TestSudokuTable(unittest.TestCase):

    def setUp(self):
        self.onedata = {"A1":6}
        self.dic_with_data = {"A1":1, "A2":3, "A3":1, "B1":0, "B2":2, "B3":0, "C1":2, "C2":1, "C3":3}
        self.emptydic = {"A1":0, "A2":0, "A3":0, "B1":0, "B2":0, "B3":0, "C1":0, "C2":0, "C3":0}
        self.dic_with_invalid_values = {"A1":0, "A2":5, "A3":6, "B1":0, "B2":9, "B3":1, "C1":0, "C2":9, "C3":8}

    def ifASukokuTableIsCreatedThenTheDictionaryStructureShouldHaveTheRightSizeOfRecordsWithDefaultInformation(self):
        sudoku = Sudoku_Table(3)
        
        self.assertEqual(3, sudoku.size)
        self.assertEqual(9, len(sudoku.dic))
        
        cols = [1, 2, 3]
        rows = ['A', 'B', 'C']
        
        for row in rows:
            for col in cols:
                cell = sudoku.getCell(row, col)
                value = cell.get_value()
                editable = cell.iseditable()
                self.assertEqual(0, value)
                self.assertTrue(editable)
    
    def testIfTableIsCreatedByDefaultThenShouldHaveSize9AndShouldHave81Cells(self):
        sudoku = Sudoku_Table()
        
        self.assertEqual(9, sudoku.size)
        self.assertEqual(81, len(sudoku.dic))
    
    def testIfTableisCreatedWithSizeParameterThenShouldHaveTheRightSizeAndCellNumber(self):
        sudoku = Sudoku_Table(18)
        
        self.assertEqual(18, sudoku.size)
        self.assertEqual(18*18, len(sudoku.dic)) 
    
    def testIfTryToAddDataInRightCellThenShouldAddTheDataProperly(self):
        sudoku = Sudoku_Table(18)
        sudoku.set_value('B', 2, 5)
        
        self.assertEqual(5, sudoku.dic['B2'].get_value())
    
    def testIfTryToUpdateDataInAnInvalidRowThenShouldTrowAnException(self):
        sudoku = Sudoku_Table()
        try:
            sudoku.set_value('J', 2, 5)
            self.fail("Did not raise the exception Invalid_row_exception")
        except Invalid_row_exception:
            pass

    def testIfTryToUpdateDataInAnInvalidColumnThenShouldTrowAnException(self):
        sudoku = Sudoku_Table()
        try:
            sudoku.set_value('A', 10, 5)
            self.fail("Did not raise the exception Invalid_column_exception")
        except Invalid_column_exception:
            pass
    
    def testIfTryToFindDataInRightCellThenShouldFindTheCorrectData(self):
        sudoku = Sudoku_Table(3)
        sudoku.dic['C2'].set_value(4)
        value = sudoku.get_value('C', 2)
        self.assertEqual(4, value)
    
    def testIfTryToFindDataFromInvalidRowThenShouldTrowAnException(self):
        sudoku = Sudoku_Table(3)
        try:
            sudoku.get_value('D', 2)
            self.fail("Did not raise the exception Invalid_row_exception")
        except Invalid_row_exception:
            pass
    
    def testIfTryToFindDataFromInvalidColumnThenShouldTrowAnException(self):
        sudoku = Sudoku_Table(3)
        try:
            sudoku.get_value('C', 4)
            self.fail("Did not raise the exception Invalid_column_exception")
        except Invalid_column_exception:
            pass
    
    def testWhenTrySetDataInCorrectAndEditableCellThenShouldSetDataProperly(self):
        sudoku = Sudoku_Table(3)
        sudoku.set_value('C', 2, 2)
        self.assertEqual(2, sudoku.dic['C2'].get_value())
    
    def testWhenTrySetDateInCorrectAndNonEditableCellThenShouldThrownAnException(self):
        sudoku = Sudoku_Table(3)
        sudoku.set_editable('C', 2, False)
        try:
            sudoku.set_value('C', 2, 2)
            self.fail("Did not raise the exception CellNotEditableException")
        except CellNotEditableException:
            pass
        
    def testWhenTryToSetAnInvalidValueThehnShouldRaiseanException(self):
        sudoku = Sudoku_Table(3)
        try:
            sudoku.set_value('C', 2, 5)
            self.fail("Did not raise the exception InvalidParameterValueException")
        except InvalidParameterValueException:
            pass
    
    def test_given_a_valid_dictionary_then_should_convert_it_to_sudoku_table(self):
        sudoku = Sudoku_Table(3)
        sudoku.from_dictionary(self.dic_with_data)
        
        rows = ['A', 'B', 'C']
        cols = range(1, 4)
        
        self.assertEqual(len(self.dic_with_data), len(sudoku.dic))
        
        for row in rows:
            for col in cols:
                self.assertEqual(self.dic_with_data[row + str(col)], sudoku.get_value(row, col))
                
    def test_given_an_invalid_dictionary_size_then_should_raise_an_exception(self):
        sudoku = Sudoku_Table()
        
        try:
            sudoku.from_dictionary(self.dic_with_data)
            self.fail("Did not raise the exception Invalid_dictionary_size_exception")
        except Invalid_dictionary_size_exception:
            pass
        
    def test_given_a_dictionary_with_invalid_values_then_should_raise_an_exception(self):
        sudoku = Sudoku_Table(3)
        
        try:
            sudoku.from_dictionary(self.dic_with_invalid_values)
            self.fail("Did not raise the exception InvalidParameterValueException")
        except InvalidParameterValueException:
            pass
        
    def test_given_a_sudoku_table_then_should_convert_it_to_dictionary(self):
        sudoku = Sudoku_Table(3)
        rows = ['A', 'B', 'C']
        cols = range(1, 4)
        for row in rows:
            for col in cols:
                sudoku.set_value(row, col, self.dic_with_data[row + str(col)])
                
        dictionary = sudoku.to_dictionary()
        self.assertDictEqual(self.dic_with_data, dictionary)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()