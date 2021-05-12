from board import Board
from enums import Direction
from utils import convert_to_direction

class Game():
    def play(self, board):
        print("\n-- PLAY --\n")
        num_moves = 0
        while (not board.is_solved()):
            board.print()
            row, col, direction = self.input_movement(board)
            board.move_block(row, col, direction)
            print()
            num_moves += 1
        board.print()
        print("You solved it with " + str(num_moves) + " movements")
    
    def input_movement(self, board):
        row, col = self.input_row_col(board)
        direction = self.input_direction(board, row, col)
        return row, col, direction
    
    def input_row_col(self, board):
        is_valid = False
        directions = list(map(int, Direction))
        row, col = None, None
        while not is_valid:
            position = input("row, col: ").split(",")
            try:
                row, col = int(position[0]), int(position[1])
                valid_direction = False
                for direction in directions:
                    if board.can_move(row, col, direction):
                        valid_direction = True
                if not valid_direction:
                    raise Exception
                is_valid = True
            except:
                print("Invalid input")
            print()
        return row, col

    def input_direction(self, board, row, col):
        is_valid = False
        direction = None
        while not is_valid:
            direction_string = input("top, right, bottom, left: ")
            direction = convert_to_direction(direction_string)
            if direction is not None:
                if board.can_move(row, col, direction):
                    is_valid = True
            if not is_valid:
                print("Invalid input")
            print()
        return direction