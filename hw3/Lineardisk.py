import Queue

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

print solve_distinct_disks(8,4)
#print solve_distinct_disks(5,4)
#print solve_distinct_disks(5,2)
#print solve_distinct_disks(12,3)
#print solve_distinct_disks(9,7)
#print solve_distinct_disks(10,5)
#print solve_distinct_disks(10,9)
