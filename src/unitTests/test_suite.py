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
from unitTests.settings.TestSettingsWriter import TestSettingsWriter
from unitTests.settings.TestSettings import TestSettings
from unitTests.settings.Test_Level import TestLevel
from unitTests.writer.displayCMDTest import TestDisplayCMD
from unitTests.writer.writerTest import TestWriter
from unitTests.reader.test_txtparser import TestTXTParser
from unitTests.reader.test_csvparser import TestCSVParser
from unitTests.reader.test_commandlineparser import TestCommandLineParser
from unitTests.settings.TestSettingsManager import TestSettingsManager
from unitTests.model.UniTestcell import TestCell
from unitTests.model.UniTestSudokutable import TestSudokuBoard
from unitTests.game.Test_Game import TestGame
from unitTests.game.Test_About import TestAbout
from unitTests.game.Test_Sudoku_Command import TestSudokuCommand
from unitTests.game.Test_Read_Configuration import TestReadConfiguration
from unitTests.game.TestSetValueCommand import TestSetValueCommand
from unitTests.game.TestRestartGameCommand import TestRestartGameCommand
from unitTests.game.TestHintCommand import TestHintCommand
from unitTests.game.TestCommandFactory import TestCommandFactory
from unitTests.generator.test_generator import TestGenerator
from unitTests.game.test_generate_game import TestGenerateGameCommand
from unitTests.console.test_console import TestConsole
from unitTests.game.test_printCommand import TestPrintBoardCommand
from unitTests.game.TestStartCommand import TestStartCommand
from unitTests.game.TestStopCommand import TestStopCommand
from unitTests.game.TestPauseCommand import TestPauseCommand
from unitTests.game.test_solve_game import TestSolveGameCommand
from unitTests.reader.test_parser_factory import TestParserFactory
from unitTests.writer.test_game_writer import TestSudokuGameWriter
from unitTests.reader.test_game_reader import TestSudokuGameReader
from unitTests.game.test_save_command import TestSaveGameCommand
from unitTests.game.test_open_command import TestOpenGameCommand
from unitTests.game.test_import import TestImportCommand
from unitTests.game.test_export import TestExportCommand
from unitTests.writer.TestWriteFactory import TestWriterFactory

def main():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBacktracking))
    suite.addTest(unittest.makeSuite(TestAlgPeter))
    suite.addTest(unittest.makeSuite(Test_Recursive))
    suite.addTest(unittest.makeSuite(TestAlgFactory))
    suite.addTest(unittest.makeSuite(TestSettingsReader))
    suite.addTest(unittest.makeSuite(TestSettingsWriter))
    suite.addTest(unittest.makeSuite(TestSettings))
    suite.addTest(unittest.makeSuite(TestLevel))
    suite.addTest(unittest.makeSuite(TestDisplayCMD))
    suite.addTest(unittest.makeSuite(TestWriter))
    suite.addTest(unittest.makeSuite(TestTXTParser))
    suite.addTest(unittest.makeSuite(TestCSVParser))
    suite.addTest(unittest.makeSuite(TestCommandLineParser))
    suite.addTest(unittest.makeSuite(TestSettingsManager))
    suite.addTest(unittest.makeSuite(TestCell))
    suite.addTest(unittest.makeSuite(TestSudokuBoard))
    suite.addTest(unittest.makeSuite(TestGame))
    suite.addTest(unittest.makeSuite(TestSudokuCommand))
    suite.addTest(unittest.makeSuite(TestAbout))
    suite.addTest(unittest.makeSuite(TestReadConfiguration))
    suite.addTest(unittest.makeSuite(TestSetValueCommand))
    suite.addTest(unittest.makeSuite(TestRestartGameCommand))
    suite.addTest(unittest.makeSuite(TestHintCommand))
    suite.addTest(unittest.makeSuite(TestCommandFactory))
    suite.addTest(unittest.makeSuite(TestGenerator))
    suite.addTest(unittest.makeSuite(TestGenerateGameCommand))
    suite.addTest(unittest.makeSuite(TestPrintBoardCommand))
    suite.addTest(unittest.makeSuite(TestConsole))
    suite.addTest(unittest.makeSuite(TestStartCommand))
    suite.addTest(unittest.makeSuite(TestStopCommand))
    suite.addTest(unittest.makeSuite(TestPauseCommand))
    suite.addTest(unittest.makeSuite(TestSolveGameCommand))
    suite.addTest(unittest.makeSuite(TestParserFactory))
    suite.addTest(unittest.makeSuite(TestSudokuGameWriter))
    suite.addTest(unittest.makeSuite(TestSudokuGameReader))
    suite.addTest(unittest.makeSuite(TestSaveGameCommand))
    suite.addTest(unittest.makeSuite(TestOpenGameCommand))
    suite.addTest(unittest.makeSuite(TestImportCommand))
    suite.addTest(unittest.makeSuite(TestExportCommand))
    suite.addTest(unittest.makeSuite(TestWriterFactory))

    unittest.TextTestRunner(verbosity = 2).run(suite)
    
if __name__ == '__main__':
    main()
    cov.stop()
    cov.save()
    cov.html_report()
