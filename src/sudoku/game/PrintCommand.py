'''
Created on Jul 18, 2013

@author: Ines Baina
'''
from sudoku.game.SudokuCommand import SudokuCommand
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException

class PrintBoardCommand(SudokuCommand):
    '''
    PrintBoardCommand class prints the sudoku game in console
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        SudokuCommand.__init__(self, params)
    
    def execute(self):
        '''
        Print the sudoku table in console
        '''
        if self.game == None:
            raise InvalidCmdParametersException("The command needs a game.")
        elif self.game.user_sudoku == None:
            raise InvalidCmdParametersException("The Sudoku was not loaded.")
                
        self.write(self.game.user_sudoku.to_dictionary())
        
        
    def validate(self):
        '''
        Validate number of parameters and the parameter of the command
        '''
        self.validate_needed_parameters()
 
 
    def write(self,sudoku):
        '''
        Receives a sudoku as string and print in console as a table 
        '''
        print(" SUDOKU GAME ")
                
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

            print (cadena+"\n")
            counter+=1
            if counter==3 or counter==6:
                print (barra+"\n")
                
                
    row_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I']
    column_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def dict_to_str(self, grid):
        '''Takes a dictionary representation of a sudoku puzzle and returns a
        string representation.'''
        string_representation = ''
        for row in self.row_labels:
            for column in self.column_labels:
                string_representation += '.' if grid[row + column] == 0 else str(grid[row + column])
        return string_representation         
              