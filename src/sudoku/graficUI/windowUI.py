'''
Created on Jul 23, 2013

@author: Ines Baina
'''
from tkinter import *
from tkinter import ttk
from tkinter import font


class SudokuGameWindow():
    
    def initUI(self):
    
        root = Tk()
        root.geometry("600x650+300+300")
        root.title('Sudoku Game')

        content = ttk.Frame(root)
        frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=500, height=500)
        
        self.customFont_title = font.Font(family="Helvetica",size=18,weight="bold")
        self.customFont_label = font.Font(family="Comic Sans",size=12,weight="bold")
        title_lbl = ttk.Label(content, text = "Sudoku Game",font=self.customFont_title)
        time_lbl=ttk.Label(content,text = "Timer:",font=self.customFont_label)
        
        level_sudoku_tab = ttk.Notebook(root,width=400,height=400)

        tab1 = Frame(level_sudoku_tab)
        tab2 = Frame(level_sudoku_tab)
        tab3 = Frame(level_sudoku_tab)
        level_sudoku_tab.add(tab1, text = "EASY")
        level_sudoku_tab.add(tab2, text = "MEDIUM")
        level_sudoku_tab.add(tab3, text = "HARD")
        
        #-----Time control buttons---------
        start_btn = ttk.Button(content, text="Start",command = self.onStartButtonClick)
        pause_btn = ttk.Button(content, text="Pause",command = self.onPauseButtonClick)
        stop_btn = ttk.Button(content, text="Stop",command = self.onStopButtonClick)
        
        
        #-----Play buttons---------
        load_btn = ttk.Button(content, text = "Load" , command = self.onLoadButtonClick)
        restart_btn = ttk.Button(content, text = "Restart" ,command = self.onRestartButtonClick)
        hint_btn = ttk.Button(content, text = "Hint" , command = self.onHintButtonClick)
        solve_btn = ttk.Button(content, text = "Solve" , command = self.onSolveButtonClick)
        save_btn = ttk.Button(content, text = "Save" , command = self.onSaveButtonClick)
        
        #-----Quit buttons---------
        quit_btn = ttk.Button(content, text = "Quit" , command = self.onQuitButtonClick)
       
        #----- Grid Distribution-------
        content.grid(column=0, row=0)
        frame.grid(column=0, row=1, columnspan=5, rowspan=2)
        title_lbl.grid(column=3, row=0, columnspan=1)
        time_lbl.grid(column=5,row=2, columnspan=1)
        level_sudoku_tab.grid(column=0,row=0,columnspan=4, rowspan=2)
       
        start_btn.grid(column=5, row=3)
        pause_btn.grid(column=5, row=4)
        stop_btn.grid(column=5, row=5)
        
        load_btn.grid(column=1, row=3)
        restart_btn.grid(column=1, row=4)
        hint_btn.grid(column=1, row=5)
        solve_btn.grid(column=2, row=3)
        save_btn.grid(column=2, row=4)
        
        quit_btn.grid(column=2, row=5)
        
        # ----------Grid----------
       # name=
        
        #-------------------------
        
        
        
        
        
        root.mainloop()

    def onStartButtonClick(self):
        print ("You clicked the Start  Game Timer button !")
    def onPauseButtonClick(self):
        print ("You clicked the Pause Game Timer button !")
    def onStopButtonClick(self):
        print ("You clicked the Stop Game Timer button !")
    def onLoadButtonClick(self):
        print ("You clicked the Load Game button !")
    def onRestartButtonClick(self):
        print ("You clicked the Restart Game button !")
    def onHintButtonClick(self):
        print ("You clicked the Hint button !")
    def onSolveButtonClick(self):
        print ("You clicked the Solve Game button !")
    def onSaveButtonClick(self):
        print ("You clicked the Save button !")
    def onQuitButtonClick(self):
        print ("You clicked the Quit Game button !")


    def onPressEnter(self,event):
        print ("You pressed enter !")
      
  
        
app=SudokuGameWindow()
app.initUI()
      



    

    