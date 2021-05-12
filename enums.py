from enum import IntEnum

class BlockType(IntEnum):
    INIT = 1
    END = 2
    MOVABLE = 3
    FIXED = 4

class Direction(IntEnum):
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    LEFT = 4