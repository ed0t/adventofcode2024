import functools
import math


def compute_distance(left, right):
    t = functools.reduce(lambda a, b: a + b,
                         map(lambda x: abs(int(x[0]) - int(x[1])),
                             zip(sorted(left), sorted(right))))
    return t


def collect(filename):
    left = []
    right = []
    with open(filename, 'r', encoding='UTF-8') as file:
        while line := file.readline():
            l, r = [l.strip() for l in line.split(" ") if l != ""]
            left.append(l)
            right.append(r)
    return left,right

def main1(filename):
    l,r = collect(filename)
    return compute_distance(l,r)



def main(filename):
    left = {}
    right = {}
    with open(filename, 'r', encoding='UTF-8') as file:
        while line := file.readline():
            l, r = [l.strip() for l in line.split(" ") if l != ""]
            l = int(l)
            r = int(r)
            if l in left.keys():
                left[l] = left[l]+1
            else:
                left[l] = 1

            if r in right.keys():
                right[r] = right[r]+ 1
            else:
                right[r] = 1

    print(right)
    t = 0
    for element in left.keys():
        t += (element * right.pop(element,0))

    return t

    # t= 0
    # for pair in zip(sorted(left), sorted(right)):
    #     t += abs(int(pair[0])-int(pair[1]))
    # print(t)


if __name__ == '__main__':
    total = main("input.txt")
    print(total)
