'''
Created on Jun 30, 2013

@author: Jimena Terceros
'''
import unittest
from sudoku.model.sudokutable import sudokutable

class Testsudoku(unittest.TestCase):

    def setUp(self):
        self.onedata = {"A1":6}
        self.dicwithdata = {"A1":1, "A2":3, "A3":5, "B1":7, "B2":8, "B3":9, "C1":2, "C2":6, "C3":4}
        self.emptydic = {"A1":0, "A2":0, "A3":0, "B1":0, "B2":0, "B3":0, "C1":0, "C2":0, "C3":0}
        self.dicmissingdata = {"A1":0, "A2":5, "A3":6, "B1":0, "B2":9, "B3":1, "C1":0, "C2":9, "C3":8}

    def ifASukokuTableIsCreatedThenTheDictionaryStructureShouldHaveTheRightSizeOfRecordsWithDefaultInformation(self):
        pass
    
    def testIfTableIsCreatedByDefaultThenShouldHaveSize9AndShouldHave81Cells(self):
        pass
    
    def testIfTableisCreatedWithSizeParameterThenShouldHaveTheRightSizeAndCellNumber(self):
        pass
    
    def testIfTryToAddDataInRightCellThenShouldAddTheDataProperly(self):
        pass
    
    def testIfTryToAddDateInAnInvalidRowThenShouldTrowAnException(self):
        pass
    
    def testIfTryToAddDateInAnInvalidColumnThenShouldTrowAnException(self):
        pass
    
    def testIfTryToUpdateDataFromRightCellThenShouldRemoveTheDataProperly(self):
        pass
    
    def testIfTryToUpdateDataFromInvalidRowThenShouldTrowAnException(self):
        pass
    
    def testIfTryToUpdateDataFromInvalidColumnThenShouldTrowAnException(self):
        pass
    
    def testIfTryToFindDataFromRightCellThenShouldFindTheCorrectData(self):
        pass
    
    def testIfTryToFindDataFromInvalidRowThenShouldTrowAnException(self):
        pass
    
    def testIfTryToFindDataFromInvalidColumnThenShouldTrowAnException(self):
        pass
    
    def testWhenTrySetDataInCorrectAndEditableCellThenShouldSetDataProperly(self):
        pass
    
    def testWhenTrySetDateInCorrectAndNonEditableCellThenShouldThrownAnException(self):
        pass
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()