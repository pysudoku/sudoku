'''
Created on Jul 3, 2013

@author: Jimena Terceros
'''
from sudoku.algorithm.AlgorithmFactory import AlgorithmFactory
from sudoku.algorithm.AlgorithmType import AlgorithmType

if __name__ == '__main__':
    """
    this grid is to verify valid solution of the algorithm
    grid = {
            "A1":'4', "A2":'.', "A3":'.', "A4":'.', "A5":'.', "A6":'.', "A7":'8', "A8":'.', "A9":'5',
            "B1":'.', "B2":'3', "B3":'.', "B4":'.', "B5":'.', "B6":'.', "B7":'.', "B8":'.', "B9":'.',
            "C1":'.', "C2":'.', "C3":'.', "C4":'7', "C5":'.', "C6":'.', "C7":'.', "C8":'.', "C9":'.',
            "D1":'.', "D2":'2', "D3":'.', "D4":'.', "D5":'.', "D6":'.', "D7":'.', "D8":'6', "D9":'.',
            "E1":'.', "E2":'.', "E3":'.', "E4":'.', "E5":'8', "E6":'.', "E7":'4', "E8":'.', "E9":'.',
            "F1":'.', "F2":'.', "F3":'.', "F4":'.', "F5":'1', "F6":'.', "F7":'.', "F8":'.', "F9":'.',
            "G1":'.', "G2":'.', "G3":'.', "G4":'6', "G5":'.', "G6":'3', "G7":'.', "G8":'7', "G9":'.',
            "H1":'5', "H2":'.', "H3":'.', "H4":'2', "H5":'.', "H6":'.', "H7":'.', "H8":'.', "H9":'.',
            "I1":'1', "I2":'4', "I3":'.', "I4":'.', "I5":'.', "I6":'.', "I7":'.', "I8":'.', "I9":'.'
            }
    this grid has all data emptly, the result return a valid solution
    grid = {
            "A1":'.', "A2":'.', "A3":'.', "A4":'.', "A5":'.', "A6":'.', "A7":'.', "A8":'.', "A9":'.',
            "B1":'.', "B2":'.', "B3":'.', "B4":'.', "B5":'.', "B6":'.', "B7":'.', "B8":'.', "B9":'.',
            "C1":'.', "C2":'.', "C3":'.', "C4":'.', "C5":'.', "C6":'.', "C7":'.', "C8":'.', "C9":'.',
            "D1":'.', "D2":'.', "D3":'.', "D4":'.', "D5":'.', "D6":'.', "D7":'.', "D8":'.', "D9":'.',
            "E1":'.', "E2":'.', "E3":'.', "E4":'.', "E5":'.', "E6":'.', "E7":'.', "E8":'.', "E9":'.',
            "F1":'.', "F2":'.', "F3":'.', "F4":'.', "F5":'.', "F6":'.', "F7":'.', "F8":'.', "F9":'.',
            "G1":'.', "G2":'.', "G3":'.', "G4":'.', "G5":'.', "G6":'.', "G7":'.', "G8":'.', "G9":'.',
            "H1":'.', "H2":'.', "H3":'.', "H4":'.', "H5":'.', "H6":'.', "H7":'.', "H8":'.', "H9":'.',
            "I1":'.', "I2":'.', "I3":'.', "I4":'.', "I5":'.', "I6":'.', "I7":'.', "I8":'.', "I9":'.'
            }
    This grid is to verify if you give to the algorithm solved, the algorithm return the same solution
    grid = {
            "A1":'1', "A2":'2', "A3":'3', "A4":'4', "A5":'5', "A6":'6', "A7":'7', "A8":'8', "A9":'9',
            "B1":'4', "B2":'5', "B3":'6', "B4":'7', "B5":'8', "B6":'9', "B7":'1', "B8":'2', "B9":'3',
            "C1":'7', "C2":'8', "C3":'9', "C4":'1', "C5":'2', "C6":'3', "C7":'4', "C8":'5', "C9":'6',
            "D1":'2', "D2":'3', "D3":'1', "D4":'6', "D5":'7', "D6":'4', "D7":'8', "D8":'9', "D9":'5',
            "E1":'8', "E2":'7', "E3":'5', "E4":'9', "E5":'1', "E6":'2', "E7":'3', "E8":'6', "E9":'4',
            "F1":'6', "F2":'9', "F3":'4', "F4":'5', "F5":'3', "F6":'8', "F7":'2', "F8":'1', "F9":'7',
            "G1":'3', "G2":'1', "G3":'7', "G4":'2', "G5":'6', "G6":'5', "G7":'9', "G8":'4', "G9":'8',
            "H1":'5', "H2":'4', "H3":'2', "H4":'8', "H5":'9', "H6":'7', "H7":'6', "H8":'3', "H9":'1',
            "I1":'9', "I2":'6', "I3":'8', "I4":'3', "I5":'4', "I6":'1', "I7":'5', "I8":'7', "I9":'2'
            }
    """
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
    
    #Algotithm solver = new PeterNorvigSolver()
    #solver = PeterNorvigAlgorithm()
    #solution = solver.solve(grid)
    #print(solution)
    
    factory = AlgorithmFactory(AlgorithmType.PETER_NORVIG)
    alg = factory.getAlgorithm()
    solution = alg.solve(grid)
    print(solution)
    
    factory = AlgorithmFactory(AlgorithmType.BACK_TRACKING)
    alg = factory.getAlgorithm()
    solution = alg.solve(grid)
    print(solution)
    
    factory = AlgorithmFactory(AlgorithmType.RECURSIVE)
    alg = factory.getAlgorithm()
    solution = alg.solve(grid)
    print(solution)