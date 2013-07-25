#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ines Baina
#
# Created:     09/07/2013
# Copyright:   (c) Ines Baina 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from sudoku.writer.writer import Writer
import os.path
import datetime
import time
import string

class WriterCSV(Writer):
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
                string_representation += '0' if grid[row + column] == '.' else grid[row + column]
        return string_representation
    
    def write(self,sudoku,filename_user):
        if os.path.isfile(filename_user):
            #file exists then create it
            new_file = open(self.createNewFilename(filename_user), 'w')
        else:
            #file does  exist, lets open it
            new_file = open(filename_user, 'w')
            
        str_result = self.dict_to_str(sudoku)
        n=9
        rownumbers=[str_result[i:i+n]for i in range(0, len(str_result), n)]

        for row in rownumbers:
            cadena=""
            for number in row:
                cadena += number + " "
            new_file.write(cadena+",")


        new_file.close()
        return True

    def createNewFilename(self, filename_user):
        
        name_copied_file = os.path.basename(filename_user)
        os.path.splitext(name_copied_file)
        name_copied_file = os.path.splitext(name_copied_file)[0]
        
        ticks = time.time()
        stringname=str(ticks)
        str.translate(stringname, ',.')
        for c in string.punctuation:
            stringname = stringname.replace(c,"")
        
        stringname = stringname + ".csv"
        path = os.path.dirname(filename_user)
        name_file = path +"\\"+ name_copied_file +"_" + stringname

        return name_file


    