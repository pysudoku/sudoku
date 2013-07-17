'''
Created on Jul 16, 2013

@author: Jimena Terceros
'''
import unittest
from sudoku.game.exceptions.InvalidCmdParameterException import InvalidCmdParametersException
from sudoku.game.About import About


class TestAbout(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_when_an_about_cmd_is_created_with_None_parameter_then_should_pass_validation(self):
        try:
            about = About(None)
            result = about.execute()
            self.assertNotEqual(0, len(result))
        except InvalidCmdParametersException:
            self.fail("The initializer should not raise an exception.")
            
    def test_when_an_about_cmd_is_created_with_clear_parameter_then_should_pass_validation(self):
        dict = {}
        try:
            about = About(dict)
            result = about.execute()
            self.assertNotEqual(0, len(result))
        except InvalidCmdParametersException:
            self.fail("The initializer should not raise an exception.")
            
    def test_when_an_about_cmd_is_created_with_some_parameter_then_should_raise_an_exception(self):
        dict = {"param1": 0}
        try:
            about = About(dict)
            self.fail("The initializer should raise an exception.")
        except InvalidCmdParametersException:
            pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()