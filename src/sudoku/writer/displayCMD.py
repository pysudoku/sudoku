#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ines Baina
#
# Created:     08/07/2013
# Copyright:   (c) Ines Baina 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import collections
class DisplayCMD:
    def __init__(self):
        pass
    row_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I']
    column_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def dict_to_str(self, grid):
        '''Takes a dictionary representation of a sudoku puzzle and returns a
        string representation.'''
        string_representation = ''
        for row in self.row_labels:
            for column in self.column_labels:
                string_representation += '.' if grid[row + column] == '.' else grid[row + column]
        return string_representation

    def display (self, sudokusolved):
        """display is a function to display and asign the sudoku solved

        @param dict_result: will contain the sudoku solved in a dictionary structure
        @param sudoku:
        @param asignadas:

        @return: a dictionary with the sudoku solved where the Key is the Row and column of sudokugame and Value is the number asigned to solve sudoku
        """
        barra = ""
        for i in range(0,9):
            barra += "·---"
        barra += "."

        print (barra)
        str_result = self.dict_to_str(sudokusolved)
        n=9
        rownumbers=[str_result[i:i+n]for i in range(0, len(str_result), n)]
        #print (rownumber)
        for row in rownumbers:
            cadena=""
            for number in row:
                cadena += "| "+ number + " "

            cadena += "|"
            print (cadena)
            print (barra)

        return True



