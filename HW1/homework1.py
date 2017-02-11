############################################################
# CIS 521: Homework 1
############################################################

student_name = "Hari Sudhan Parameswaran"

############################################################
# Section 1: Python Concepts
############################################################

python_concepts_question_1 = """
In Python strongly typed refers to the fact that Every object
  has an associated type. Executing expresssion between types
  that are incompatible are not allowed. For eg.,
  #trying to add string to an integer.
  >>>"abc" + 2
  #throws the error
  Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
  "abc" + 2
  TypeError: cannot concatenate 'str' and 'int' objects
Python is also dynamically typed, in the sense any object takes
  the type of the variable decalred at the point of execution.
  In other words, a same variable can take up different types
  at different places in the same code;
  #for Eg.
  >>> a= 2
  >>> a*2
  4
  >>> a='abc'
  >>> a
  'abc'   
"""

python_concepts_question_2 = """
Lists are mutable objects. Hence cannot be used as dict keys .
The issue can be resolved by changing the list into tuples, which
immutable.
>>> points_to_names = {(0, 0): "home", (1, 2): "school", (-1, 1): "market"}
"""

python_concepts_question_3 = """
def concatenate2(strings) is faster for larger set of strings. 
Because join is an iter method that gives back an iter object,
the exectution is faster that def concatenate1(strings) which
basically a for loop.
"""

############################################################
# Section 2: Working with Lists
############################################################

def extract_and_apply(l, p, f):
    return [f(x) for x in l if p(x)]

def concatenate(seqs):
    return [ y for x in seqs \
               for y in x]

def transpose(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

############################################################
# Section 3: Sequence Slicing
############################################################

def copy(seq):
  temp= seq[:]
  return temp

def all_but_last(seq):
  temp= seq[:]
  return temp[:-1]

def every_other(seq):
  temp= seq[:]
  return temp[::2]

############################################################
# Section 4: Combinatorial Algorithms
############################################################

def prefixes(seq):
  for index in range(len(seq)+1):
    yield seq[:index]
    
def suffixes(seq):
  for index in range(len(seq)+1):
    yield seq[index:]

def slices(seq):
  for i in range(len(seq)):
    for j in range(len(seq)-i):
      yield seq[i:i+j+1]

############################################################
# Section 5: Text Processing
############################################################

def normalize(text):
  temp= text.lower()
  spl= temp.split()
  str=" "
  return str.join(spl)

def no_vowels(text):
  temp= text
  new=""
  for  i in range(len(temp)):
    if(temp[i]!='a' and temp[i]!='e' and temp[i]!='i' and temp[i]!='o' and temp[i]!='u' and temp[i]!='A' and temp[i]!='E' and temp[i]!='i' and temp[i]!='O' and temp[i]!='U'):
      new= new+temp[i]
  return new

def digits_to_words(temp):
  new=""
  for  i in range(len(temp)):
    if(temp[i]=='1'):
      new= new+'one'+' '
    if(temp[i]=='2'):
      new= new+'two'+' '
    if(temp[i]=='3'):
      new= new+'three'+' '
    if(temp[i]=='4'):
      new= new+'four'+' '
    if(temp[i]=='5'):
      new= new+'five'+' '
    if(temp[i]=='6'):
      new= new+'six'+' '
    if(temp[i]=='7'):
      new= new+'seven'+' '
    if(temp[i]=='8'):
      new= new+'eight'+' '
    if(temp[i]=='9'):
      new= new+'nine'+' '
    if(temp[i]=='0'):
      new= new+'zero'+' ' 
  return new[:-1]

def to_mixed_case(name):
  temp= name.lower()
  spl=temp.split('_')
  new=""
  for i in range(len(spl)):
    if len(new):
      new=new+spl[i].capitalize()
    else:
      new=spl[i]
  return new

############################################################
# Section 6: Polynomials
############################################################

class Polynomial(object):
  t=()
  def __init__(self, polynomial):
    self.t=tuple(polynomial)
    
  def get_polynomial(self):
    return self.t

  def __neg__(self):
    return Polynomial(((-1*self.t[i][0],self.t[i][1]) for i in range(len(self.t))))

  def __add__(self, other):
    r=self.t
    r+=other.t
    return Polynomial(r)
  
  def __sub__(self, other):
    r=self.t
    a=-other
    r+=a.t
    return Polynomial(r)
  
  def __mul__(self, other):
    return Polynomial(((self.t[i][0]*other.t[j][0],self.t[i][1]+other.t[j][1]) for i in range(len(self.t)) for j in range(len(other.t))))
  
  def __call__(self, x):
    r=0
    for i in range(len(self.t)):
      r+=self.t[i][0]*(pow(x,self.t[i][1]))
    return r

  def simplify(self):
    r=[0]; mx=0; temp=[]
    for i in range(len(self.t)):
      if mx<self.t[i][1]:
        mx=self.t[i][1]
    for i in range(mx):
      r.append(0)
    for i in range(len(self.t)):
      r[self.t[i][1]]+=self.t[i][0]
    for i in range(mx+1):
      if r[mx-i]!=0:
        temp.append((r[mx-i],mx-i))
    self.t=tuple(temp)

  def __str__(self):
    text=""
    for i in range(len(self.t)):
      if (i==0):
        if(self.t[i][1]==0):
          text+=(str(self.t[i][0]))
        elif(self.t[i][1]==1):
          if(self.t[i][0]==1):
            text+=('x')
          elif(self.t[i][0]==-1):
            text+=('-x')
          else:
            text+=(str(self.t[i][0])+'x')
        else:
          if(self.t[i][0]==1):
            text+=('x^'+str(self.t[i][1]))
          elif(self.t[i][0]==-1):
            text+=('-x^'+str(self.t[i][1]))
          else:
            text+=(str(self.t[i][0])+'x^'+str(self.t[i][1]))
      else:
        if(self.t[i][1]==0):
          if(self.t[i][0]>=0):
            text+=(' + '+str(self.t[i][0]))
          else:
            text+=(' '+str(self.t[i][0]))
        elif(self.t[i][1]==1):
          if(self.t[i][0]>=0):
            if(self.t[i][0]==1):
              text+=(' + '+'x')
            else:
              text+=(' + '+str(self.t[i][0])+'x')
          else:
            if(self.t[i][0]==-1):
              text+=(' -'+'x')
            else:
              text+=(' '+str(self.t[i][0])+'x')
        else:
          if(self.t[i][0]>=0):
            if(self.t[i][0]==1):
              text+=(' + '+'x^'+str(self.t[i][1]))
            else:
              text+=(' + '+str(self.t[i][0])+'x^'+str(self.t[i][1]))
          else:
            if(self.t[i][0]==-1):
              text+=(' '+'x^'+str(self.t[i][1]))
            else:
              text+=(' '+str(self.t[i][0])+'x^'+str(self.t[i][1]))
    return text

############################################################
# Section 7: Feedback
############################################################

feedback_question_1 = """
15-16hours
"""

feedback_question_2 = """
understanding the iterators and generators
"""

feedback_question_3 = """
assignment challenges the understanding of the concepts
"""
