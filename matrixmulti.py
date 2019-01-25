import copy


def multi(x, y):
    z = copy.deepcopy(x)  # create z with same size
    for i in range(len(z)):
        for j in range(len(z)):
            k = 0
            for _ in range(len(x)):
                k += x[i][_] * y[_][j]
            z[i][j] = k
    return z

