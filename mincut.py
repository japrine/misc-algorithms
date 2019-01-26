from random import randint
from copy import deepcopy


# array = []                                                      # Build array from file
# with open('kargerMinCut.txt') as f:
#     for line in f:
#         line = line.strip('\t\n')                               # Strip tab and new line char from lines
#         array.append([int(s) for s in line.split('\t')])        # Split lines by tab and build int list


def karger(a):
    while len(a) > 2:
        rn = randint(0, len(a)-1)                       # Pick random 1st vertex index
        i1 = a[rn][0]                                   # Label of 1st vertex
        i2 = a[rn][randint(1, len(a[rn])-1)]            # Label of 2nd vertex on a random edge selected

        for idx, _ in enumerate(a):
            if _[0] == i2:                              # Find 2nd vertex index in array
                a[rn].extend(_[1:])                     # Copy 2nd vertex edges into 1st vertex
                id = idx                                # Get 2nd vertex index for next step

        for idx1, vertex in enumerate(a):               # Reassign all edges connecting to 2nd vertex to 1st
            for idx2, _ in enumerate(vertex[1:]):
                if _ == i2:
                    a[idx1][idx2+1] = i1

        remove_list = []
        for idx, _ in enumerate(a[rn][1:]):             # Identify self-loops inside 1st vertex
            if _ == i1:
                remove_list.insert(0,idx+1)             # Build list in reverse order
        for _ in remove_list:                           # Delete the self-loops in list
            del a[rn][_]
        del a[id]
    return a                                            # Return array when only 2 vertex remain


def run_karger(array):
    min_conn = []
    for _ in range(len(array)):
        a = deepcopy(array)                                 # Copy array to new list a
        a = karger(a)
        min_conn.append(len(a[0])-1)                        # Append resulting edges to list
        # print(len(a[0])-1, a)
    return min_conn
