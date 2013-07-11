#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      Ines Baina
#
# Created:     04/07/2013
# Copyright:   (c) Ines Baina 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from sudoku.writer.writer import Writer
import os.path
import datetime
import time
import string

class WriterTXT(Writer):
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
        
            
    def write(self,sudoku,filename_user):
        
        # c:/sudoku>exe d:/sudoku/sud.txt  ---output d:/sudoku/sud.txt
        # c:/sudoku>exe sud.txt ---output c:/sudoku/sud.txt
        
        if os.path.isfile(filename_user):
            #file exists then rename it
            new_file = open(self.createNewFilename(filename_user), 'w')
            
        else:
            #file does not exist, lets create it
            new_file = open(filename_user, 'w')
        
        str_result = self.dict_to_str(sudoku)
        barra=""
        for i in range(0,8):
            barra += "·---"

        n=9
        rownumbers=[str_result[i:i+n]for i in range(0, len(str_result), n)]

        counter=0
        for row in rownumbers:
            cadena=""
            block= ('|'.join([row[i:i+3] for i in range(0, len(row), 3)]))
            for number in block:
                cadena += " "+ number + " "

            new_file.write (cadena+"\n")
            counter+=1
            if counter==3 or counter==6:
                new_file.write (barra+"\n")

        new_file.close()
        return True

    def createNewFilename(self, filename_user):
        now = datetime.datetime.now()
        now=now.replace(microsecond=0)
        now=now.strftime("%B %d, %Y")
        ticks = time.time()

        stringname=now+str(ticks)
        str.translate(stringname, ',.')
        for c in string.punctuation:
            stringname= stringname.replace(c,"")
        stringname=stringname+".txt"
        
        path = os.path.dirname(filename_user)
        
        return path + "\\" + stringname


