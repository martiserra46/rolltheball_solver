from constants import PRINT_SIZE
from utils import next_row_col, get_opposite_direction
from block import Block, Filled, Empty
from enums import Direction, BlockType

"""
This class represents the Board
"""
class Board():
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[Empty() for j in range(cols)] for i in range(rows)]
        self.can_move_positions = set()
        self.init_block_row_col = None
        self.solved = None
    
    def add_block(self, row, col, block):
        self.matrix[row][col] = block
    
    def get_block(self, row, col):
        return self.matrix[row][col]
    
    def print(self):
        for row in range(self.rows):
            for position_row in range(PRINT_SIZE*3):
                rows = []
                for col in range(self.cols):
                    block = self.matrix[row][col]
                    rows.append(block.rows_to_draw[position_row])
                row_to_print = '   '.join(rows)
                print(row_to_print)
            print()
    
    def can_move(self, row, col, direction):
        if (row, col, direction) in self.can_move_positions:
            return True
        if (row < 0 or row >= self.rows or col < 0 or col >= self.cols):
            return False
        block = self.matrix[row][col]
        if not isinstance(block, Filled):
            return False
        if block.block_type != BlockType.MOVABLE:
            return False
        if row == 0 and direction == Direction.TOP:
            return False
        if col == 0 and direction == Direction.LEFT:
            return False
        if row == self.rows - 1 and direction == Direction.BOTTOM:
            return False
        if col == self.cols - 1 and direction == Direction.RIGHT:
            return False
        (next_row, next_col) = next_row_col(row, col, direction)
        if not isinstance(self.matrix[next_row][next_col], Empty):
            return False
        self.can_move_positions.add((row, col, direction))
        return True
    
    def move_block(self, row, col, direction):
        if self.can_move(row, col, direction):
            next_row, next_col = next_row_col(row, col, direction)
            block = self.matrix[row][col]
            self.matrix[row][col] = self.matrix[next_row][next_col]
            self.matrix[next_row][next_col] = block
            self.can_move_positions.clear()
            self.solved = None
            return True
        return False
    
    def is_solved(self):
        if self.solved is not None:
            return self.solved
        (row, col) = self.find_init_block_row_col()
        if row is None:
            return False
        prev_row, prev_col = None, None
        can_continue = True
        is_solved = False
        while can_continue:
            (next_row, next_col) = self.compute_next_row_col(row, col, prev_row, prev_col)
            prev_row, prev_col = row, col
            row, col = next_row, next_col
            if row is None:
                can_continue = False
            elif self.matrix[row][col].block_type == BlockType.END:
                can_continue = False
                is_solved = True
        self.solved = is_solved
        return is_solved
    
    def find_init_block_row_col(self):
        if self.init_block_row_col is not None:
            (row, col) = self.init_block_row_col
            return row, col
        for i in range(self.rows):
            for j in range(self.cols):
                if isinstance(self.matrix[i][j], Filled):
                    if self.matrix[i][j].block_type == BlockType.INIT:
                        self.init_block_row_col = (i, j)
                        return i, j
        return None, None
    
    def compute_next_row_col(self, row, col, prev_row, prev_col):
        block = self.matrix[row][col]
        if not isinstance(block, Filled):
            return (None, None)
        directions = block.directions
        positions = set()
        for direction in directions:
            (next_row, next_col) = next_row_col(row, col, direction)
            if next_row >= 0 and next_row < self.rows and next_col >= 0 and next_col < self.cols:
                block = self.matrix[next_row][next_col]
                if isinstance(block, Filled):
                    if get_opposite_direction(direction) in block.directions:
                        positions.add((next_row, next_col))
        if (prev_row, prev_col) in positions:
            positions.remove((prev_row, prev_col))
        if len(positions) == 0:
            return (None, None)
        else:
            return next(iter(positions))
