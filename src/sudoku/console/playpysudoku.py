'''
Created on Jul 16, 2013

@author: Ines Baina
'''
import os


class PlaySudokuMenu(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    sudoku= {
            "A1":'.', "A2":'8', "A3":'.', "A4":'7', "A5":'.', "A6":'4', "A7":'.', "A8":'.', "A9":'.',
            "B1":'9', "B2":'.', "B3":'4', "B4":'.', "B5":'.', "B6":'.', "B7":'6', "B8":'.', "B9":'8',
            "C1":'7', "C2":'.', "C3":'6', "C4":'.', "C5":'8', "C6":'.', "C7":'.', "C8":'.', "C9":'.',
            "D1":'.', "D2":'.', "D3":'.', "D4":'2', "D5":'.', "D6":'8', "D7":'.', "D8":'6', "D9":'5',
            "E1":'.', "E2":'9', "E3":'2', "E4":'.', "E5":'4', "E6":'7', "E7":'.', "E8":'.', "E9":'3',
            "F1":'.', "F2":'.', "F3":'.', "F4":'.', "F5":'.', "F6":'.', "F7":'.', "F8":'.', "F9":'.',
            "G1":'.', "G2":'.', "G3":'.', "G4":'8', "G5":'.', "G6":'.', "G7":'.', "G8":'.', "G9":'1',
            "H1":'4', "H2":'6', "H3":'5', "H4":'.', "H5":'2', "H6":'.', "H7":'.', "H8":'8', "H9":'9',
            "I1":'3', "I2":'.', "I3":'.', "I4":'.', "I5":'.', "I6":'9', "I7":'5', "I8":'.', "I9":'6'
            }
        
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
    
    def print_sudoku(self):
        str_result = self.dict_to_str(self.sudoku)
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

            print (cadena+"\n")
            counter+=1
            if counter==3 or counter==6:
                print (barra+"\n")
                
                
    def select_menu(self):
          
        print (30 * '-')
        print ("   S U D O K U - G A M E   ")
        print (30 * '-')
       # print (Timer)
        print ("1. Remove value")
        print ("2. Hints")
        print ("3. Pause")
        print ("4. Restart")
        print ("5. Solve")
        print ("6. Exit")
        print (30 * '-')
 
        ###########################
        ## Robust error handling ##
        ## only accept int       ##
        ###########################
        ## Wait for valid input in while...not ###
        is_valid=0
 
        while not is_valid :
            self.print_sudoku()
            try :
                choice = int (input("Enter your choice [1-6] : ") )
                is_valid = 1 ## set it to 1 to validate input and to terminate the while..not loop
            except ValueError as e :
                print ("'%s' is not a valid integer." % e.args[0].split(": ")[1])
 
        ### Take action as per selected menu-option ###
        if choice == 1:
            print ("Remove value")
            
        elif choice == 2:
            print ("Hints")
            
        elif choice == 3:
            print ("Pause")
            
        elif choice == 4:
            print ("Restart")
            
        elif choice == 5:
            print ("Solve")
            
        elif choice == 6:
            print ("Exit")
        else:
            print ("Invalid number. Try again...")
