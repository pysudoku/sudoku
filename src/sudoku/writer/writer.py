#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Ines Baina
#
# Created:     04/07/2013
# Copyright:   (c) Ines Baina 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from abc import abstractmethod

class Writer(object):

    @abstractmethod
    def write(self,sudoku,filename_user):
        """
        Write abstract method
        """
