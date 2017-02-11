import random
from copy import deepcopy

def create_dominoes_game(rows, cols):
    board = []
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(False)
        board.append(col[:])
    return DominoesGame(board)

class DominoesGame(object):
    b = []
    def __init__(self, board):
        self.b = board
    def get_board(self):
        return self.b
    def reset(self):
        self = create_dominoes_game(len(self.b), len(self.b[0]))
    def is_legal_move(self, row, col, vertical):
        if vertical:
            if not self.b[row][col] and not self.b[row + 1][col]:
                return True
        else:
            if not self.b[row][col] and not self.b[row][col + 1]:
                return True
        return False

    def legal_moves(self, vertical):
        for i in range(len(self.b)):
            for j in range(len(self.b[0])):
                if not self.b[i][j]:
                    if vertical and i + 1 < len(self.b):
                        if not self.b[i + 1][j]:
                            yield tuple((i, j))
                    if not vertical and j + 1 < len(self.b[0]):
                        if not self.b[i][j + 1]:
                            yield tuple((i, j))

    def perform_move(self, row, col, vertical):
        if not self.b[row][col]:
            if vertical:
                self.b[row][col] = True
                self.b[row + 1][col] = True
            else:
                self.b[row][col] = True
                self.b[row][col + 1] = True

    def game_over(self, vertical):
        if len(list(self.legal_moves(vertical))):
            return False
        return True

    def copy(self):
        return deepcopy(self)

    def successors(self, vertical):
        moves = list(self.legal_moves(vertical))
        for i in range(len(moves)):
            newboard = self.copy()
            if vertical:
                newboard.b[moves[i][0]][moves[i][1]] = True
                newboard.b[moves[i][0] + 1][moves[i][1]] = True
            else:
                newboard.b[moves[i][0]][moves[i][1]] = True
                newboard.b[moves[i][0]][moves[i][1] + 1] = True
            yield moves[i], newboard

    def get_random_move(self, vertical):
        moves = list(self.legal_moves(vertical))
        return moves[random.randint(0, len(moves) - 1)]

     # Required
    def get_best_move(self, vertical, limit):
        alpha = -1000
        beta = 1000
        nodes_visited=0
        (move, node_val, nodes_visited) = self.get_max((0,0),vertical, alpha, beta,0, limit, nodes_visited)
        return (move, node_val, nodes_visited)

    def get_max(self, node, vertical, alpha, beta, depth, limit, nodes_visited):
        if depth == limit:
            nodes_visited += 1
            return (node, len(list(self.legal_moves(vertical)))-len(list(self.legal_moves(not vertical))) , nodes_visited) #len(list(newboard.legal_moves(not vertical)))
        v = -1000
        for m, new_g in self.successors(vertical):
            (move, node_val, nodes_visited) = new_g.get_min(m ,not vertical, alpha, beta, depth + 1, limit, nodes_visited)
            if v<node_val:
                node=m
                v = max(v, node_val)
            if v >= beta:
                return (node, v, nodes_visited)
            alpha = max(alpha, v)
        return node, v, nodes_visited

    def get_min(self,node,vertical, alpha, beta, depth, limit,nodes_visited):
        if depth == limit:
            nodes_visited += 1
            return (node, len(list(self.legal_moves(not vertical)))-len(list(self.legal_moves(vertical))), nodes_visited)  # len(list(newboard.legal_moves(not vertical)))
        v = 1000
        for m, new_g in self.successors(vertical):
            (move, node_val, nodes_visited) = new_g.get_max( m ,not vertical, alpha, beta, depth + 1, limit, nodes_visited)
            if v>node_val:
                node=m
                v = min(v, node_val)
            if v <= alpha:
                return (node, v, nodes_visited)
            beta = min(beta, v)
        return node, v, nodes_visited

b = [[False] * 3 for i in range(3)]
g = DominoesGame(b)
print g.get_best_move(True, 1)
print g.get_best_move(True, 2)

b = [[False] * 3 for i in range(3)]
g = DominoesGame(b)
g.perform_move(0, 1, True)
print g.get_best_move(False, 1)
print g.get_best_move(False, 2)
#((2, 0), -3, 2)
#((0, 1), 2, 6)
#((0, 1), 3, 10)