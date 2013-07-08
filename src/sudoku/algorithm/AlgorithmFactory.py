'''
Created on Jul 3, 2013

@author: Jimena Terceros
'''
from sudoku.algorithm.AlgorithmType import AlgorithmType
from sudoku.algorithm.PeterNorvigAlgorithm import PeterNorvigAlgorithm
from sudoku.algorithm.backtrackingAdapter import BacktrackingAdapter
from sudoku.algorithm.recursive import Recursive

class AlgorithmFactory(object):
    '''
    classdocs
    '''

    def __init__(self, settings):
        '''
        Constructor
        '''
        self.settings = settings
    
    def getAlgorithm(self):
        if(self.settings == AlgorithmType.PETER_NORVIG):
            return PeterNorvigAlgorithm()
        if(self.settings == AlgorithmType.BACK_TRACKING):
            return BacktrackingAdapter()
        
        if(self.settings == AlgorithmType.RECURSIVE):
            return Recursive()
        
