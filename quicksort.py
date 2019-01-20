from random import randint
from numpy import argsort


def first(a, l=0, r=None):
    if r is None:
        r = len(a)
    if r - l < 2:                          # Check Base Case
        return
    p, i = l, l+1                          # Assign Pivot
    for j in range(i, r):
        if a[l] <= a[j]:                   # if j is larger
            pass
        else:                              # if j is smaller
            a[i], a[j] = a[j], a[i]
            i += 1
    a[l], a[i-1] = a[i-1], a[l]
    first(a, l, i - 1)
    first(a, i, r)


def last(a, l=0, r=None):
    if r is None:
        r = len(a)
    if r - l < 2:                          # Check Base Case
        return
    p, i = r-1, l+1                          # Assign Pivot
    a[l], a[p] = a[p], a[l]
    for j in range(i, r):
        if a[l] <= a[j]:                   # if j is larger
            pass
        else:                              # if j is smaller
            a[i], a[j] = a[j], a[i]
            i += 1
    a[l], a[i-1] = a[i-1], a[l]
    last(a, l, i - 1)
    last(a, i, r)


def random(a, l=0, r=None):
    if r is None:
        r = len(a)
    if r - l < 2:                          # Check Base Case
        return
    p, i = randint(l, r-1), l+1            # Assign Pivot
    a[l], a[p] = a[p], a[l]
    for j in range(i, r):
        if a[l] <= a[j]:                   # if j is larger
            pass
        else:                              # if j is smaller
            a[i], a[j] = a[j], a[i]
            i += 1
    a[l], a[i-1] = a[i-1], a[l]
    random(a, l, i - 1)
    random(a, i, r)


def three(a, l=0, r=None):
    if r is None:
        r = len(a)
    if r - l < 2:                          # Check Base Case
        return
    if (r-l) % 2 == 0:
        _ = l + ((r-l)//2)-1
    else:
        _ = l + ((r-l)//2)
    p = argsort([a[l], a[_], a[r-1]])[1]   # Assign Pivot
    if p == 0:
        p = l
    elif p == 1:
        p = _
    else:
        p = r-1
    i = l+1
    a[l], a[p] = a[p], a[l]
    for j in range(i, r):
        if a[l] <= a[j]:                   # if j is larger
            pass
        else:                              # if j is smaller
            a[i], a[j] = a[j], a[i]
            i += 1
    a[l], a[i-1] = a[i-1], a[l]
    three(a, l, i - 1)
    three(a, i, r)
