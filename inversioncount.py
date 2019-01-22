def brute(a):
    if len(a) < 2:
        return 0
    count = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[j] < a[i]:
                count += 1
    return count


def sort_merge(a):
    if len(a) < 2:
        return 0, a
    s = len(a) // 2
    b, c = a[:s], a[s:]
    b_count, b = sort_merge(b)
    c_count, c = sort_merge(c)
    count = 0 + b_count + c_count

    d = []  # merger
    i, j = 0, 0
    for k in range(len(a)):
        if not (i >= len(b)) and not (j >= len(c)):
            if b[i] <= c[j]:
                d.append(b[i])
                i += 1
            else:
                d.append(c[j])
                j += 1
                count += len(b) - i
        elif not i >= len(b):
            d.append(b[i])
            i += 1
        elif not j >= len(c):
            d.append(c[j])
            j += 1
    return count, d
