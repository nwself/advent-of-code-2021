import itertools
import functools

lines = [line.strip() for line in open("./input9.txt")]

marked = []
def recurse(row, col):
    if (row, col) in marked:
        return 0
    marked.append((row, col))
    if row < 0 or col < 0 or row >= len(lines) or col >= len(lines[0]):
        return 0
    if lines[row][col] != "9":
        to_check = [c for c in [
            (row - 1, col),
            (row, col - 1),
            (row + 1, col),
            (row, col + 1),
        ] if c not in marked]

        return 1 + sum(itertools.starmap(recurse, to_check))
    else:
        return 0

basins = []
for row in range(len(lines)):
    for col in range(len(lines[j])):
        if lines[row][col] != "9" and (row, col) not in marked:
            print(f"{row},{col}")
            basins.append(recurse(row, col))

print(functools.reduce(operator.mul, sorted(basins)[-3:]))
