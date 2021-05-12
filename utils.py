from enums import Direction

def get_opposite_direction(direction):
    if direction == Direction.TOP:
        return Direction.BOTTOM
    elif direction == Direction.BOTTOM:
        return Direction.TOP
    elif direction == Direction.RIGHT:
        return Direction.LEFT
    else:
        return Direction.RIGHT

def next_row_col(row, col, direction):
    next_row = row
    next_col = col
    if direction == Direction.TOP:
        next_row -= 1
    elif direction == Direction.RIGHT:
        next_col += 1
    elif direction == Direction.BOTTOM:
        next_row += 1
    else:
        next_col -= 1
    return (next_row, next_col)

def convert_to_direction(direction_string):
    if direction_string == "top":
        return Direction.TOP
    elif direction_string == "right":
        return Direction.RIGHT
    elif direction_string == "bottom":
        return Direction.BOTTOM
    elif direction_string == "left":
        return Direction.LEFT
    return None

def direction_to_string(direction):
    if direction == Direction.TOP:
        return "top"
    elif direction == Direction.RIGHT:
        return "right"
    elif direction == Direction.BOTTOM:
        return "bottom"
    elif direction == Direction.LEFT:
        return "left"
    return None