def merge(lists):
    output = []

    if len(lists) < 2:
        return lists

    def nested_len(l):
        if type(l) == list:
            return sum(nested_len(sublist) for sublist in l)
        else:
            return 1

    qty = nested_len(lists)                                         # Total Qty of Items in all Lists

    for n in range(qty):
        low = None
        list_k = 0
        for _ in range(len(lists)):
            if lists[_]:
                if low is None:
                    low = lists[_][0]
                    list_k = _
                if lists[_][0] < low:
                    low = lists[_][0]
                    list_k = _
        output.append(low)
        lists[list_k].pop(0)
    return output
