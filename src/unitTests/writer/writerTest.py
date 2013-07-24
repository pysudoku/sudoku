#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      Ines Baina
#
# Created:     04/07/2013
# Copyright:   (c) Ines Baina 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import unittest
from coverage import coverage
from sudoku.writer.writer import Writer
from sudoku.writer.writerTXT import WriterTXT
from sudoku.writer.writerCSV import WriterCSV


class TestWriter(unittest.TestCase):
    def setUp(self):
        pass

    

    def test_to_verify_if_write_method_in_writerTXT_create_a_fileTXT(self):
        sudoku = {
            "A1":'.', "A2":'6', "A3":'7', "A4":'6', "A5":'4', "A6":'.', "A7":'.', "A8":'.', "A9":'2',
            "B1":'9', "B2":'.', "B3":'.', "B4":'7', "B5":'3', "B6":'.', "B7":'4', "B8":'5', "B9":'.',
            "C1":'4', "C2":'.', "C3":'5', "C4":'.', "C5":'.', "C6":'.', "C7":'.', "C8":'.', "C9":'.',
            "D1":'6', "D2":'.', "D3":'.', "D4":'.', "D5":'8', "D6":'.', "D7":'.', "D8":'.', "D9":'.',
            "E1":'.', "E2":'.', "E3":'.', "E4":'9', "E5":'.', "E6":'.', "E7":'3', "E8":'2', "E9":'.',
            "F1":'2', "F2":'8', "F3":'3', "F4":'5', "F5":'.', "F6":'.', "F7":'6', "F8":'4', "F9":'9',
            "G1":'.', "G2":'7', "G3":'.', "G4":'.', "G5":'.', "G6":'.', "G7":'.', "G8":'.', "G9":'3',
            "H1":'.', "H2":'.', "H3":'.', "H4":'6', "H5":'5', "H6":'7', "H7":'8', "H8":'.', "H9":'4',
            "I1":'.', "I2":'.', "I3":'6', "I4":'4', "I5":'2', "I6":'3', "I7":'5', "I8":'9', "I9":'7'
            }
        writer = WriterTXT()

        writer.write(sudoku, "file2.txt")
        
        exist = False
        for file in os.listdir("."):
            if file == "file2.txt":
                exist = True
        self.assertEqual(True, exist)

    def test_to_verify_if_write_method_in_writerCSV_create_a_fileCSV(self):
        sudoku = {
            "A1":'.', "A2":'6', "A3":'7', "A4":'6', "A5":'4', "A6":'.', "A7":'.', "A8":'.', "A9":'2',
            "B1":'9', "B2":'.', "B3":'.', "B4":'7', "B5":'3', "B6":'.', "B7":'4', "B8":'5', "B9":'.',
            "C1":'4', "C2":'.', "C3":'5', "C4":'.', "C5":'.', "C6":'.', "C7":'.', "C8":'.', "C9":'.',
            "D1":'6', "D2":'.', "D3":'.', "D4":'.', "D5":'8', "D6":'.', "D7":'.', "D8":'.', "D9":'.',
            "E1":'.', "E2":'.', "E3":'.', "E4":'9', "E5":'.', "E6":'.', "E7":'3', "E8":'2', "E9":'.',
            "F1":'2', "F2":'8', "F3":'3', "F4":'5', "F5":'.', "F6":'.', "F7":'6', "F8":'4', "F9":'9',
            "G1":'.', "G2":'7', "G3":'.', "G4":'.', "G5":'.', "G6":'.', "G7":'.', "G8":'.', "G9":'3',
            "H1":'.', "H2":'.', "H3":'.', "H4":'6', "H5":'5', "H6":'7', "H7":'8', "H8":'.', "H9":'4',
            "I1":'.', "I2":'.', "I3":'6', "I4":'4', "I5":'2', "I6":'3', "I7":'5', "I8":'9', "I9":'7'
            }
        writer = WriterCSV()

        writer.write(sudoku, "file3.csv")
        exist = False
        for file in os.listdir("."):
            if file == "file3.csv":
                exist = True
        self.assertEqual(True, exist)


    def test_to_verify_if_exist_write_method_for_TXT(self):
        sudoku = {
            "A1":'.', "A2":'6', "A3":'7', "A4":'6', "A5":'4', "A6":'.', "A7":'.', "A8":'.', "A9":'2',
            "B1":'9', "B2":'.', "B3":'.', "B4":'7', "B5":'3', "B6":'.', "B7":'4', "B8":'5', "B9":'.',
            "C1":'4', "C2":'.', "C3":'5', "C4":'.', "C5":'.', "C6":'.', "C7":'.', "C8":'.', "C9":'.',
            "D1":'6', "D2":'.', "D3":'.', "D4":'.', "D5":'8', "D6":'.', "D7":'.', "D8":'.', "D9":'.',
            "E1":'.', "E2":'.', "E3":'.', "E4":'9', "E5":'.', "E6":'.', "E7":'3', "E8":'2', "E9":'.',
            "F1":'2', "F2":'8', "F3":'3', "F4":'5', "F5":'.', "F6":'.', "F7":'6', "F8":'4', "F9":'9',
            "G1":'.', "G2":'7', "G3":'.', "G4":'.', "G5":'.', "G6":'.', "G7":'.', "G8":'.', "G9":'3',
            "H1":'.', "H2":'.', "H3":'.', "H4":'6', "H5":'5', "H6":'7', "H7":'8', "H8":'.', "H9":'4',
            "I1":'.', "I2":'.', "I3":'6', "I4":'4', "I5":'2', "I6":'3', "I7":'5', "I8":'9', "I9":'7'
            }
        writer = WriterTXT()
        self.assertTrue(writer.write(sudoku, "file.txt"))
    def test_to_verify_if_exist_write_method_for_CSV(self):
        sudoku = {
            "A1":'.', "A2":'6', "A3":'7', "A4":'6', "A5":'4', "A6":'.', "A7":'.', "A8":'.', "A9":'2',
            "B1":'9', "B2":'.', "B3":'.', "B4":'7', "B5":'3', "B6":'.', "B7":'4', "B8":'5', "B9":'.',
            "C1":'4', "C2":'.', "C3":'5', "C4":'.', "C5":'.', "C6":'.', "C7":'.', "C8":'.', "C9":'.',
            "D1":'6', "D2":'.', "D3":'.', "D4":'.', "D5":'8', "D6":'.', "D7":'.', "D8":'.', "D9":'.',
            "E1":'.', "E2":'.', "E3":'.', "E4":'9', "E5":'.', "E6":'.', "E7":'3', "E8":'2', "E9":'.',
            "F1":'2', "F2":'8', "F3":'3', "F4":'5', "F5":'.', "F6":'.', "F7":'6', "F8":'4', "F9":'9',
            "G1":'.', "G2":'7', "G3":'.', "G4":'.', "G5":'.', "G6":'.', "G7":'.', "G8":'.', "G9":'3',
            "H1":'.', "H2":'.', "H3":'.', "H4":'6', "H5":'5', "H6":'7', "H7":'8', "H8":'.', "H9":'4',
            "I1":'.', "I2":'.', "I3":'6', "I4":'4', "I5":'2', "I6":'3', "I7":'5', "I8":'9', "I9":'7'
            }
        writer = WriterCSV()
        self.assertTrue(writer.write(sudoku, "filec.csv"))
         
    def tearDown(self):
        if os.path.isfile("file2.txt"):
            os.remove("file2.txt")
        if os.path.isfile("file.txt"):
            os.remove("file.txt")
        if os.path.isfile("file3.csv"):
            os.remove("file3.csv")
        if os.path.isfile("filec.csv"):
            os.remove("filec.csv")       

if __name__ == '__main__':

    unittest.main()
