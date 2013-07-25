'''
Created on Jul 16, 2013

@author: Ines Baina
'''

import os
import sys
import getopt

from sudoku.game.Game import Game
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.model.exception.CellNotEditableException import CellNotEditableException
from sudoku.settings.SettingsManager import SettingsManager
from sudoku.generator.generator import Generator
from sudoku.game.CommandFactory import CommandFactory

class Console(object):
    '''
    Console class is defining console to receive an input from user
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.settings_manager = SettingsManager('mySettings.xml')
        self.settings_manager.load()
        self.generator = Generator()
        self.game = Game()
        self.game.set_settings_manager(self.settings_manager)
        self.game.set_game_generator(self.generator)
        self.factory = CommandFactory(self.game)
        
        
   
    def read_command(self):
        '''
        Read_command function reads the user command input
        '''
        cmd = input("PY-SUDOKU #") 
        return cmd
    
    def parse_parameter(self, paramStr, params):
        '''
        Parse_parameter function verifies if a parameter and its value is correct.
        If the parameter is correct then it is saved in params dictionary with the paramName as key and paramValue as value.
        
        '''
        #verify is correct
        if paramStr[0] != '/':
            raise  InvalidCmdParametersException("The parameter doesn't contain / character.")
        
        paramSplit = paramStr.split("=")
        if len(paramSplit) != 2:
            raise InvalidCmdParametersException("The parameter doesn't contain = character.")
        paramName = paramSplit[0][1:]
        paramValue = paramSplit[1]
        
        params[paramName] = paramValue
        return params    
    
    def parse_command(self, cmd):
        '''
        Parse_command function verifies if a command is correct.
        The entire string of user is split in commands and parameters. Only the Command is returned.
        '''
        cmdSplit = cmd.split(" ")
        
        if len(cmdSplit) > 0:
            cmdName = cmdSplit[0]
            params = {}
            
            for param in cmdSplit[1:]:
                try:
                    self.parse_parameter(param, params)
                except:
                    return None
            if params=={}:
                params=None
                    
            #generate command
            try:
                cmd = self.factory.getCommand(cmdName, params)
            except :
                raise InvalidCmdParametersException("The command is not valid.")
                #return None
            return cmd 
                
    def execute_command(self, cmd):
        '''
        Execute_command function execute a command given by user
        '''
        if cmd: 
            response = cmd.execute()
            if response:
                print(response)
            
        else:
            print("The command is incorrect, please try again")
            
    def run(self):
        '''
        Run function calls the execute_command function if command previously given by user has been parsed in a correct way.
        The sudoku game is being print every time a value or hint has been set.
        '''
        while True:
            cmdLine = self.read_command()
            print_cmd = self.parse_command("print")
            
            if not cmdLine=="":
                cmd = self.parse_command(cmdLine)
                try:
                    os.system('cls')
                    self.execute_command(cmd)
                    self.execute_command(print_cmd)
                except CellNotEditableException:
                    print("Cell is not editable!!!")
                    self.execute_command(print_cmd)
                except Exception as e:
                    print("Ooops unexpected Exception ", e)

