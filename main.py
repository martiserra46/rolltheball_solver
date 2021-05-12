from game import Game
from levels import levels
from solver import Solver

if __name__ == '__main__':
    is_valid = False
    board = levels[1]
    print("\n-- ROLL THE BALL --\n")
    board.print()
    print()
    text = ""
    while not is_valid:
        print("Play (p)")
        print("Show solution (s)")
        text = input("- ")
        if text == 'p' or text == 's':
            is_valid = True
    if text == 'p':
        game = Game()
        game.play(board)
    else:
        solver = Solver()
        solver.print_solution(board)