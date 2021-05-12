from board import Board
from block import Block, Filled, Empty
from enums import Direction, BlockType

levels = []

level = Board(2,3)
level.add_block(0,0, Filled(BlockType.INIT, { Direction.RIGHT }))
level.add_block(0,2, Filled(BlockType.END, { Direction.LEFT }))
level.add_block(0,1, Filled(BlockType.MOVABLE, {}))
level.add_block(1,0, Filled(BlockType.MOVABLE, { Direction.LEFT, Direction.RIGHT }))

levels.append(level)

level = Board(4,4)
level.add_block(0,0, Filled(BlockType.INIT, { Direction.BOTTOM }))
level.add_block(0,1, Filled(BlockType.MOVABLE, { }))
level.add_block(0,2, Filled(BlockType.MOVABLE, { }))
level.add_block(0,3, Filled(BlockType.MOVABLE, { }))
level.add_block(1,1, Filled(BlockType.MOVABLE, { Direction.TOP, Direction.BOTTOM }))
level.add_block(1,3, Filled(BlockType.MOVABLE, { }))
level.add_block(2,0, Filled(BlockType.MOVABLE, { Direction.TOP, Direction.BOTTOM }))
level.add_block(2,1, Filled(BlockType.MOVABLE, { }))
level.add_block(2,2, Filled(BlockType.MOVABLE, { Direction.LEFT, Direction.RIGHT }))
level.add_block(3,0, Filled(BlockType.MOVABLE, { Direction.TOP, Direction.RIGHT }))
level.add_block(3,2, Filled(BlockType.FIXED, { Direction.LEFT, Direction.RIGHT }))
level.add_block(3,3, Filled(BlockType.END, { Direction.LEFT }))

levels.append(level)
