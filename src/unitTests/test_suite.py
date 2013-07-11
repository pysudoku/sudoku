'''
Created on Jul 8, 2013

@author: Jimena Terceros
'''
import unittest
from coverage import coverage

cov = coverage(omit=['*__.py', '*test*.py'])
cov.start()

from unitTests.algorithm.backtrakingTest import TestBacktracking
from unitTests.algorithm.UniTest_algPeter import TestAlgPeter
from unitTests.algorithm.test_recursive import Test_Recursive
from unitTests.algorithm.UnitTest_AlgFactory import TestAlgFactory
from unitTests.settings.TestSettingsReader import TestSettingsReader
from unitTests.settings.TestSettings import TestSettings
from unitTests.settings.Test_Level import TestLevel
from unitTests.writer.displayCMDTest import TestDisplayCMD
from unitTests.writer.writerTest import TestWriter
from unitTests.reader.test_txtparser import TestTXTParser
from unitTests.reader.test_csvparser import TestCSVParser
from unitTests.reader.test_commandlineparser import TestCommandLineParser

def main():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBacktracking))
    suite.addTest(unittest.makeSuite(TestAlgPeter))
    suite.addTest(unittest.makeSuite(Test_Recursive))
    suite.addTest(unittest.makeSuite(TestAlgFactory))
    suite.addTest(unittest.makeSuite(TestSettingsReader))
    suite.addTest(unittest.makeSuite(TestSettings))
    suite.addTest(unittest.makeSuite(TestLevel))
    suite.addTest(unittest.makeSuite(TestDisplayCMD))
    suite.addTest(unittest.makeSuite(TestWriter))
    suite.addTest(unittest.makeSuite(TestTXTParser))
    suite.addTest(unittest.makeSuite(TestCSVParser))
    suite.addTest(unittest.makeSuite(TestCommandLineParser))

    unittest.TextTestRunner(verbosity = 2).run(suite)
    
if __name__ == '__main__':
    main()
    cov.stop()
    cov.save()
    cov.html_report()
