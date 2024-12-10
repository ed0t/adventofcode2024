import functools
from typing import NamedTuple

# r,c
#
# r,c+1
# r,c+2
# r,c+3
#
# r+1,c
# r+2,c
# r+3,c
#
# r+1,c+1
# r+2,c+2
# r+3,c+3
#
# r+1,c-1
# r+2,c-2
# r+3,c-3


xmas_letters = {1: "M", 2: "A", 3: "S"}


def check_right(data, coordinates, letters):
    total = 0
    x = coordinates[0]
    y = coordinates[1]
    length_y = len(data[x])
    length_x = len(data)
    while x < length_x:
        # print("row ", x)
        while y < length_y:
            # print(y, data[x][y])
            if data[x][y] == "X":
                if c_r2(data, x, y, identity, inc_by_one, ["M", "A", "S"]):
                    total += 1
                if c_r2(data, x, y, inc_by_one, inc_by_one, ["M", "A", "S"]):
                    total += 1
                if c_r2(data, x, y, inc_by_one, identity, ["M", "A", "S"]):
                    total += 1
                if c_r2(data, x, y, inc_by_one, dec_by_one, ["M", "A", "S"]):
                    total += 1
                if c_r2(data, x, y, identity, dec_by_one, ["M", "A", "S"]):
                    total += 1
                if c_r2(data, x, y, dec_by_one, dec_by_one, ["M", "A", "S"]):
                    total += 1
                if c_r2(data, x, y, dec_by_one, identity, ["M", "A", "S"]):
                    total += 1
                if c_r2(data, x, y, dec_by_one, inc_by_one, ["M", "A", "S"]):
                    total += 1
                y += 1
            else:
                y += 1

        x += 1
        y = 0
    return total


def inc_by_one(x):
    return x + 1


def identity(x):
    return x


def dec_by_one(x):
    return x - 1


def c_r2(data, x, y, x_fn, y_fn, letters):
    length_x = len(data)
    length_y = len(data[0])

    if len(letters) == 0:
        return True
    else:
        letter = letters.pop(0)
        x = x_fn(x)
        y = y_fn(y)

        if (x >= 0 and x < length_x) and (y >= 0 and y < length_y):
            # need to do boundary check
            #     print(x,y, len(data))
            current_letter = data[x][y]
            if current_letter == letter:
                return c_r2(data, x, y, x_fn, y_fn, letters)
        return False


def main(filename):
    result = []
    with open(filename, 'r', encoding='UTF-8') as file:
        while line := file.readline():
            result.append(line.strip())
    print(result)

    return check_right(result, [0, 0], xmas_letters)


if __name__ == '__main__':
    # print(check_right(["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX",
    #                    "XMASAMX.MM", "X.....XA.A", "S.S.S.S.SS", ".A.A.A.A.A",
    #                    "..M.M.M.MM",".X.X.XMASX"], [0, 0], xmas_letters))
    # print(check_right([ "S.S.S.S.SS", ".A.A.A.A.A",
    #                    "..M.M.M.MM", ".X.X.XMASX"], [0, 0], xmas_letters))

    # # c_r2(["MMMSXXMASM", "MSAMXMSMSA", "AMXSXMAAMM", "MSAMASMSMX"], 0, 0, identity, inc_by_one)
    # total = main("input_small.txt")
    total = main("input.txt")
    print(total)
