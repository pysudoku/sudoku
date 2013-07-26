'''
Created on Jul 25, 2013

@author: Jimena Terceros
'''
import unittest
from sudoku.writer.WriterFactory import WriterFactory
from sudoku.writer.writerCSV import WriterCSV
from sudoku.writer.writerTXT import WriterTXT
from sudoku.writer.displayCMD import DisplayCMD


class TestWriterFactory(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_having_csv_file_should_return_a_csv_file_writer(self):
        writer_factory = WriterFactory('csv')
        writer = writer_factory.getWriter()
        self.assertEqual(WriterCSV, type(writer))
        
    def test_having_txt_file_should_return_a_txt_file_writer(self):
        writer_factory = WriterFactory('txt')
        writer = writer_factory.getWriter()
        self.assertEqual(WriterTXT, type(writer))

    def test_factory_should_return_a_console_writer(self):
        writer_factory = WriterFactory('console')
        writer = writer_factory.getWriter()
        self.assertEqual(DisplayCMD, type(writer))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()