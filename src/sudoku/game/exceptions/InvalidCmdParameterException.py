'''
Created on Jul 16, 2013

@author: Jimena Terceros
'''

class InvalidCmdParametersException(Exception):
    '''
    classdocs
    '''


    def __init__(self, message):
        '''
        Constructor
        '''
        self.message = message