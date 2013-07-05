'''
Created on Jul 3, 2013

@author: Jimena Terceros
'''

from abc import abstractmethod

class Algorithm(object):
    
    @abstractmethod
    def solve(self, grid): pass
        