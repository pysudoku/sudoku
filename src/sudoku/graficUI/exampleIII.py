'''
Created on Jul 19, 2013

@author: Ines Baina
'''


from tkinter import Tk, Text,RIGHT,LEFT,BOTH,TOP

from tkinter.ttk import *
from tkinter.ttk import Frame, Button, Style, Label
from tkinter.constants import RAISED



class SudokuGameWindow(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Sudoku")
        self.style = Style()
        self.style.theme_use("default")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=1)
        
        self.pack(fill=BOTH, expand=1)
        

               
        lbl = Label(self, text="Sudoku Game")
        lbl.pack(side=TOP,padx=200,pady=200)
        
        area = Text(self)
        
        #area.pack(side=LEFT, padx=0, pady=1)
        
        lbtn = Button(self, text="Load",command=self.onLoadButtonClick)
        lbtn.pack(side=RIGHT, padx=0, pady=5)

        rbtn = Button(self, text="Restart",command=self.onRestartButtonClick)
        rbtn.pack(side=RIGHT, padx=0, pady=5)
        
        hbtn = Button(self, text="Hint",command=self.onHintButtonClick)
        hbtn.pack(side=RIGHT, padx=0, pady=5)

        sbtn = Button(self, text="Solve",command=self.onSolveButtonClick)
        sbtn.pack(side=RIGHT,padx=0, pady=7)
         
        ssbtn = Button(self, text="Save",command=self.onSaveButtonClick)
        ssbtn.pack(side=RIGHT,padx=0, pady=7)
        
        qbtn = Button(self, text="Quit",command=self.onQuitButtonClick)
        qbtn.pack(side=RIGHT,padx=0, pady=9)       
              
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
def main():
  
    root = Tk()
    root.geometry("450x600+300+300")
    app = SudokuGameWindow(root)
    root.mainloop()  


if __name__ == '__main__':
    main()