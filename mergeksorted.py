def merge(lists):
    output = []

    def nested_len(l):
        if type(l) == list:
            return sum(nested_len(sublist) for sublist in l)
        else:
            return 1

    qty = nested_len(lists)

    for n in range(qty):
        low = 999
        list_k = 0
        for _ in range(len(lists)):
            if lists[_]:
                if lists[_][0] < low:
                    low = lists[_][0]
                    list_k = _
        output.append(low)
        lists[list_k].pop(0)
    return output
