from random import randint

# My Algorithms
import karatsuba
import sortmerge
import quicksort


def random_lister(x, z):  # x is length and y is int max
    l = []
    for _ in range(x):
        l.append(randint(1, z))
    return l


def load_file(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(int(line))
    return data


if __name__ == '__main__':
    # For Sorts
    l = random_lister(100000, 100000)
    # l = [3, 2, 5, 6, 1, 9, 7, 8, 0, 4, 10, 15, 14, 12, 11, 16, 17, 19, 18]
    print(l)

    # Sort Merge
    # print(sortmerge.sort(l))

    # Quck Sort
    # print(quicksort.first(l))
    # print(quicksort.last(l))
    # print(quicksort.random(l))
    print(quicksort.three(l))


    # Karatsuba Multiplication
    # print(karatsuba.multiply(3141592653589793238462643383279502884197169399375105820974944592,
    #                          2718281828459045235360287471352662497757247093699959574966967627))
