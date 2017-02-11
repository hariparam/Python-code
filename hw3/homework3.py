############################################################
# CIS 521: Homework 3
############################################################

student_name = "Hari Sudhan Parmeswaran"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import Queue
import random
from copy import deepcopy

############################################################
# Section 1: Tile Puzzle
############################################################

def create_tile_puzzle(rows, cols):
    board = []
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append((i * cols) + j + 1)
        board.append(col[:])
    board[-1][-1]=0
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
            moves = []
            solutions_found = False
        while solutions_found==False: #len(solutions) == 0:
            successors_boards = []
            successors_moves = []
            successors_boards, successors_moves = iddfs_helper(boards, moves)
            boards = successors_boards[:]
            moves = successors_moves[:]
            for i in range(len(successors_boards)):
                if successors_boards[i].is_solved():
                    solutions_found=True
                    yield successors_moves[i]
                    #solutions.append(successors_moves[i])
        #yield solutions

    def find_solution_a_star(self):
        q = Queue.PriorityQueue()
        visited=[]
        move = []
        if not self.is_solved():
            md = calculate_manhattan(self.b)
            node = tuple((self, move));
            q.put((md, node))
            visited.append(self.get_board())
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
                    visited.append(successors_boards[i].get_board())

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


############################################################
# Section 2: Grid Navigation
############################################################

def find_path(start, goal, scene):
    rows = len(scene)
    cols = len(scene[0])
    array=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            if scene[i][j]:
                row.append(-1)
            else:
                row.append(0)
        array.append(row)
    if array[start[0]][start[1]]==-1 | array[goal[0]][goal[1]]==-1 |array[start[0]][start[1]]==array[goal[0]][goal[1]]:
        return None
    else:
        currentnode=start
        q=Queue.PriorityQueue()
        dist=getecdist(currentnode,goal)
        moves=[currentnode]
        q.put((dist,(currentnode, moves)))
        while currentnode!=goal and (q.qsize() != 0):
            successor_nodes=[]
            successor_moves=[]
            moves_made = []
            node = ()
            x = q.get()
            (node, moves_made) = x[1]
            if node==goal:
                return moves_made
            successor_moves=get_successors(node,array)
            currentnode=node
            if len(successor_moves)>0:
                for m in range(len(successor_moves)):
                    newmoves=moves_made[:]
                    if successor_moves[m]=='up':
                        newnode=(currentnode[0]-1,currentnode[1])
                        ecdist=getecdist(newnode,goal)
                        if array[newnode[0]][newnode[1]]>(ecdist+len(moves_made)+1) or array[newnode[0]][newnode[1]]==0:
                            array[newnode[0]][newnode[1]]=ecdist+len(moves_made)+1
                            newmoves.append(newnode)
                            q.put(((ecdist+len(moves_made)+1),(newnode,newmoves)))
                    if successor_moves[m]=='down':
                        newnode=(currentnode[0]+1,currentnode[1])
                        ecdist=getecdist(newnode,goal)
                        if array[newnode[0]][newnode[1]]>(ecdist+len(moves_made)+1) or array[newnode[0]][newnode[1]]==0:
                            array[newnode[0]][newnode[1]]=ecdist+len(moves_made)+1
                            newmoves.append(newnode)
                            q.put(((ecdist + len(moves_made) + 1), (newnode, newmoves)))
                    if successor_moves[m]=='left':
                        newnode=(currentnode[0],currentnode[1]-1)
                        ecdist=getecdist(newnode,goal)
                        if array[newnode[0]][newnode[1]]>(ecdist+len(moves_made)+1) or array[newnode[0]][newnode[1]]==0:
                            array[newnode[0]][newnode[1]]=ecdist+len(moves_made)+1
                            newmoves.append(newnode)
                            q.put(((ecdist + len(moves_made) + 1), (newnode, newmoves)))
                    if successor_moves[m]=='right':
                        newnode=(currentnode[0],currentnode[1]+1)
                        ecdist=getecdist(newnode,goal)
                        if array[newnode[0]][newnode[1]]>(ecdist+len(moves_made)+1) or array[newnode[0]][newnode[1]]==0:
                            array[newnode[0]][newnode[1]]=ecdist+len(moves_made)+1
                            newmoves.append(newnode)
                            q.put(((ecdist + len(moves_made) + 1), (newnode, newmoves)))
                    if successor_moves[m]=='upleft':
                        newnode=(currentnode[0]-1,currentnode[1]-1)
                        ecdist=getecdist(newnode,goal)
                        if array[newnode[0]][newnode[1]]>(ecdist+len(moves_made)+1) or array[newnode[0]][newnode[1]]==0:
                            array[newnode[0]][newnode[1]]=ecdist+len(moves_made)+1
                            newmoves.append(newnode)
                            q.put(((ecdist + len(moves_made) + 1), (newnode, newmoves)))
                    if successor_moves[m] == 'upright':
                        newnode = (currentnode[0]-1, currentnode[1] + 1)
                        ecdist = getecdist(newnode, goal)
                        if array[newnode[0]][newnode[1]] > (ecdist + len(moves_made) + 1) or array[newnode[0]][
                            newnode[1]] == 0:
                            array[newnode[0]][newnode[1]] = ecdist + len(moves_made) + 1
                            newmoves.append(newnode)
                            q.put(((ecdist + len(moves_made) + 1), (newnode, newmoves)))
                    if successor_moves[m]=='downright':
                        newnode=(currentnode[0]+1,currentnode[1]+1)
                        ecdist=getecdist(newnode,goal)
                        if array[newnode[0]][newnode[1]]>(ecdist+len(moves_made)+1) or array[newnode[0]][newnode[1]]==0:
                            array[newnode[0]][newnode[1]]=ecdist+len(moves_made)+1
                            newmoves.append(newnode)
                            q.put(((ecdist + len(moves_made) + 1), (newnode, newmoves)))
                    if successor_moves[m]=='downleft':
                        newnode=(currentnode[0]+1,currentnode[1]-1)
                        ecdist=getecdist(newnode,goal)
                        if array[newnode[0]][newnode[1]]>(ecdist+len(moves_made)+1) or array[newnode[0]][newnode[1]]==0:
                            array[newnode[0]][newnode[1]]=ecdist+len(moves_made)+1
                            newmoves.append(newnode)
                            q.put(((ecdist + len(moves_made) + 1), (newnode, newmoves)))
    if len(moves_made)==1 or q.qsize()==0:
        return None
    return moves_made

def getecdist(a,b):
    dist=abs(a[0]-b[0])+abs(a[1]-b[1])
    return  dist

def get_successors(currentnode, array):
    moves=[]
    rows = len(array)
    cols = len(array[0])
    if (currentnode[1]-1>=0):
        if array[currentnode[0]][currentnode[1]-1]!=-1:
            moves.append('left')
    if (currentnode[1]+1)<cols:
        if array[currentnode[0]][currentnode[1]+1]!=-1:
            moves.append('right')
    if (currentnode[0]-1)>=0:
        if array[currentnode[0]-1][currentnode[1]]!=-1:
            moves.append('up')
    if (currentnode[0]+1)<rows:
        if array[currentnode[0]+1][currentnode[1]]!=-1:
            moves.append('down')
    if (currentnode[0] - 1) >=0 and (currentnode[1]-1>=0):
        if array[currentnode[0] - 1][currentnode[1]-1] != -1:
            moves.append('upleft')
    if (currentnode[0] - 1) >=0 and (currentnode[1]+1)<cols:
        if array[currentnode[0] - 1][currentnode[1]+1] != -1:
            moves.append('upright')
    if (currentnode[0]+1)<rows and (currentnode[1]-1>=0):
        if array[currentnode[0]+1][currentnode[1]-1] != -1:
            moves.append('downleft')
    if (currentnode[0] + 1) < rows and (currentnode[1]+1)<cols:
        if array[currentnode[0]+1][currentnode[1]+1] != -1:
            moves.append('downright')
    return moves



############################################################
# Section 3: Linear Disk Movement, Revisited
############################################################

def solve_distinct_disks(length, n):
    array = [0] * length
    for i in range(n):
        array[i] = i + 1
    index = n - 1
    move = []
    q = Queue.PriorityQueue()
    if not is_unique_solved(array, n):
        q.put(((len(move) + get_heuristic(array)), (array, move)))
    while (not is_unique_solved(array, n)):
        arraylist = []
        moves = []
        (x, (array, solution)) = q.get()
        [arraylist, moves] = unique_next_moves(array, solution)
        for m in range(len(moves)):
            q.put(((len(moves[m]) + get_heuristic(arraylist[m])), (arraylist[m], moves[m])))
    return solution


def unique_next_moves(array, moved):
    arraylist = []
    moves_list = []
    for i in range(len(array)):
        if array[i] != 0:
            if i - 2 >= 0:
                if array[i - 1] != 0 and array[i - 2] == 0:
                    arraylist.append(array[:])
                    moves_list.append(moved[:])
                    temp = arraylist[-1][i]
                    arraylist[-1][i] = arraylist[-1][i - 2]
                    arraylist[-1][i - 2] = temp
                    moves_list[-1].append(tuple((i, i - 2)))
            if i - 1 >= 0:
                if array[i - 1] == 0:
                    arraylist.append(array[:])
                    moves_list.append(moved[:])
                    temp = arraylist[-1][i]
                    arraylist[-1][i] = arraylist[-1][i - 1]
                    arraylist[-1][i - 1] = temp
                    moves_list[-1].append(tuple((i, i - 1)))
            if i + 1 <= len(array) - 1:
                if array[i + 1] == 0:
                    arraylist.append(array[:])
                    moves_list.append(moved[:])
                    temp = arraylist[-1][i]
                    arraylist[-1][i] = arraylist[-1][i + 1]
                    arraylist[-1][i + 1] = temp
                    moves_list[-1].append(tuple((i, i + 1)))
            if i + 2 <= len(array) - 1:
                if array[i + 1] != 0 and array[i + 2] == 0:
                    arraylist.append(array[:])
                    moves_list.append(moved[:])
                    temp = arraylist[-1][i]
                    arraylist[-1][i] = arraylist[-1][i + 2]
                    arraylist[-1][i + 2] = temp
                    moves_list[-1].append(tuple((i, i + 2)))
    return arraylist, moves_list


def is_unique_solved(array, n):
    for i in range(len(array)):
        if i < n:
            if (array[len(array) - 1 - i] != i + 1):
                return False
        else:
            if (array[len(array) - 1 - i] != 0):
                return False
    return True


def get_heuristic(array):
    h = 0
    for i in range(len(array)):
        if array[i]:
            h += len(array) - i - array[i];
    return h


############################################################
# Section 4: Dominoes Game
############################################################

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

############################################################
# Section 5: Feedback
############################################################

feedback_question_1 = """
15hrs
"""

feedback_question_2 = """
alpha beta pruning"""

feedback_question_3 = """
more details and conceptual understanding of alpha-beta pruning could've been done"""


