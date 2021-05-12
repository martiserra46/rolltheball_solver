from constants import PRINT_SIZE
from enums import Direction, BlockType

"""
This class represents a Block either Filled or Empty placed at the Board
"""
class Block():
    def __init__(self):
        self.matrix = None
        self.rows_to_draw = None

        self.setup_matrix()
        self.setup_rows_to_draw()
    
    def setup_matrix(self):
        pass
 
    def setup_rows_to_draw(self):
        pass

class Filled(Block):
    def __init__(self, block_type, directions):
        self.block_type = block_type
        self.letter = 'I' if block_type == BlockType.INIT else 'E' if block_type == BlockType.END else 'M' if block_type == BlockType.MOVABLE else 'F'
        self.directions = directions
        self.rows_to_draw = None

        self.setup_rows_to_draw()

    def setup_rows_to_draw(self):
        matrix = self.get_matrix()
        self.rows_to_draw = [' '.join([matrix[i // PRINT_SIZE][j // PRINT_SIZE] for j in range(3*PRINT_SIZE)]) for i in range(3*PRINT_SIZE)]

    def get_matrix(self):
        matrix = [[self.letter for j in range(3)] for i in range(3)]
        if len(self.directions) > 0:
            matrix[1][1] = ' '
            if Direction.TOP in self.directions:
                matrix[0][1] = ' '
            if Direction.RIGHT in self.directions:
                matrix[1][2] = ' '
            if Direction.BOTTOM in self.directions:
                matrix[2][1] = ' '
            if Direction.LEFT in self.directions:
                matrix[1][0] = ' '
        return matrix

    def print(self):
        for row in self.rows_to_draw:
            print(row)

class Empty(Block):
    def __init__(self):
        self.matrix = None
        self.rows_to_draw = None

        self.setup_matrix()
        self.setup_rows_to_draw()
    
    def setup_matrix(self):
        self.matrix = [[' ' for j in range(3)] for i in range(3)]
    
    def setup_rows_to_draw(self):
        self.rows_to_draw = [' '.join([' ' for j in range(3*PRINT_SIZE)]) for i in range(3*PRINT_SIZE)]
