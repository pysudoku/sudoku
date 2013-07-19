import unittest
from sudoku.algorithm.recursive import Recursive
from sudoku.algorithm.exceptions.InvalidSudokuException import InvalidSudokuException

class Test_Recursive(unittest.TestCase):
    def setUp(self):
        self.easy_level_puzzle = {
            "A1":'.', "A2":'6', "A3":'7', "A4":'.', "A5":'4', "A6":'.', "A7":'.', "A8":'.', "A9":'2',
            "B1":'9', "B2":'.', "B3":'.', "B4":'7', "B5":'3', "B6":'.', "B7":'4', "B8":'5', "B9":'.',
            "C1":'4', "C2":'.', "C3":'5', "C4":'.', "C5":'.', "C6":'.', "C7":'.', "C8":'.', "C9":'.',
            "D1":'6', "D2":'.', "D3":'.', "D4":'.', "D5":'8', "D6":'.', "D7":'.', "D8":'.', "D9":'.',
            "E1":'.', "E2":'.', "E3":'.', "E4":'9', "E5":'.', "E6":'.', "E7":'3', "E8":'2', "E9":'.',
            "F1":'2', "F2":'8', "F3":'3', "F4":'5', "F5":'.', "F6":'.', "F7":'6', "F8":'4', "F9":'9',
            "G1":'.', "G2":'7', "G3":'.', "G4":'.', "G5":'.', "G6":'.', "G7":'.', "G8":'.', "G9":'3',
            "H1":'.', "H2":'.', "H3":'.', "H4":'6', "H5":'5', "H6":'7', "H7":'8', "H8":'.', "H9":'4',
            "I1":'.', "I2":'.', "I3":'6', "I4":'4', "I5":'2', "I6":'3', "I7":'5', "I8":'9', "I9":'7'
            }

        self.easy_level_puzzle_solution = {
            "A1":'1', "A2":'6', "A3":'7', "A4":'8', "A5":'4', "A6":'5', "A7":'9', "A8":'3', "A9":'2',
            "B1":'9', "B2":'2', "B3":'8', "B4":'7', "B5":'3', "B6":'6', "B7":'4', "B8":'5', "B9":'1',
            "C1":'4', "C2":'3', "C3":'5', "C4":'2', "C5":'1', "C6":'9', "C7":'7', "C8":'8', "C9":'6',
            "D1":'6', "D2":'4', "D3":'9', "D4":'3', "D5":'8', "D6":'2', "D7":'1', "D8":'7', "D9":'5',
            "E1":'7', "E2":'5', "E3":'1', "E4":'9', "E5":'6', "E6":'4', "E7":'3', "E8":'2', "E9":'8',
            "F1":'2', "F2":'8', "F3":'3', "F4":'5', "F5":'7', "F6":'1', "F7":'6', "F8":'4', "F9":'9',
            "G1":'5', "G2":'7', "G3":'4', "G4":'1', "G5":'9', "G6":'8', "G7":'2', "G8":'6', "G9":'3',
            "H1":'3', "H2":'9', "H3":'2', "H4":'6', "H5":'5', "H6":'7', "H7":'8', "H8":'1', "H9":'4',
            "I1":'8', "I2":'1', "I3":'6', "I4":'4', "I5":'2', "I6":'3', "I7":'5', "I8":'9', "I9":'7'
            }

        self.moderate_level_puzzle = {
            "A1":'.', "A2":'8', "A3":'.', "A4":'7', "A5":'.', "A6":'4', "A7":'.', "A8":'.', "A9":'.',
            "B1":'9', "B2":'.', "B3":'4', "B4":'.', "B5":'.', "B6":'.', "B7":'6', "B8":'.', "B9":'8',
            "C1":'7', "C2":'.', "C3":'6', "C4":'.', "C5":'8', "C6":'.', "C7":'.', "C8":'.', "C9":'.',
            "D1":'.', "D2":'.', "D3":'.', "D4":'2', "D5":'.', "D6":'8', "D7":'.', "D8":'6', "D9":'5',
            "E1":'.', "E2":'9', "E3":'2', "E4":'.', "E5":'4', "E6":'7', "E7":'.', "E8":'.', "E9":'3',
            "F1":'.', "F2":'.', "F3":'.', "F4":'.', "F5":'.', "F6":'.', "F7":'.', "F8":'.', "F9":'.',
            "G1":'.', "G2":'.', "G3":'.', "G4":'8', "G5":'.', "G6":'.', "G7":'.', "G8":'.', "G9":'1',
            "H1":'4', "H2":'6', "H3":'5', "H4":'.', "H5":'2', "H6":'.', "H7":'.', "H8":'8', "H9":'9',
            "I1":'3', "I2":'.', "I3":'.', "I4":'.', "I5":'.', "I6":'9', "I7":'5', "I8":'.', "I9":'6'
            }
        self.moderate_level_puzzle_solution = {
            "A1":'5', "A2":'8', "A3":'1', "A4":'7', "A5":'6', "A6":'4', "A7":'3', "A8":'9', "A9":'2',
            "B1":'9', "B2":'2', "B3":'4', "B4":'3', "B5":'1', "B6":'5', "B7":'6', "B8":'7', "B9":'8',
            "C1":'7', "C2":'3', "C3":'6', "C4":'9', "C5":'8', "C6":'2', "C7":'1', "C8":'5', "C9":'4',
            "D1":'1', "D2":'4', "D3":'7', "D4":'2', "D5":'3', "D6":'8', "D7":'9', "D8":'6', "D9":'5',
            "E1":'6', "E2":'9', "E3":'2', "E4":'5', "E5":'4', "E6":'7', "E7":'8', "E8":'1', "E9":'3',
            "F1":'8', "F2":'5', "F3":'3', "F4":'6', "F5":'9', "F6":'1', "F7":'2', "F8":'4', "F9":'7',
            "G1":'2', "G2":'7', "G3":'9', "G4":'8', "G5":'5', "G6":'6', "G7":'4', "G8":'3', "G9":'1',
            "H1":'4', "H2":'6', "H3":'5', "H4":'1', "H5":'2', "H6":'3', "H7":'7', "H8":'8', "H9":'9',
            "I1":'3', "I2":'1', "I3":'8', "I4":'4', "I5":'7', "I6":'9', "I7":'5', "I8":'2', "I9":'6'
            }

        self.hard_level_puzzle = {
            "A1":'.', "A2":'.', "A3":'9', "A4":'.', "A5":'2', "A6":'1', "A7":'4', "A8":'.', "A9":'.',
            "B1":'7', "B2":'.', "B3":'.', "B4":'.', "B5":'3', "B6":'.', "B7":'.', "B8":'.', "B9":'6',
            "C1":'.', "C2":'6', "C3":'.', "C4":'.', "C5":'.', "C6":'4', "C7":'.', "C8":'2', "C9":'.',
            "D1":'9', "D2":'.', "D3":'5', "D4":'.', "D5":'.', "D6":'.', "D7":'.', "D8":'8', "D9":'.',
            "E1":'.', "E2":'.', "E3":'.', "E4":'.', "E5":'.', "E6":'.', "E7":'.', "E8":'.', "E9":'.',
            "F1":'8', "F2":'.', "F3":'3', "F4":'.', "F5":'6', "F6":'.', "F7":'.', "F8":'1', "F9":'.',
            "G1":'.', "G2":'.', "G3":'.', "G4":'.', "G5":'.', "G6":'.', "G7":'.', "G8":'5', "G9":'2',
            "H1":'.', "H2":'.', "H3":'.', "H4":'2', "H5":'.', "H6":'8', "H7":'.', "H8":'3', "H9":'.',
            "I1":'.', "I2":'.', "I3":'.', "I4":'.', "I5":'4', "I6":'9', "I7":'.', "I8":'.', "I9":'.'
            }

        self.hard_level_puzzle_solution = {
            "A1":'3', "A2":'8', "A3":'9', "A4":'6', "A5":'2', "A6":'1', "A7":'4', "A8":'7', "A9":'5',
            "B1":'7', "B2":'2', "B3":'4', "B4":'8', "B5":'3', "B6":'5', "B7":'1', "B8":'9', "B9":'6',
            "C1":'5', "C2":'6', "C3":'1', "C4":'7', "C5":'9', "C6":'4', "C7":'3', "C8":'2', "C9":'8',
            "D1":'9', "D2":'7', "D3":'5', "D4":'4', "D5":'1', "D6":'2', "D7":'6', "D8":'8', "D9":'3',
            "E1":'6', "E2":'1', "E3":'2', "E4":'9', "E5":'8', "E6":'3', "E7":'5', "E8":'4', "E9":'7',
            "F1":'8', "F2":'4', "F3":'3', "F4":'5', "F5":'6', "F6":'7', "F7":'2', "F8":'1', "F9":'9',
            "G1":'4', "G2":'3', "G3":'8', "G4":'1', "G5":'7', "G6":'6', "G7":'9', "G8":'5', "G9":'2',
            "H1":'1', "H2":'9', "H3":'6', "H4":'2', "H5":'5', "H6":'8', "H7":'7', "H8":'3', "H9":'4',
            "I1":'2', "I2":'5', "I3":'7', "I4":'3', "I5":'4', "I6":'9', "I7":'8', "I8":'6', "I9":'1'
            }

        self.no_answerable_puzzle = {
            "A1":'6', "A2":'.', "A3":'7', "A4":'.', "A5":'4', "A6":'.', "A7":'.', "A8":'.', "A9":'2',
            "B1":'9', "B2":'.', "B3":'.', "B4":'7', "B5":'3', "B6":'.', "B7":'4', "B8":'5', "B9":'.',
            "C1":'4', "C2":'.', "C3":'5', "C4":'.', "C5":'.', "C6":'.', "C7":'.', "C8":'.', "C9":'.',
            "D1":'6', "D2":'.', "D3":'.', "D4":'.', "D5":'8', "D6":'.', "D7":'.', "D8":'.', "D9":'.',
            "E1":'.', "E2":'.', "E3":'.', "E4":'9', "E5":'.', "E6":'.', "E7":'3', "E8":'2', "E9":'.',
            "F1":'2', "F2":'8', "F3":'3', "F4":'5', "F5":'.', "F6":'.', "F7":'6', "F8":'4', "F9":'9',
            "G1":'.', "G2":'7', "G3":'.', "G4":'.', "G5":'.', "G6":'.', "G7":'.', "G8":'.', "G9":'3',
            "H1":'.', "H2":'.', "H3":'.', "H4":'6', "H5":'5', "H6":'7', "H7":'8', "H8":'.', "H9":'4',
            "I1":'.', "I2":'.', "I3":'6', "I4":'4', "I5":'2', "I6":'3', "I7":'5', "I8":'9', "I9":'7'
            }
        
        self.invalid_solution = '967845132928736451435219786649382175751964328283571649574198263392657814816423597'
        self.recursive_solver = Recursive()

    def test_recursive_algorithm_should_solve_an_easy_level_sudoku_puzzle(self):
        actual_results = self.recursive_solver.solve(self.easy_level_puzzle)
        expected_result = self.easy_level_puzzle_solution
        self.assertEqual(expected_result, actual_results)

    def test_recursive_algorithm_should_solve_a_moderate_level_sudoku_puzzle(self):
        actual_results = self.recursive_solver.solve(self.moderate_level_puzzle)
        expected_result = self.moderate_level_puzzle_solution
        self.assertEqual(expected_result, actual_results)

    def test_recursive_algorithm_should_solve_a_hard_level_sudoku_puzzle(self):    
        actual_results = self.recursive_solver.solve(self.hard_level_puzzle)
        expected_result = self.hard_level_puzzle_solution
        self.assertEqual(expected_result, actual_results)

    def test_recursive_algorithm_should_raise_an_InvalidSudokuException_if_sudoku_puzzle_has_no_solution(self):
        with self.assertRaises(InvalidSudokuException):
            self.recursive_solver.solve(self.no_answerable_puzzle)

    def test_recursive_algorithm_should_solve_an_already_solved_sudoku_puzzle(self):
        actual_results = self.recursive_solver.solve(self.hard_level_puzzle_solution)
        expected_result = self.hard_level_puzzle_solution
        self.assertEqual(expected_result, actual_results)

    def test_is_valid_solution_should_return_false_if_solution_is_invalid(self):
        self.assertFalse(self.recursive_solver.is_valid_solution(self.invalid_solution))


if __name__ == '__main__':
    unittest.main()