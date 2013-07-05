from sudoku.algorithm.Algorithm import Algorithm
from sudoku.algorithm.exceptions.InvalidSudokuException import InvalidSudokuException


class Posicion:
    """
    Posicion is a class that alow us to manage better every position in Sudoku

    """

    def __init__(self,maxfila,maxcol):
        self.maxfila = maxfila
        self.maxcol = maxcol
        self.fila = 0
        self.col = 0

    def setFila(self, fila):
        """setFila is going to asign the correct row value to any function

        :fila: is the number of row to execute a task
        :maxfila: is a constant that contains the number of total rows in Sudoku

        """
        if fila < 0:
            self.fila = 0
        elif fila >= self.maxfila:
            self.fila = -1
        else:
            self.fila = fila

    def setCol(self, col):
        """setCol is going to asign the correct column value to any function

        :col: is the number of column to execute a task
        :maxcol: is a constant that contains the number of total columns in Sudoku

        """
        if col < 0:
            self.col = 0
        elif col >= self.maxcol:
            self.col = -1
        else:
            self.col = col

    def getFila(self):
        return self.fila

    def getCol(self):
        return self.col

    def fin(self):
        return self.fila == -1 and self.col == -1

    def reset(self):
        self.fila = 0
        self.col = 0

    def sig(self):
        """sig function will give the next position in grid if fila and column are -1 if we are at the end of sudoku grid.
            This will control that position is out of the scope grids

       """

        if not self.fin():
            self.col += 1
            if self.col == self.maxcol:
                self.col = 0
                self.fila +=1
                if self.fila == self.maxfila:
                    self.fila = -1
                    self.col = -1

    def getPos(self):
        return [self.fila, self.col]

# --------------clase Backtraking----------------

class BacktrackingAlgorithm(Algorithm):

    MAXLINEAS = 0
    MAXCOLS = 0
#Funcion que resuelve el sudoku
    def solve(self, grid):

        sudoku = self.dict_to_list(grid)
        self.MAXLINEAS = len(sudoku)
        self.MAXCOLS = self.MAXLINEAS

        # Comenzamos en [0,0]
        pos = Posicion(self.MAXLINEAS,self.MAXCOLS)

        pilaActual = []
        pilaPosibles = []

        while not pos.fin():
            posibles = self.prueba(sudoku,pilaActual,pos.getFila(),pos.getCol())

            while posibles == []:
                if pos.fin():
                    # Hemos llegado al fin
                    solution = self.imprime(sudoku,pilaActual)
                    #print (sudoku)
                    return solution

                pos.sig()
                posibles = self.prueba(sudoku,pilaActual,pos.getFila(),pos.getCol())

            if posibles == [-1]:
                # Backtracking
                estado = pilaActual.pop()
                while estado[0] != pilaPosibles[-1][0] or estado[1] != pilaPosibles[-1][1]:
                    estado = pilaActual.pop()
                # Ahora los ultimos estados de ambas tienen la misma posicion
                pilaActual.append(pilaPosibles.pop())
                # Ponemos la posicion correcta
                pos.setFila(pilaActual[-1][0])
                pos.setCol(pilaActual[-1][1])

            else:
                # Aqui tenemos unas posibles
                # Cojemos la primera y la apilamos en pilaActual, y el resto en pilaPosibles
                for posible in posibles[1:]:
                    pilaPosibles.append([pos.getFila(),pos.getCol(),posible])

                pilaActual.append([pos.getFila(),pos.getCol(),posibles[0]])


            pos.sig()
        result = self.imprime(sudoku,pilaActual)
        if not result:
            raise InvalidSudokuException()
        else:
            return result

    def existe(self, sudoku, num, linea, col):
        """existe is a function to verify if the number exists in row or column

        @param sudoku:
        @param encontrado:
        @param LINEAS:
        @param COLUMNAS:
        @return: a boolean if number exists in row or column could be True or False
        """
        encontrado = False
        for l in range(0,self.LINEAS):
            if sudoku[l][col] == num:
                encontrado = True

        for c in range(0,self.COLUMNAS):
            if sudoku[linea][c] == num:
                encontrado = True
        return encontrado


    def prueba(self, sudoku, asignadas, fila, col):
        """prueba is a function to verify if the number exists in row or column
            It could return three results:
            a) [] if position is busy
            b) a list of posible numbers
            c) [-1] it is imposible to solve

        @param sudoku:
        @param resultado:
        @param existe:

        @return: a list of posible values
        """
        if sudoku[fila][col] != 0:
            return []

        else:
            resultado = []

            # probamos todos los numeros posibles
            for n in range(1,self.MAXLINEAS+1):

                existe = False

                # barremos lineas
                for l in range(0,self.MAXLINEAS):
                    if sudoku[l][col] == n:
                        existe = True
                        break

                # barremos columnas
                for c in range(0,self.MAXCOLS):
                    if sudoku[fila][c] == n:
                        existe = True
                        break

                # barremos cuadrantes

                r1 = [0, 1, 2]
                r2 = [3, 4, 5]
                r3 = [6, 7, 8]
                if fila in r1:
                    rFilas = r1
                elif fila in r2:
                    rFilas = r2
                else:
                    rFilas = r3
                if col in r1:
                    rCols = r1
                elif col in r2:
                    rCols = r2
                else:
                    rCols = r3

                for rr in rFilas:
                    for cc in rCols:
                        if sudoku[rr][cc] == n:
                            existe = True
                            break

                # Buscamos en las posiciones asignadas
                for asig in asignadas:
                    if asig[0] == fila and asig[2] == n:
                        existe = True
                        break
                    if asig[1] == col and asig[2] == n:
                        existe = True
                        break

                if not existe:
                    resultado.append(n)

            if resultado == []:
                # Un callejon sin salida
                resultado = [-1]

            #print (resultado)
            return resultado


    def imprime(self, sudoku, asignadas):
        """imprime is a function to display and asign the sudoku solved

        @param dict_result: will contain the sudoku solved in a dictionary structure
        @param sudoku:
        @param asignadas:

        @return: a dictionary with the sudoku solved where the Key is the Row and column of sudokugame and Value is the number asigned to solve sudoku
        """
        dict_result = {}
        for fila in range(0,len(sudoku)):
            cadena = ""
            for columna in range(0,len(sudoku)):
                if sudoku[fila][columna] == 0:
                    encontrado = False
                    for a in asignadas:
                        if a[0] == fila and a[1] == columna:
                            dict_result[chr(fila+65) + str(columna+1)] = str(a[2])
                            cadena +=  str(a[2])
                            encontrado = True
                    if not encontrado:
                        cadena += ""
                else:
                    cadena += str(sudoku[fila][columna])
                    dict_result[chr(fila+65) + str(columna+1)] = str(sudoku[fila][columna])

        return dict_result

    #Funcion que devuelve una matriz apartir de un diccionario
    def dict_to_list(self, grid):
        """dict_to_list is a function to change the sudoku from a dictionary to a matrix
            It only works with 9 rows and 9 columns

        @param matrix: will contain the sudoku solved in a dictionary structure
        @return: a List of list with the sudoku numbers Zero instead of .
        """
        matrix = []
        for row in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I']:
            matrix_row = []
            for column in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                matrix_row.append(0 if grid[row + column] == '.' else int(grid[row + column]))
            matrix.append(matrix_row)

        return matrix
