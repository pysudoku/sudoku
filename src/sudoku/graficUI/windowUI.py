'''
Created on Jul 23, 2013

@author: Ines Baina
'''
from tkinter import *
from tkinter import ttk
from tkinter import font




from tkinter.filedialog import askopenfilename


class SudokuGameWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.boardsize = 405
        self.sqsize = self.boardsize//9
        master.geometry("600x650+300+300")
        master.title('Sudoku Game')
        self.initialdraw()
        self.grid(row=0,column=0)
    
    def initialdraw(self):
    
        #root = Tk()
        #root.geometry("600x650+300+300")
        #root.title('Sudoku Game')

        content = ttk.Frame(self,padding=(70,70,5,5))
        
        
        self.customFont_title = font.Font(family="Helvetica",size=18,weight="bold")
        self.customFont_label = font.Font(family="Comic Sans",size=12,weight="bold")
        title_lbl = ttk.Label(content, text = "Sudoku Game",font=self.customFont_title)
        time_lbl=ttk.Label(content,text = "Timer:",font=self.customFont_label)
        
        level_sudoku_tab = ttk.Notebook(content,width=405,height=405)
        
        
        #self.board = Canvas(content, width=self.boardsize, height=self.boardsize,bg='white')
        

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
        
        title_lbl.grid(column=2, row=0, columnspan=1)
        time_lbl.grid(column=5,row=2, columnspan=1)
        level_sudoku_tab.grid(column=0, row=1, columnspan=5, rowspan=2)
       
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
       # command=printBoardCommand()
       
       
         
    
       
        """
        self.board.grid(row=1,column=0,padx=(100,10),pady=(100,10))
        
        for row in range(9):
            for col in range(9):
                top = row * self.sqsize
                left = col * self.sqsize
                bottom = row * self.sqsize + self.sqsize -2
                right = col * self.sqsize + self.sqsize -2
                rect = self.board.create_rectangle(left,top,right,bottom,outline='gray',fill='')

        self.board.focus_set()
        #-------------------------
        """
        
        
        
        
        

    def onStartButtonClick(self):
        print ("You clicked the Start  Game Timer button !")
    def onPauseButtonClick(self):
        print ("You clicked the Pause Game Timer button !")
    def onStopButtonClick(self):
        print ("You clicked the Stop Game Timer button !")
    def onLoadButtonClick(self):
        print ("You clicked the Load Game button !") 
        filename = askopenfilename (filetypes=[("allfiles","*"),("TXTfiles","*.txt")])
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
      
if __name__ == '__main__':
    tk = Tk()
    sudoku_gameUI = SudokuGameWindow(tk)
    tk.mainloop()  
        

      



    

    