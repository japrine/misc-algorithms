# Recursive even split and sorting merge


def sort(l):
    if len(l) < 2:                      # Check Base Case
        return l
    s = len(l) // 2                     # Split and Recurse
    a, b = l[:s], l[s:]
    a, b = sort(a), sort(b)
    o = []                              # Sort Merge
    i, j = 0, 0
    for k in range(len(l)):
        if not (i >= len(a)) and not (j >= len(b)):
            if a[i] <= b[j]:
                o.append(a[i])
                i += 1
            else:
                o.append(b[j])
                j += 1
        elif not i >= len(a):
            o.append(a[i])
            i += 1
        elif not j >= len(b):
            o.append(b[j])
            j += 1
    return o
