############################################################
# Section 3: Linear Disk Movement
############################################################

def solve_identical_disks(length, n):
  array=[0]*length
  for i in range(n):
    array[i]=1
  index=n-1
  moves=[]
  while index>=0:
    if array[index]==1:
      cnode=index;
      while cnode<length-1:
        if (arra3y[cnode-1]==1 and s) and array[cnode+1]==0:
          temp=array[cnode-1]
          array[cnode-1]=array[cnode+1]
          array[cnode+1]=temp
          moves.append((cnode-1,cnode+1))
          cnode+=1
        elif array[cnode+1]==0:
          temp=array[cnode]
          array[cnode]=array[cnode+1]
          array[cnode+1]=temp
          moves.append(((cnode,cnode+1)))
          cnode+=1
        else:
          cnode+=1
    index-=1
  return moves