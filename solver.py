from board import Board
from enums import Direction
from utils import direction_to_string, next_row_col, get_opposite_direction
import copy
import time

class Solver():

    def print_solution(self, board):
        print("\n-- SOLUTION --\n")
        board.print()
        print()
        movements, duration, num_solutions_checked = self.solve(board)
        print(str(len(movements)) + " movements\n")
        print(str(duration) + " seconds\n")
        print(str(num_solutions_checked) + " possible solutions have been checked\n")
        for movement in movements:
            self.apply_movement(board, movement)
            string_movement = self.get_string_movement(movement)
            print(string_movement + "\n")
            board.print()
            print()
    
    def solve(self, board):
        start_time = time.time()
        list_movements = [[]]
        solution_found = False
        movements = None
        num_solutions_checked = 0
        while not solution_found and len(list_movements) > 0:
            movements = list_movements.pop(0)
            if self.is_solution(board, movements):
                solution_found = True
            else:
                new_list_movements = self.new_list_movements(board, movements)
                list_movements = list_movements + new_list_movements
            num_solutions_checked += 1
        duration = time.time() - start_time
        return movements, duration, num_solutions_checked
    
    def is_solution(self, board, movements):
        self.apply_movements(board, movements)
        is_solved = board.is_solved()
        reverse_movements = self.get_reverse_movements(movements)
        self.apply_movements(board, reverse_movements)
        return is_solved
    
    def new_list_movements(self, board, movements):
        self.apply_movements(board, movements)
        new_list_movements = []
        directions = list(map(int, Direction))
        for row in range(board.rows):
            for col in range(board.cols):
                for direction in directions:
                    if board.can_move(row, col, direction):
                        new_movements = copy.deepcopy(movements)
                        new_movements.append((row, col, direction))
                        new_list_movements.append(new_movements)
        reverse_movements = self.get_reverse_movements(movements)
        self.apply_movements(board, reverse_movements)
        return new_list_movements
    
    def apply_movement(self, board, movement):
        (row, col, direction) = movement
        board.move_block(row, col, direction)
    
    def apply_movements(self, board, movements):
        for movement in movements:
            self.apply_movement(board, movement)
    
    def get_reverse_movements(self, movements):
        new_movements = []
        for movement in movements:
            new_movements.insert(0, self.get_reverse_movement(movement))
        return new_movements
    
    def get_reverse_movement(self, movement):
        (row, col, direction) = movement
        new_row, new_col = next_row_col(row, col, direction)
        new_direction = get_opposite_direction(direction)
        return (new_row, new_col, new_direction)

    def get_string_movement(self, movement):
        (row, col, direction) = movement
        return "row: " + str(row) + ", col: " + str(col) + ", direction: " + direction_to_string(direction)