from random import randint

# My Algorithms
import karatsuba
import sortmerge


def random_lister(x, z):  # x is length and y is int max
    l = []
    for _ in range(x):
        l.append(randint(1, z))
    return l


if __name__ == '__main__':
    # Sort Merge
    l = random_lister(100000, 100000)
    print(l)
    print(sortmerge.sort(l))

    # Karatsuba Multiplication
    print(karatsuba.multiply(3141592653589793238462643383279502884197169399375105820974944592,
                             2718281828459045235360287471352662497757247093699959574966967627))
