############################################################
# Section 1: Tile Puzzle
############################################################

import random
from copy import deepcopy
import Queue

def create_tile_puzzle(rows, cols):
    board = []
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append((i * cols) + j + 1)
        board.append(col[:])
    board[-1][-1] = 0
    return TilePuzzle(board)


class TilePuzzle(object):
    b = []

    def __init__(self, board):
        self.b = board

    def get_board(self):
        return self.b

    def perform_move(self, direction):
        rows = len(self.b)
        cols = len(self.b[0])
        performed = False
        for i in range(rows):
            for j in range(cols):
                if self.b[i][j] == 0:
                    if direction == 'up':
                        if i - 1 >= 0:
                            temp = self.b[i - 1][j]
                            self.b[i - 1][j] = self.b[i][j]
                            self.b[i][j] = temp
                            return True
                    if direction == 'down':
                        if i + 1 <= rows - 1:
                            temp = self.b[i + 1][j]
                            self.b[i + 1][j] = self.b[i][j]
                            self.b[i][j] = temp
                            return True
                    if direction == 'left':
                        if j - 1 >= 0:
                            temp = self.b[i][j - 1]
                            self.b[i][j - 1] = self.b[i][j]
                            self.b[i][j] = temp
                            return True
                    if direction == 'right':
                        if j + 1 <= cols - 1:
                            temp = self.b[i][j]
                            self.b[i][j] = self.b[i][j + 1]
                            self.b[i][j + 1] = temp
                            return True
                    return False

    def scramble(self, num_moves):
        case = ['up', 'down', 'left', 'right']
        dir = random.choice(case)
        for i in range(num_moves):
            dir = random.choice(case)
            self.perform_move(dir)

    def is_solved(self):
        rows = len(self.b)
        cols = len(self.b[0])
        solved = create_tile_puzzle(rows, cols)
        isit = True
        for i in range(rows):
            for j in range(cols):
                if self.b[i][j] != solved.b[i][j]:
                    isit = False;
                    continue;
        return isit;

    def copy(self):
        return deepcopy(self)

    def successors(self):
        rows = len(self.b)
        cols = len(self.b[0])
        case = ['up', 'down', 'left', 'right']
        for i in range(rows):
            for j in range(cols):
                if self.b[i][j] == 0:
                    for k in range(len(case)):
                        c = self.copy()
                        action = c.perform_move(case[k])
                        if action:
                            yield case[k], c

    # Required
    def find_solutions_iddfs(self):
        moves = []
        if not self.is_solved():
            boards = [self];
            moves = [[]]
            solutions = []
        while len(solutions) == 0:
            successors_boards = []
            successors_moves = []
            successors_boards, successors_moves = iddfs_helper(boards, moves)
            boards = successors_boards[:]
            moves = successors_moves[:]
            for i in range(len(successors_boards)):
                if successors_boards[i].is_solved():
                    solutions.append(successors_moves[i])
        for x in (solutions):
            yield x

    def find_solution_a_star(self):
        q = Queue.PriorityQueue()
        visited=[]
        move = []
        if not self.is_solved():
            md = calculate_manhattan(self.b)
            node = tuple((self, move));
            q.put((md, node))
            visited.append([self.b])
            solution_found = False
        while (q.qsize() != 0):
            (x, (boards, moves)) = q.get()
            successors_boards = []
            successors_moves = []
            successors_boards, successors_moves = astar_helper(boards, moves)
            for i in range(len(successors_boards)):
                if successors_boards[i].is_solved():
                    return successors_moves[i]
                md = calculate_manhattan(successors_boards[i].b)
                if not is_visited(successors_boards[i].b,visited):
                    q.put((md + len(successors_moves[i]), tuple((successors_boards[i], successors_moves[i]))))
                    visited.append(successors_boards[i].b)

def iddfs_helper(boards, moves):
    successors_boards = []
    successors_moves = []
    for i in range(len(boards)):
        for move, board in boards[i].successors():
            moved = [];
            if len(moves):
                moved = moves[i][:]
            successors_boards.append(board)
            moved.append(move);
            successors_moves.append(moved)
    return successors_boards, successors_moves

def astar_helper(boards, moves):
    successors_boards = []
    successors_moves = []
    for move, board in boards.successors():
        moved = [];
        if len(moves):
            moved = moves[:]
        successors_boards.append(board)
        moved.append(move);
        successors_moves.append(moved)
    return successors_boards, successors_moves

def calculate_manhattan(board):
    rows = len(board)
    cols = len(board[0])
    manhattandist = 0
    for i in range(rows):
        for j in range(cols):
            if board[i][j] > 0:
                manhattandist += abs(board[i][j] - ((i * cols) + j) - 1)
    return manhattandist

def is_visited(board,visited):
    rows = len(board)
    cols = len(board[0])
    if len(visited):
        for k in range(len(visited)):
            count=0
            for i in range(rows):
                for j in range(cols):
                    if visited[k][i][j]== board[i][j]:
                        count+=1
            if count==9:
                return True
    return False
