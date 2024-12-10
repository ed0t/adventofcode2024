import functools
import math


def compute_distance(left, right):
    t = functools.reduce(lambda a, b: a + b,
                         map(lambda x: abs(int(x[0]) - int(x[1])),
                             zip(sorted(left), sorted(right))))
    return t


import itertools


def collect(filename):
    total = 0
    with open(filename, 'r', encoding='UTF-8') as file:
        while line := file.readline():
            o = [int(l.strip()) for l in line.split(" ") if l != ""]
            for a in combinations(o):
                if all_increasing(a):
                    total += 1
                    break
                elif all_decreasing(a):
                    total += 1
                    break

    return total


def all_increasing(elements):
    x = 0
    while x < len(elements) - 1:
        y = x + 1
        if elements[x] >= elements[y]:
            return False
        distance = abs(elements[x] - elements[y])
        if distance > 3:
            return False
        x += 1
    return True


def main(filename):
    return collect(filename)


def all_decreasing(elements):
    x = 0
    while x < len(elements) - 1:
        y = x + 1
        if elements[x] <= elements[y]:
            return False
        distance = abs(elements[x] - elements[y])
        if distance > 3:
            return False
        x += 1
    return True


def combinations(elements):
    c = [elements]

    for x in range(len(elements)):
        c.append(elements[0:x] + elements[x+1:])

    return c


if __name__ == '__main__':
    total = main("input.txt")
    print(total)
    # print(all_decreasing2([8, 6, 4, 5, 1]))
    # print(all_decreasing2([1, 2, 7, 8, 9]))
    # print(all_increasing2([4, 5, 7, 8, 9]))
    # print(combinations([4, 5, 7, 8, 9]))
