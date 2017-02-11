import Queue
from copy import deepcopy

def printsudoku(a):
    for i in range(9):
        for j in range(9):
            print a.board[(i, j)],
        print '\n'


def get_neighbors(i, j):
    n = []
    if i % 3 == 0 and j % 3 == 0:
        n.append((i, j + 1))
        n.append((i, j + 2))
        n.append((i + 1, j))
        n.append((i + 1, j + 1))
        n.append((i + 1, j + 2))
        n.append((i + 2, j + 0))
        n.append((i + 2, j + 1))
        n.append((i + 2, j + 2))
    elif i % 3 == 0 and j % 3 == 1:
        n.append((i, j - 1))
        n.append((i, j + 1))
        n.append((i + 1, j - 1))
        n.append((i + 1, j))
        n.append((i + 1, j + 1))
        n.append((i + 2, j - 1))
        n.append((i + 2, j))
        n.append((i + 2, j + 1))
    elif i % 3 == 0 and j % 3 == 2:
        n.append((i, j - 2))
        n.append((i, j - 1))
        n.append((i + 1, j - 2))
        n.append((i + 1, j - 1))
        n.append((i + 1, j))
        n.append((i + 2, j - 2))
        n.append((i + 2, j - 1))
        n.append((i + 2, j))
    elif i % 3 == 1 and j % 3 == 0:
        n.append((i - 1, j + 0))
        n.append((i - 1, j + 1))
        n.append((i - 1, j + 2))
        n.append((i, j + 1))
        n.append((i, j + 2))
        n.append((i + 1, j + 0))
        n.append((i + 1, j + 1))
        n.append((i + 1, j + 2))
    elif i % 3 == 1 and j % 3 == 1:
        n.append((i - 1, j - 1))
        n.append((i - 1, j))
        n.append((i - 1, j + 1))
        n.append((i, j - 1))
        n.append((i, j + 1))
        n.append((i + 1, j - 1))
        n.append((i + 1, j))
        n.append((i + 1, j + 1))
    elif i % 3 == 1 and j % 3 == 2:
        n.append((i - 1, j - 2))
        n.append((i - 1, j - 1))
        n.append((i - 1, j))
        n.append((i, j - 2))
        n.append((i, j - 1))
        n.append((i + 1, j - 2))
        n.append((i + 1, j - 1))
        n.append((i + 1, j))
    elif i % 3 == 2 and j % 3 == 0:
        n.append((i - 2, j + 0))
        n.append((i - 2, j + 1))
        n.append((i - 2, j + 2))
        n.append((i - 1, j))
        n.append((i - 1, j + 1))
        n.append((i - 1, j + 2))
        n.append((i, j + 1))
        n.append((i, j + 2))
    elif i % 3 == 2 and j % 3 == 1:
        n.append((i - 2, j - 1))
        n.append((i - 2, j + 0))
        n.append((i - 2, j + 1))
        n.append((i - 1, j - 1))
        n.append((i - 1, j + 0))
        n.append((i - 1, j + 1))
        n.append((i, j - 1))
        n.append((i, j + 1))
    else:
        n.append((i - 2, j - 2))
        n.append((i - 2, j - 1))
        n.append((i - 2, j))
        n.append((i - 1, j - 2))
        n.append((i - 1, j - 1))
        n.append((i - 1, j))
        n.append((i, j - 2))
        n.append((i, j - 1))
    for h in range(9):
        if h != i:
            n.append((h, j))
        if h != j:
            n.append((i, h))
    return n


def get_impossible_values(a):
    new_board = deepcopy(a)
    for i in range(9):
        for j in range(9):
            mt=set([])
            if len(a.board[(i, j)]) != 1:
                for h in range(9):
                    if h!=i and len(a.board[(h, j)])==1:
                        mt.update(a.board[(h, j)])
                for k in range(9):
                    if k != j and len(a.board[(i, k)]) == 1:
                        mt.update(a.board[(i, k)])
                if (i == 0 or i == 3 or i == 6) and (j == 0 or j == 3 or j == 6):
                    if len(a.board[(i + 1, j + 1)]) == 1:
                        mt.update(a.board[(i + 1, j + 1)])
                    if len(a.board[(i + 1, j + 2)]) == 1:
                      mt.update(a.board[(i + 1, j + 2)])
                    if len(a.board[(i + 2, j + 1)]) == 1:
                      mt.update(a.board[(i + 2, j + 1)])
                    if len(a.board[(i + 2, j + 2)]) == 1:
                      mt.update(a.board[(i + 2, j + 2)])
                elif (i == 0 or i == 3 or i == 6) and (j == 1 or j == 4 or j == 7):
                    if len(a.board[(i + 1, j - 1)])==1:
                      mt.update(a.board[(i + 1, j - 1)])
                    if len(a.board[(i + 1, j + 1)]) == 1:
                      mt.update(a.board[(i + 1, j + 1)])
                    if len(a.board[(i + 2, j - 1)]) == 1:
                      mt.update(a.board[(i + 2, j - 1)])
                    if len(a.board[(i + 2, j + 1)]) == 1:
                      mt.update(a.board[(i + 2, j + 1)])
                elif (i == 0 or i == 3 or i == 6) and (j == 2 or j == 5 or j == 8):
                    if len(a.board[(i + 1, j - 1)]) == 1:
                      mt.update(a.board[(i + 1, j - 1)])
                    if len(a.board[(i + 1, j - 2)]) == 1:
                      mt.update(a.board[(i + 1, j - 2)])
                    if len(a.board[(i + 2, j - 1)]) == 1:
                      mt.update(a.board[(i + 2, j - 1)])
                    if len(a.board[(i + 2, j - 2)]) == 1:
                      mt.update(a.board[(i + 2, j - 2)])
                elif (i == 1 or i == 4 or i == 7) and (j == 0 or j == 3 or j == 6):
                    if len(a.board[(i - 1, j + 1)]) == 1:
                        mt.update(a.board[(i - 1, j + 1)])
                    if len(a.board[(i - 1, j + 2)]) == 1:
                        mt.update(a.board[(i - 1, j + 2)])
                    if len(a.board[(i + 1, j + 1)]) == 1:
                        mt.update(a.board[(i + 1, j + 1)])
                    if len(a.board[(i + 1, j + 2)]) == 1:
                        mt.update(a.board[(i + 1, j + 2)])
                elif (i == 1 or i == 4 or i == 7) and (j == 1 or j == 4 or j == 7):
                    if len(a.board[(i - 1, j - 1)]) == 1:
                        mt.update(a.board[(i - 1, j - 1)])
                    if len(a.board[(i - 1, j + 1)]) == 1:
                        mt.update(a.board[(i - 1, j + 1)])
                    if len(a.board[(i + 1, j - 1)]) == 1:
                        mt.update(a.board[(i + 1, j - 1)])
                    if len(a.board[(i + 1, j + 1)]) == 1:
                        mt.update(a.board[(i + 1, j + 1)])
                elif (i == 1 or i == 4 or i == 7) and (j == 2 or j == 5 or j == 8):
                    if len(a.board[(i - 1, j - 1)]) == 1:
                        mt.update(a.board[(i - 1, j - 1)])
                    if len(a.board[(i - 1, j - 2)]) == 1:
                        mt.update(a.board[(i - 1, j - 2)])
                    if len(a.board[(i + 1, j - 1)]) == 1:
                        mt.update(a.board[(i + 1, j - 1)])
                    if len(a.board[(i + 1, j - 2)]) == 1:
                        mt.update(a.board[(i + 1, j - 2)])
                elif (i == 2 or i == 5 or i == 8) and (j == 0 or j == 3 or j == 6):
                    if len(a.board[(i - 1, j + 1)]) == 1:
                        mt.update(a.board[(i - 1, j + 1)])
                    if len(a.board[(i - 1, j + 2)]) == 1:
                        mt.update(a.board[(i - 1, j + 2)])
                    if len(a.board[(i - 2, j + 1)]) == 1:
                        mt.update(a.board[(i - 2, j + 1)])
                    if len(a.board[(i - 2, j + 2)]) == 1:
                        mt.update(a.board[(i - 2, j + 2)])
                elif (i == 2 or i == 5 or i == 8) and (j == 1 or j == 4 or j == 7):
                    if len(a.board[(i - 1, j - 1)]) == 1:
                        mt.update(a.board[(i - 1, j - 1)])
                    if len(a.board[(i - 1, j + 1)]) == 1:
                        mt.update(a.board[(i - 1, j + 1)])
                    if len(a.board[(i - 2, j - 1)]) == 1:
                        mt.update(a.board[(i - 2, j - 1)])
                    if len(a.board[(i - 2, j + 1)]) == 1:
                        mt.update(a.board[(i - 2, j + 1)])
                else:
                    if len(a.board[(i - 1, j - 1)]) == 1:
                        mt.update(a.board[(i - 1, j - 1)])
                    if len(a.board[(i - 1, j - 2)]) == 1:
                        mt.update(a.board[(i - 1, j - 2)])
                    if len(a.board[(i - 2, j - 1)]) == 1:
                        mt.update(a.board[(i - 2, j - 1)])
                    if len(a.board[(i - 2, j - 2)]) == 1:
                        mt.update(a.board[(i - 2, j - 2)])
            #new_board.board[(i,j)].clear()
            new_board.board[(i,j)]= mt
    return new_board


def sudoku_cells():
    cells=[]
    for i in range(9):
        for j in range(9):
            cells.append((i,j))
    return cells


def sudoku_arcs():
    arcs = []
    for i in range(9):
        for j in range(9):
            # row and column dependencies
            for k in range(9):
                if k != j:
                    arcs.append(tuple(((i, j), (i, k))))
                if k != i:
                    arcs.append(tuple(((i, j), (k, j))))
            if (i == 0 or i == 3 or i == 6) and (j == 0 or j == 3 or j == 6):
                arcs.append(tuple(((i, j), (i + 1, j + 1))))
                arcs.append(tuple(((i, j), (i + 1, j + 2))))
                arcs.append(tuple(((i, j), (i + 2, j + 1))))
                arcs.append(tuple(((i, j), (i + 2, j + 2))))
            elif (i == 0 or i == 3 or i == 6) and (j == 1 or j == 4 or j == 7):
                arcs.append(tuple(((i, j), (i + 1, j - 1))))
                arcs.append(tuple(((i, j), (i + 1, j + 1))))
                arcs.append(tuple(((i, j), (i + 2, j - 1))))
                arcs.append(tuple(((i, j), (i + 2, j + 1))))
            elif (i == 0 or i == 3 or i == 6) and (j == 2 or j == 5 or j == 8):
                arcs.append(tuple(((i, j), (i + 1, j - 1))))
                arcs.append(tuple(((i, j), (i + 1, j - 2))))
                arcs.append(tuple(((i, j), (i + 2, j - 1))))
                arcs.append(tuple(((i, j), (i + 2, j - 2))))
            elif (i == 1 or i == 4 or i == 7) and (j == 0 or j == 3 or j == 6):
                arcs.append(tuple(((i, j), (i - 1, j + 1))))
                arcs.append(tuple(((i, j), (i - 1, j + 2))))
                arcs.append(tuple(((i, j), (i + 1, j + 1))))
                arcs.append(tuple(((i, j), (i + 1, j + 2))))
            elif (i == 1 or i == 4 or i == 7) and (j == 1 or j == 4 or j == 7):
                arcs.append(tuple(((i, j), (i - 1, j - 1))))
                arcs.append(tuple(((i, j), (i - 1, j + 1))))
                arcs.append(tuple(((i, j), (i + 1, j - 1))))
                arcs.append(tuple(((i, j), (i + 1, j + 1))))
            elif (i == 1 or i == 4 or i == 7) and (j == 2 or j == 5 or j == 8):
                arcs.append(tuple(((i, j), (i - 1, j - 1))))
                arcs.append(tuple(((i, j), (i - 1, j - 2))))
                arcs.append(tuple(((i, j), (i + 1, j - 1))))
                arcs.append(tuple(((i, j), (i + 1, j - 2))))
            elif (i == 2 or i == 5 or i == 8) and (j == 0 or j == 3 or j == 6):
                arcs.append(tuple(((i, j), (i - 1, j + 1))))
                arcs.append(tuple(((i, j), (i - 1, j + 2))))
                arcs.append(tuple(((i, j), (i - 2, j + 1))))
                arcs.append(tuple(((i, j), (i - 2, j + 2))))
            elif (i == 2 or i == 5 or i == 8) and (j == 1 or j == 4 or j == 7):
                arcs.append(tuple(((i, j), (i - 1, j - 1))))
                arcs.append(tuple(((i, j), (i - 1, j + 1))))
                arcs.append(tuple(((i, j), (i - 2, j - 1))))
                arcs.append(tuple(((i, j), (i - 2, j + 1))))
            else:
                arcs.append(tuple(((i, j), (i - 1, j - 1))))
                arcs.append(tuple(((i, j), (i - 1, j - 2))))
                arcs.append(tuple(((i, j), (i - 2, j - 1))))
                arcs.append(tuple(((i, j), (i - 2, j - 2))))
    return arcs


def read_board(path):
    board = {}
    with open(path) as infile:
        for row, line in enumerate(infile, start=1):
            for col, char in enumerate(line.strip(), start=1):
                if char == "*":
                    board[(row-1,col-1)]=set([1, 2, 3, 4, 5, 6, 7, 8, 9])
                elif int(char)>0 and int(char)<=9:
                    board[(row-1, col-1)]=set([int(char)])
                else:
                    print ("Unrecognized character '%s' at line %d, column %d" %
                        (char, row, col))
                    return None
    return board


def is_solved(a):
    for i in range(9):
       for j in range(9):
           if len(a.board[(i, j)])!=1:
               return False
    return True

class Sudoku(object):

    CELLS = sudoku_cells()
    ARCS = sudoku_arcs()
    board={}

    def __init__(self, board):
        self.board=board

    def get_values(self, cell):
        #print cell,self.board[cell]
        return self.board[cell]

    def remove_inconsistent_values(self, cell1, cell2):
        set1 = self.get_values(cell1)
        set2 = self.get_values(cell2)
        reduced_set=set([])
        #if cell1[0]==cell2[0] or cell1[1]==cell2[1] or ((int(cell1[0]/3)== int(cell2[0]/3)) and (int(cell1[1]/3)== int(cell2[1]/3))):
        if (cell1,cell2) in self.ARCS:
            for i in set1:
                counter=0
                for j in set2:
                    if i!=j:
                        counter+=1
                        break
                if counter:
                    reduced_set.add(i)
        if len(reduced_set)==len(self.board[cell1]):
            return False
        self.board[cell1]=reduced_set
        return True

    def infer_ac3(self):
        q=Queue.Queue()
        for (i,j) in self.ARCS:
            q.put((i,j))
        while(q.qsize()!=0):
            (i,j)=q.get()
            if self.remove_inconsistent_values(i,j):
                for (h,k) in self.ARCS:
                    if k!=j and h==i:
                        q.put((k,h))

    def infer_improved(self):
        #constrained_board=get_impossible_values(self)
        self.infer_ac3()
        printsudoku(self)
        for i in range(9):
            for j in range(9):
                if len(self.board[(i, j)])>1:
                    neighbors=get_neighbors(i,j)
                    value=set([1,2,3,4,5,6,7,8,9])
                    for x in neighbors:
                        if len(self.board[x]):
                            value.intersection_update(self.board[x])
                        else:
                            value.difference_update(self.board[x])
                    if len(value)==1:
                        print i , j, self.board[(i,j)], value
                        self.board[(i, j)]=value

    def infer_with_guessing(self):
        pass


# b = read_board("medium1.txt")
# #print len(b), b[(0,0)],b[(8,8)]
# print Sudoku(b).get_values((0, 0))
# print Sudoku(b).get_values((0, 1))
# print ((0, 0), (0, 8)) in sudoku_arcs()
# #True
# print ((0, 0), (8, 0)) in sudoku_arcs()
# #True
# print ((0, 8), (0, 0)) in sudoku_arcs()
# #True
# print ((0, 0), (2, 1)) in sudoku_arcs()
# #True
# print ((2, 2), (0, 0)) in sudoku_arcs()
# #True
# print ((2, 3), (0, 0)) in sudoku_arcs()
# #False
# print sudoku_cells()
# #[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), ..., (8, 5), (8, 6), (8, 7), (8, 8)]
#sudoku = Sudoku(read_board("easy.txt")) # See below for a picture.
# print sudoku.get_values((0, 3))
# #set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# for col in [0, 1, 4]:
#     removed = sudoku.remove_inconsistent_values((0, 3), (0, col))
#     print removed, sudoku.get_values((0, 3))
# #True set([1, 2, 3, 4, 5, 6, 7, 9])
# #True set([1, 3, 4, 5, 6, 7, 9])
# #False set([1, 3, 4, 5, 6, 7, 9])
sudoku = Sudoku(read_board("Medium2.txt")) # See below for a picture.
#printsudoku(sudoku)
sudoku.infer_improved()
printsudoku(sudoku)