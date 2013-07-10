'''
Created on Jul 6, 2013

@author: Jimena Terceros
'''

class FileNotFoundException(Exception):
    '''
    classdocs
    '''
    

    def __init__(self, fileName):
        '''
        Constructor
        '''
        self.fileName = fileName
