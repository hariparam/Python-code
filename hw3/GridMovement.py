import Queue

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
        currentnode=start;
        q=Queue.PriorityQueue();
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


scene = [[False, False, False],[False, True , False],[False, False, False]]
a=find_path((0, 0), (2, 1), scene)
print a