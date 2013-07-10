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
import sys,getopt
sys.path.append("../../src")
from sudoku.algorithm.AlgorithmFactory import AlgorithmFactory
from sudoku.algorithm.AlgorithmType import AlgorithmType
from sudoku.writer.writer import Writer
from sudoku.writer.writerCSV import WriterCSV 
from sudoku.writer.writerTXT import WriterTXT
from sudoku.writer.displayCMD import DisplayCMD


def main():
    grid = {
            "A1":'.', "A2":'6', "A3":'7', "A4":'.', "A5":'4', "A6":'.', "A7":'.', "A8":'.', "A9":'2',
            "B1":'9', "B2":'.', "B3":'.', "B4":'7', "B5":'3', "B6":'.', "B7":'4', "B8":'5', "B9":'.',
            "C1":'4', "C2":'.', "C3":'5', "C4":'.', "C5":'.', "C6":'.', "C7":'.', "C8":'.', "C9":'.',
            "D1":'6', "D2":'.', "D3":'.', "D4":'.', "D5":'8', "D6":'.', "D7":'.', "D8":'.', "D9":'.',
            "E1":'.', "E2":'.', "E3":'.', "E4":'9', "E5":'.', "E6":'.', "E7":'3', "E8":'2', "E9":'.',
            "F1":'2', "F2":'8', "F3":'3', "F4":'5', "F5":'.', "F6":'.', "F7":'6', "F8":'4', "F9":'9',
            "G1":'.', "G2":'7', "G3":'.', "G4":'.', "G5":'.', "G6":'.', "G7":'.', "G8":'.', "G9":'3',
            "H1":'.', "H2":'.', "H3":'.', "H4":'6', "H5":'5', "H6":'7', "H7":'8', "H8":'.', "H9":'4',
            "I1":'.', "I2":'.', "I3":'6', "I4":'4', "I5":'2', "I6":'3', "I7":'5', "I8":'9', "I9":'7'
            }
    ifile=''
    algorithm_toSolve=''
    typeOutput=''
    ofile=''
    dir_path=''
    try:
        myopts, args = getopt.getopt(sys.argv[1:],"i:a:w:o:p:")
    except getopt.GetoptError as e:
        print (str(e))
        print("Usage: %s -i input -a algorithm -w typeOfoutput -o output" % sys.argv[0])
        sys.exit(2)
 
    for o, a in myopts:
        if o == '-i':
            ifile=a
        elif o=='-a':
                algorithm_toSolve=a
        elif o == '-w':
                typeOutput=a                
        elif o == '-o':
                ofile=a
        elif o == '-p':
                dir_path=a
                
    if algorithm_toSolve=="PETER_NORVIG":
        factory = AlgorithmFactory(AlgorithmType.PETER_NORVIG)
        alg = factory.getAlgorithm()
        solution = alg.solve(grid)
        if typeOutput=="CONSOLE":
            writer=DisplayCMD()
            writer.display(solution)
        if typeOutput=="TXT":
            writer=WriterTXT()
            writer.write(solution,ofile)
        if typeOutput=="CSV":
            writer=WriterCSV()
            writer.write(solution,ofile)
            
        
        
        
    if algorithm_toSolve=="BACK_TRACKING":
        factory = AlgorithmFactory(AlgorithmType.BACK_TRACKING)
        alg = factory.getAlgorithm()
        solution = alg.solve(grid)
        if typeOutput=="CONSOLE":
            writer=DisplayCMD()
            writer.display(solution)
        if typeOutput=="TXT":
            writer=WriterTXT()
            writer.write(solution,ofile)
        if typeOutput=="CSV":
            writer=WriterCSV()
            writer.write(solution,ofile)
            
            
            
    if algorithm_toSolve=="RECURSIVE":
        factory = AlgorithmFactory(AlgorithmType.RECURSIVE)
        alg = factory.getAlgorithm()
        solution = alg.solve(grid)
        if typeOutput=="CONSOLE":
            writer=DisplayCMD()
            writer.display(solution)
        if typeOutput=="TXT":
            writer=WriterTXT()
            writer.write(solution,ofile)
        if typeOutput=="CSV":
            writer=WriterCSV()
            writer.write(solution,ofile)
 
    
    
    

if __name__ == '__main__':
    main()