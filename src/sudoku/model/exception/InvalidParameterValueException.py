'''
Created on Jun 29, 2013

@author: Jimena Terceros
'''

class InvalidParameterValueException(Exception):
    '''
    classdocs
    '''
    parameterName = ""

    def __init__(self, parameterName):
        '''
        Constructor
        '''
        self.parameterName = parameterName