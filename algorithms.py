from random import randint

# My Algorithms
import sortmerge
import quicksort
import mergeksorted
import inversioncount
import selection
import karatsuba


def random_lister(x, z):  # x is length and y is int max
    l = []
    for _ in range(x):
        l.append(randint(1, z))
    return l


def load_list(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(int(line))
    return data


def sorted_lists():
    lists = []
    for k in range(10):
        lists.append(sortmerge.sort(random_lister(100, 100)))
    print(len(lists))
    return lists


if __name__ == '__main__':
    # For Sorts
    # l = random_lister(100000, 100000)
    # print(l)

    # Sort Merge - recursive even split and sorting merge
    # print(sortmerge.sort(l))

    # Quick Sort -
    # print(quicksort.first(l))
    # print(quicksort.last(l))
    # print(quicksort.random(l))
    # print(quicksort.three(l))

    # Merge K Sorted Lists
    lists = sorted_lists()
    print(mergeksorted.merge(lists))

    # Inversion Count
    # print(inversioncount.sort_merge(l))

    # Selection - Find value for index x as if it were sorted (partial sort)
    # print('Value at index 1000 is:', selection.random(l, 1000))

    # Karatsuba Multiplication
    # print(karatsuba.multiply(3141592653589793238462643383279502884197169399375105820974944592,
    #                          2718281828459045235360287471352662497757247093699959574966967627))

    # Minimum Cut

