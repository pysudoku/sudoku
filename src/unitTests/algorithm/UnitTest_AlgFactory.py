'''
Created on Jul 3, 2013

@author: Jimena Terceros
'''
import unittest
from sudoku.algorithm.AlgorithmFactory import AlgorithmFactory
from sudoku.algorithm.AlgorithmType import AlgorithmType
from sudoku.algorithm.PeterNorvigAlgorithm import PeterNorvigAlgorithm
from sudoku.algorithm.recursive import Recursive
from sudoku.algorithm.backTrackingAdapter import BackTrackingAdapter

class TestAlgFactory(unittest.TestCase):

    def setUp(self):
        # create a setting with algorithm type PETER
        self.factoryPeter = AlgorithmFactory(AlgorithmType.PETER_NORVIG)
        self.factoryBacktracking = AlgorithmFactory(AlgorithmType.BACK_TRACKING)
        self.factoryRecursive = AlgorithmFactory(AlgorithmType.RECURSIVE)

    def test_having_setttings_for_peter_the_factory_should_return_peter_algorithm(self):
        alg = self.factoryPeter.getAlgorithm()
        self.assertEqual(PeterNorvigAlgorithm, type(alg))
        
    def test_having_setttings_for_peter_the_factory_should_return_backtracking_algorithm(self):
        alg = self.factoryBacktracking.getAlgorithm()
        self.assertEqual(BackTrackingAdapter, type(alg))
        
    def test_having_setttings_for_peter_the_factory_should_return_recursive_algorithm(self):
        alg = self.factoryRecursive.getAlgorithm()
        self.assertEqual(Recursive, type(alg))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']fa
    unittest.main()