from sudoku.algorithm.Algorithm import Algorithm
from sudoku.algorithm.backtrackingAlgorithm import BacktrackingAlgorithm
class BackTrackingAdapter(Algorithm):
    """
    BackTracking is a class convert the sudoku from dictionary into a List of list structure.
    When sudoku is solved then this class also convert the sudoku solved into a Dictionary

    """
    def __init__(self):
        self.backtrackingAlgorithm = BacktrackingAlgorithm()

    def solve(self, sudokuDic):
        """dict_to_list is a function to change from dictionary  to a matrix
            It only works with 9 rows and 9 columns

        @param sudokuMatrix: List will contain the sudoku clean
        @param resolvedSudokuMatrix: List will contain the sudoku solved
        @return: a Dictionary with the sudoku solved
        """
        sudokuMatrix = self.dict_to_list(sudokuDic)
        
        resolvedSudokuMatrix  = self.backtrackingAlgorithm.solve(sudokuMatrix)
        return self.list_to_dict(resolvedSudokuMatrix)


    def dict_to_list(self, grid):
        """dict_to_list is a function to change from dictionary  to a matrix
            It only works with 9 rows and 9 columns

        @param matrix: will contain the sudoku clean in a List structure
        @return: a List of list with the sudoku numbers Zero instead of .
        """
        matrix = []
        for row in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I']:
            matrix_row = []
            for column in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                matrix_row.append(0 if grid[row + column] == '.' else int(grid[row + column]))
            matrix.append(matrix_row)

        return matrix

    def list_to_dict(self, grid_as_list):
        """list_to_dic is a function to change the sudoku from a matrix to a dictionary
            It only works with 9 rows and 9 columns

        @param grid_as_dic: will contain the sudoku solved in a Dictionary structure
        @return: a dictionary with the sudoku solved
        """
        row = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I']
        column = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        grid_as_dict = {}

        for j in range(9):
            for i in range(9):
                grid_as_dict[row[j] + column[i]] = '.' if grid_as_list[j][i] == 0 else str(grid_as_list[j][i])
        return grid_as_dict
