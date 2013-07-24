'''
Created on Jul 16, 2013

@author: Jimena Terceros
'''
import time

class Game(object):
    '''
    Game class create the game empty. all commands update the fields of this class 
    '''

    def __init__(self):
        '''
        Constructor
        @var settings_manager: the value for all application settings that by default is none
        @var initial_sudoku: the value for initial Sudoku Board by defaul is none
        @var user_sudoku: the value for user Sudoku Board attribute by default is none
        @var solved_sudoku: the value for solved Sudoku attribute by default is none
        '''
        self.settings_manager = None
        self.initial_sudoku = None
        self.user_sudoku = None
        self.solved_sudoku = None
        self.currentTime = 0.0
        self.started = False
        self.paused = False
        self.game_generator = None
        self.solver_algorithm = None

    def set_settings_manager(self, settingsManager):
        '''
        Sets the setting manager value
        '''
        self.settings_manager = settingsManager
        
    def start_game_timer(self):
        if not self.paused:
            self.currentTime = 0.0
        self.paused = False
        self.started = True
        self.startTime =  time.clock()
        
    def stop_game_timer(self):
        self.calculate_time()
        self.started = False
        self.paused = False
        
    def pause_game_timer(self):
        self.calculate_time()
        self.paused = True
        self.started = False
    
    def calculate_time(self):
        endTime = time.clock()
        self.currentTime = self.currentTime + (endTime - self.startTime)
        
    def is_started(self):
        return self.started
    
    def is_paused(self):
        return self.paused
    
    def get_current_time(self):
        return self.currentTime

    def set_game_generator(self, generator):
        '''
        Sets the generator object the game uses to generate Sudoku puzzles
        '''
        self.game_generator = generator
        
    def set_solver(self, solver_algorithm):
        '''
        Sets the solver object the game uses to solve Sudoku puzzles
        '''
        self.solver_algorithm = solver_algorithm