############################################################
# CIS 521: Homework 2
############################################################

student_name = "Hari Sudhan Parameswaran"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import random
from itertools import permutations
from copy import deepcopy

############################################################
# Section 1: N-Queens
############################################################

def num_placements_all(n):
  numplacements=1
  for i in range(n):
    numplacements*=((n*n)-i)
  return numplacements

def num_placements_one_per_row(n):
  numplacements=1
  for i in range(n):
    numplacements*= n 
  return numplacements

def n_queens_valid(board):
  numattacks=0
  for i in range(len(board)):
    #checking row attack
    for r in range(len(board)):
      if board[i]==board[r] and r<>i:
        numattacks+=1
    # left diagonal
    for l in range(len(board)):
      if ((l-i)==(board[l]-board[i])) and l<>i:
        numattacks+=1
    # right diagonal
    for d in range(len(board)):
      if ((i-d)==(board[d]-board[i])) and d<>i:
        numattacks+=1
  if numattacks:
    return False
  return True

def num_placements_all(n):
  numplacements=1
  for i in range(n):
    numplacements*=((n*n)-i)
  return numplacements

def num_placements_one_per_row(n):
  numplacements=1
  for i in range(n):
    numplacements*= n 
  return numplacements

def n_queens_valid(board):
  numattacks=0
  for i in range(len(board)):
    #checking row attack
    for r in range(len(board)):
      if board[i]==board[r] and r<>i:
        numattacks+=1
    # left diagonal
    for l in range(len(board)):
      if ((l-i)==(board[l]-board[i])) and l<>i:
        numattacks+=1
    # right diagonal
    for d in range(len(board)):
      if ((i-d)==(board[d]-board[i])) and d<>i:
        numattacks+=1
  if numattacks:
    return False
  return True

def n_queens_solutions(n):
  board=[]
  for i in range(n):
    board.append(i)
  solution=list(n_queens_helper(n,board))
  for item in solution:
    yield item

#using permutations of all the possilble coloumn combinations
#Unable to yield with DFS it prints the data correctly but
#yields a list of generators
def n_queens_helper(n,board):    
  for item in permutations(board):
    if n_queens_valid(item):
      yield item

#implemetation of n_queens_helper with DFS, having trouble with recursive yield
def n_queens_solutions_DFS(n):
  board=[]
  solution=n_queens_helper(n, board)
  return solution

def n_queens_helper_DFS(n, board):
  if n_queens_valid(board) and len(board)==n:
    #print board
    yield board
  elif(len(board)<n and n_queens_valid(board)):
    for i in range(n):
      tempboard=board[:]
      tempboard.append(i)
      yield n_queens_helper(n,tempboard)

############################################################
# Section 2: Lights Out
############################################################

class LightsOutPuzzle(object):
  b=[]

  def __init__(self, board):
    self.b=board

  def get_board(self):
    return self.b

  def perform_move(self, row, col):
    rows= len(self.b)
    cols=len(self.b[0])
    self.b[row][col]= not self.b[row][col]
    if row-1>=0:
      self.b[row-1][col]= not self.b[row-1][col]
    if row+1<=rows-1:
      self.b[row+1][col]= not self.b[row+1][col]
    if col-1>=0:
      self.b[row][col-1]= not self.b[row][col-1]
    if col+1<=cols-1:
      self.b[row][col+1]= not self.b[row][col+1]
    
  def scramble(self):
    rows= len(self.b)
    cols=len(self.b[0])
    for i in range(rows):
      for j in range(cols):
        self.b[i][j]= (random.random()<0.5)

  def is_solved(self):
    rows= len(self.b)
    cols=len(self.b[0])
    for i in range(rows):
      for j in range(cols):  
        if self.b[0][0]!=self.b[i][j]:
          return False
    return True
  
  def copy(self):
    return deepcopy(self)

  def successors(self):
    rows= len(self.b)
    cols=len(self.b[0])
    for i in range(rows):
      for j in range(cols):
        c=self.copy()
        c.perform_move(i,j)
        yield (i,j),c
  
  def find_solution(self):
    currentb=self.copy()
    #Storing both the array state corroesponding to the moves_made
    frontierqueue=[[]]
    boardqueue=[]
    boardqueue.append(currentb)
    moves_made=frontierqueue[0]
    while (not currentb.is_solved()):
      for next_moves_list, next_moves_boards in currentb.successors():
        solution=moves_made[:]
        solution.append(next_moves_list)
        frontierqueue.append(solution)
        boardqueue.append(next_moves_boards)
      frontierqueue=frontierqueue[1:]  
      boardqueue=boardqueue[1:]
      moves_made=frontierqueue[0]
      currentb=boardqueue[0]
    return moves_made 
    
def create_puzzle(rows, cols):
  board=[]
  for i in range(rows):
    row=[]
    for j in range(cols):
      row.append(False)
    board.append(row)
  return LightsOutPuzzle(board)

############################################################
# Section 3: Linear Disk Movement
############################################################

def solve_identical_disks(length, n):
  array=[0]*length
  for i in range(n):
    array[i]=1
  index=n-1
  frontierqueue=[]
  arrayqueue=[]
  solution=[]
  while (not is_solved(array,n)):
    arraylist=[]
    moves=[]
    [arraylist,moves]=next_moves(array, solution)
    for m in range(len(moves)):
      arrayqueue.append(arraylist[m])
      frontierqueue.append(moves[m])
    array=arrayqueue[0]
    solution=frontierqueue[0]
    arrayqueue=arrayqueue[1:]
    frontierqueue=frontierqueue[1:]
  return solution
  
def is_solved(array, n):
  for i in range(len(array)):
    if i<n:
      if (array[len(array)-1-i]!=1):
        return False
    else:
      if (array[len(array)-1-i]!=0):
        return False
  return True  
  
def next_moves(array, moved):
  arraylist=[]
  moves_list=[]
  for i in range(len(array)):
    if i+1<len(array):
      if array[i]!=0 and array[i+1]==0:
        arraylist.append(array[:])
        moves_list.append(moved[:])
        temp=arraylist[-1][i]
        arraylist[-1][i]=arraylist[-1][i+1]
        arraylist[-1][i+1]=temp
        moves_list[-1].append(tuple((i,i+1)))
    if i+2<len(array):
      if array[i]!=0 and array[i+1]!=0 and array[i+2]==0:
        arraylist.append(array[:])
        moves_list.append(moved[:])
        temp=arraylist[-1][i]
        arraylist[-1][i]=arraylist[-1][i+2]
        arraylist[-1][i+2]=temp
        moves_list[-1].append(tuple((i,i+2)))
  return arraylist,moves_list

def solve_distinct_disks(length, n):
  array=[0]*length
  for i in range(n):
    array[i]=i+1
  index=n-1
  frontierqueue=[]
  arrayqueue=[]
  solution=[]
  while (not is_unique_solved(array,n)):
    arraylist=[]
    moves=[]
    [arraylist,moves]=unique_next_moves(array, solution)
    for m in range(len(moves)):
      arrayqueue.append(arraylist[m])
      frontierqueue.append(moves[m])
    array=arrayqueue[0]
    solution=frontierqueue[0]
    arrayqueue=arrayqueue[1:]
    frontierqueue=frontierqueue[1:]
  return solution
  
def is_unique_solved(array, n):
  for i in range(len(array)):
    if i<n:
      if (array[len(array)-1-i]!=i+1):
        return False
    else:
      if (array[len(array)-1-i]!=0):
        return False
  return True  
  
def unique_next_moves(array, moved):
  arraylist=[]
  moves_list=[]
  for i in range(len(array)):
    if array[i]!=0:
      if i-2>=0:
        if array[i-1]!=0 and array[i-2]==0:
          arraylist.append(array[:])
          moves_list.append(moved[:])
          temp=arraylist[-1][i]
          arraylist[-1][i]=arraylist[-1][i-2]
          arraylist[-1][i-2]=temp
          moves_list[-1].append(tuple((i,i-2)))
      if i-1>=0:
        if array[i-1]==0:
          arraylist.append(array[:])
          moves_list.append(moved[:])
          temp=arraylist[-1][i]
          arraylist[-1][i]=arraylist[-1][i-1]
          arraylist[-1][i-1]=temp
          moves_list[-1].append(tuple((i,i-1)))
      if i+1<=len(array)-1:
        if array[i+1]==0:
          arraylist.append(array[:])
          moves_list.append(moved[:])
          temp=arraylist[-1][i]
          arraylist[-1][i]=arraylist[-1][i+1]
          arraylist[-1][i+1]=temp
          moves_list[-1].append(tuple((i,i+1)))
      if i+2<=len(array)-1:
        if array[i+1]!=0 and array[i+2]==0:
          arraylist.append(array[:])
          moves_list.append(moved[:])
          temp=arraylist[-1][i]
          arraylist[-1][i]=arraylist[-1][i+2]
          arraylist[-1][i+2]=temp
          moves_list[-1].append(tuple((i,i+2)))
  return arraylist,moves_list

############################################################
# Section 4: Feedback
############################################################

feedback_question_1 = """
15-20hrs"""

feedback_question_2 = """
Yeilding generators was tough
"""

feedback_question_3 = """
the problems were challenging but more topics couldve been covered.
"""
