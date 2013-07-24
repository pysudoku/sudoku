'''
Created on Jul 19, 2013

@author: Ines Baina
'''


from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksavefilename


def open_file_windows():

    root=Tk()    
    filename = askopenfilename (filetypes=[("allfiles","*"),("pythonfiles","*.py")])
def save_file_windows():

    root=Tk()    
    filename = askopenfilename (filetypes=[("allfiles","*"),("pythonfiles","*.py")])
    
main()    