from random import randint


def random_lister(x, z):  # x is length and y is int max
    l = []
    for _ in range(x):
        l.append(randint(1, z))
    return l


def sort_merger(l):
    if len(l) < 3:
        # print('base', l)
        l.sort()
        return l
    else:
        s = len(l) // 2
        # print('unsorted', l)
        a, b = l[:s], l[s:]
        # print('unsorted split', a, b)
        a = sort_merger(a)
        b = sort_merger(b)
        # print('sorted split', a, b)
        o = []  # merger
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
        # print('sorted merge', o)
        return o


if __name__ == '__main__':
    l = random_lister(100000, 100000)
    print(l)
    print(sort_merger(l))
