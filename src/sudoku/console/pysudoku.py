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
import sys
import getopt
import time
sys.path.append("../../../src")

from sudoku.algorithm.AlgorithmFactory import AlgorithmFactory
from sudoku.algorithm.AlgorithmType import AlgorithmType
from sudoku.writer.writer import Writer
from sudoku.writer.writerCSV import WriterCSV 
from sudoku.writer.writerTXT import WriterTXT
from sudoku.writer.displayCMD import DisplayCMD
from sudoku.reader.txtparser import TXTParser
from sudoku.reader.csvparser import CSVParser
from sudoku.reader.commandlineparser import CommandLineParser
from sudoku.settings.SettingsReader import SettingsReader


class PySudoku(object):
    '''
    classdocs
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
    def validate_input(self,inputfile_user,inputfilepath_user):
        if inputfile_user=="TXT": 
            reader=TXTParser()
            grid=reader.parse_puzzle(inputfilepath_user)
        if inputfile_user=="CSV": 
            reader=CSVParser()
            grid=reader.parse_puzzle(inputfilepath_user)
        if inputfile_user=="CONSOLE": 
            reader=CommandLineParser()
            grid=reader.parse_puzzle(inputfilepath_user)
        
        return grid
    def print_solution(self,solution,typeOutput,path):
        
        if typeOutput=="Console":
            writer=DisplayCMD()
            writer.display(solution)
        if typeOutput=="file":
            writer=WriterTXT()
            writer.write(solution,path)
    def factory_solution(self,factory,grid_parsed):
        alg = factory.getAlgorithm()
        solution = alg.solve(grid_parsed)
        return solution
            
    def calculate_time(self,endTime,startTime):
            duration = endTime - startTime
            print( "Found solution in seconds: %f"%( duration ))
                
    def solve_sudoku(self,inputfile,inputfilepath,settingsfilepath):
        
        algorithm_toSolve=''     
        grid_parsed= self.validate_input(inputfile, inputfilepath)
        config=SettingsReader()    
        configSettings=config.read(settingsfilepath)
        algorithm_toSolve=configSettings.getAlgorithmName()
        typeOutput=configSettings.getOutputType()
        path=configSettings.getPath()
        startTime = time.time()
        
        print(algorithm_toSolve)     
                    
        if algorithm_toSolve=="PETER_NORVIG":
            factory = AlgorithmFactory(AlgorithmType.PETER_NORVIG)
            solution=self.factory_solution(factory,grid_parsed)
            self.print_solution(solution,typeOutput,path)
            self.calculate_time(time.time(),startTime)
            
        if algorithm_toSolve=="BACK_TRACKING":
            factory = AlgorithmFactory(AlgorithmType.BACK_TRACKING)
            solution=self.factory_solution(factory,grid_parsed)
            self.print_solution(solution,typeOutput,path)
            self.calculate_time(time.time(),startTime)
               
        if algorithm_toSolve=="RECURSIVE":
            factory = AlgorithmFactory(AlgorithmType.RECURSIVE)
            solution=self.factory_solution(factory,grid_parsed)
            self.print_solution(solution,typeOutput,path)
            self.calculate_time(time.time(),startTime)
            

        def generate_sudoku(): 
           pass
       