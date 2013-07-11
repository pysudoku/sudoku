#-------------------------------------------------------------------------------
# Name:        writerFactory
# Purpose:
#
# Author:      Ines Baina
#
# Created:     04/07/2013
# Copyright:   (c) Ines Baina 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from sudoku.writer.writerType import WriterType
from sudoku.writer.writerCSV import WriterCSV
from sudoku.writer.writerTXT import WriterTXT
from sudoku.writer.displayCMD import DisplayCMD

class WriterFactory(object):
    '''
    classdocs
    '''


    def __init__(self, settings):
        '''
        Constructor
        '''
        self.settings = settings
    
    def getWriter(self):
        if(self.settings == WriterType.TXT):
            return WriterTXT()
        if(self.settings == WriterType.CSV):
            return WriterCSV()
        
        if(self.settings == WriterType.CONSOLE):
            return DisplayCMD()
        