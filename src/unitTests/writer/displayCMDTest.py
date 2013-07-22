#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Ines Baina
#
# Created:     08/07/2013
# Copyright:   (c) Ines Baina 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import unittest
from sudoku.writer.displayCMD import DisplayCMD

class TestDisplayCMD(unittest.TestCase):
    def setUp(self):
        self.displayCMD=DisplayCMD()

    def test_if_sudoku_solved_is_displayed_in_cmd_method_should_return_True(self):
        sudokusolved={
            "A1":'1', "A2":'6', "A3":'7', "A4":'8', "A5":'4', "A6":'5', "A7":'9', "A8":'3', "A9":'2',
            "B1":'9', "B2":'2', "B3":'8', "B4":'7', "B5":'3', "B6":'6', "B7":'4', "B8":'5', "B9":'1',
            "C1":'4', "C2":'3', "C3":'5', "C4":'2', "C5":'1', "C6":'9', "C7":'7', "C8":'8', "C9":'6',
            "D1":'6', "D2":'4', "D3":'9', "D4":'3', "D5":'8', "D6":'2', "D7":'1', "D8":'7', "D9":'5',
            "E1":'7', "E2":'5', "E3":'1', "E4":'9', "E5":'6', "E6":'4', "E7":'3', "E8":'2', "E9":'8',
            "F1":'2', "F2":'8', "F3":'3', "F4":'5', "F5":'7', "F6":'1', "F7":'6', "F8":'4', "F9":'9',
            "G1":'5', "G2":'7', "G3":'4', "G4":'1', "G5":'9', "G6":'8', "G7":'2', "G8":'6', "G9":'3',
            "H1":'3', "H2":'9', "H3":'2', "H4":'6', "H5":'5', "H6":'7', "H7":'8', "H8":'1', "H9":'4',
            "I1":'8', "I2":'1', "I3":'6', "I4":'4', "I5":'2', "I6":'3', "I7":'5', "I8":'9', "I9":'7'
            }

        self.assertTrue(self.displayCMD.display(sudokusolved))

if __name__ == '__main__':
    unittest.main()