'''
Created on Jul 16, 2013

@author: Ines Baina
'''

import os
import sys
import getopt
from sudoku.console.pysudoku import PySudoku


class Console(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def read_command(self):
        cmd = input("PY-SUDOKU #") 
        return cmd
    
    def parse_command(self, cmd):
        cmdSplit = cmd.split(" ")
        if len(cmdSplit) == 5:
            return cmdSplit
        return None
    
    def execute_command_solve(self, cmd):
                  
        if cmd:
            if cmd[0]=="-input" and cmd[3]=="-settings":
                try:
                    print("Execute {%s [%s][%s]%s[%s]}" %(cmd[0], cmd[1],cmd[2],cmd[3],cmd[4]))
                    new = PySudoku()
                    new.solve_sudoku(cmd[1],cmd[2],cmd[4])
                 
                except ValueError as e :
                    print ("'%s' is not a valid command." % e.args[0].split(": ")[1])
            else:
                print ("The commands are incorrect, please try again")
            
        else:
            print("The command is incorrect, please try again")
            
    def execute_command_generate(self, cmd):
        
        if cmd:
            
            print("Execute {%s [%s][%s]%s[%s]}" %(cmd[0], cmd[1],cmd[2],cmd[3],cmd[4]))
            new = PySudoku()
            new.generate_sudoku()
        else:
            print("The command is incorrect, please try again")