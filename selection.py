from random import randint


def random(a, z, l=0, r=None):
    if r is None:
        r = len(a) - 1
    if r - l < 2:                          # Check Base Case
        # print('Found at Base, value is', a[l])
        return a[z]
    p, i = randint(l, r-1), l+1            # Assign Pivot
    # print('Current Range is', l, r)
    # print('pointer index', p, 'pointer value', a[p])
    a[l], a[p] = a[p], a[l]
    for j in range(i, r):
        if a[l] <= a[j]:                   # if j is larger
            pass
        else:                              # if j is smaller
            a[i], a[j] = a[j], a[i]
            i += 1
    a[l], a[i-1] = a[i-1], a[l]
    # print('pivot placed at index', i-1)
    if i-1 == z:
        # print('Found after placing pivot, value is', a[i-1])
        return a[z]
    if i-1 > z:
        # print('recurse left')
        iz = random(a, z, l, i - 1)
    if i-1 < z:
        # print('recurse right')
        iz = random(a, z, i, r)
    return iz
