'''
Created on Jul 16, 2013

@author: Ines Baina
'''
import os

from sudoku.console.console import Console
from sudoku.console.playpysudoku import PlaySudokuMenu

class MainMenu(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def select_menu(self):
          
        print (30 * '-')
        print ("   M A I N - M E N U")
        print (30 * '-')
        print ("1. Solve sudoku")
        print ("2. Generate sudoku game")
        print ("3. Play Sudoku")
        print ("4. Exit")
        print (30 * '-')
 
        ###########################
        ## Robust error handling ##
        ## only accept int       ##
        ###########################
        ## Wait for valid input in while...not ###
        is_valid=0
 
        while not is_valid :
            try :
                choice = int (input("Enter your choice [1-4] : ") )
                is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
            except ValueError as e :
                print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
 
        ### Take action as per selected menu-option ###
        if choice == 1:
            print ("Commands to use: >> Help: List of all commands available to solve a sudoku and output/input type")
            
            console = Console()
            while True:
                cmd = console.read_command()
                command = console.parse_command(cmd)
                console.execute_command_solve(command)
        elif choice == 2:
            print ("Commands to use: >> Help: List of all commands available to generate a sudoku and output type")
            
            console = Console()
            while True:
                cmd = console.read_command()
                command = console.parse_command(cmd)
                console.execute_command_generate(command)
        elif choice == 3:
            print (30 * '-')
            print ("   SUDOKU - GAME   ")
            print (30 * '-')
            print ("Levels:")
            print ("   1. Basic")
            print ("   2. Intermediate")
            print ("   3. Advanced")
            print ("   4. Exit")
            print (30 * '-')
            
            is_valid=0
 
            while not is_valid :
                try :
                    choice = int (input("Enter your choice [1-4] : ") )
                    is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
                except ValueError as e :
                    print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
            ### Take action as per selected menu-option ###
            if choice == 1:
                print ("Basic sudoku")
                game = PlaySudokuMenu()
                game.select_menu()
            elif choice == 2:
                print ("Intermediate sudoku")
            elif choice == 3:
                print ("Advanced sudoku")
            elif choice == 4:
                print ("Exit...")
        elif choice == 4:
            print ("Exit...")
        else:
            print ("Invalid number. Try again...")
