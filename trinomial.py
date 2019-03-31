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

    print("What you want to perform?\n1 - print trinomial tree, 2 - use trit_sum function (see more about in README)")
    while True:
        try:
            ans = int(input())
        except ValueError:
            print("Enter only 1 or 2 number!")
        else:
            if ans not in [1, 2]:
                print("Enter only 1 or 2 number!")
                continue
            break

    if ans == 1:
        
        print("Enter the tree length...")
        while True:
            try:
                length = int(input())
            except ValueError:
                print("length must be a number more than or equal to 0!")
            else:
                if length < 0:
                    print("length must be a number more than or equal to 0!")
                    continue
                break

        if length == 0:
            sys.exit

        for i in range(length):
            for j in range(-length, length + 1):

                out = len(trit_sum(i, j))

                if out == 0:
                    print("".center(6), end='')
                    continue

                print("{}".format(out).center(6), end='')

            print()

    elif ans == 2:

        print("Enter the LENGTH argument...")

        while True:
            try:
                length = int(input())
            except ValueError:
                print("length must be a number more than or equal to 0!")
            else:
                if length < 0:
                    print("length must be a number more than or equal to 0!")
                    continue
                break


        print("Set the TOTAL argument...")

        while True:
            try:
                total = int(input())
            except ValueError:
                print("total must be a number!")
            else:
                break

        print(trit_sum(length, total))
