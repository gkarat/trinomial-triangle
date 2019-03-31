#
# Python program to print the Trinomial triangle
# (see https://en.wikipedia.org/wiki/Trinomial_triangle)
#
# Run with "py trinomial.py [arg]" command, where [arg]
# is the max height of printed triangle
#
# trit_sim(length, total) function can be also used for finding all
# possible variations of (length) long lists
# of -1, 0 and 1 elements, that in total give (total) value
#


import sys


def temp(res, length, total, initArray):

    if length == 0:
        if sum(initArray) == total:
            res.append(initArray)
            return
        else:
            return

    for i in range(-1, 2):
        temp(res, length - 1, total, initArray + [i])

    return res


def trit_sum(length, total):

    if (abs(total) > length):
        return []

    if (abs(total) == length):
        if total < 0:
            return [[-1 for i in range(length)]]

        if total >= 0:
            return [[1 for i in range(length)]]

    res = []

    for i in range(-1, 2):
        temp(res, length - 1, total, [i])

    return res

if __name__ == "__main__":
    MAX_LENGTH = int(sys.argv[1])

    for i in range(MAX_LENGTH):
        for j in range(-MAX_LENGTH, MAX_LENGTH + 1):

            out = len(trit_sum(i, j))

            if out == 0:
                print("".center(6), end='')
                continue

            print("{}".format(out).center(6), end='')

        print()
