class Position:
    """
    Position is a class that allow us to manage better every position in Sudoku

    """
    def __init__(self,maxfila,maxcol):
        self.maxfila = maxfila
        self.maxcol = maxcol
        self.row = 0
        self.column = 0

    def setFila(self, fila):
        """
        setFila is going to assign the correct row value to any function

        :row: is the number of row to execute a task
        :maxfila: is a constant that contains the number of total rows in Sudoku

        """
        if fila < 0:
            self.row = 0
        elif fila >= self.maxfila:
            self.row = -1
        else:
            self.row = fila

    def setCol(self, col):
        """
        setCol is going to assign the correct column value to any function

        :column: is the number of column to execute a task
        :maxcol: is a constant that contains the number of total columns in Sudoku 
        """
        if col < 0:
            self.column = 0
        elif col >= self.maxcol:
            self.column = -1
        else:
            self.column = col
        

    def getFila(self):
        return self.row

    def getCol(self):
        return self.column

    def fin(self):
        return self.row == -1 and self.column == -1

    def sig(self):
        """sig function will give the next position in grid if row and column are -1 if we are at the end of sudoku grid.
            This will control that position is out of the scope grids

       """
        if not self.fin():
            self.column += 1
            if self.column == self.maxcol:
                self.column = 0
                self.row +=1
                if self.row == self.maxfila:
                    self.row = -1
                    self.column = -1
