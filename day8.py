import collections

Line = collections.namedtuple("Line", ["parts", "value", "db"], defaults=[{}])


lines = list(
    itertools.starmap(
        Line, 
        [
            [part.strip().split() if i != 0 else list(map(set, part.strip().split())) for i, part in enumerate(line.split("|"))
        ] for line in open("./input8.txt")]
    )
)

def solve(line):
    for digit in line.parts:
        if len(digit) == 2:
            line.db[1] = digit
        if len(digit) == 3:
            line.db[7] = digit
        if len(digit) == 4:
            line.db[4] = digit
        if len(digit) == 7:
            line.db[8] = digit

    for digit in line.parts:
        if len(digit) == 5:
            if line.db[1].issubset(digit):
                line.db[3] = digit
            elif len(line.db[4].intersection(digit)) == 2:
                line.db[2] = digit
            else:
                line.db[5] = digit

    for digit in line.parts:
        if len(digit) == 6:
            if len(line.db[5].intersection(digit)) == 5:
                if len(line.db[7].intersection(digit)) == 3:
                    line.db[9] = digit
                else:
                    line.db[6] = digit
            else:
                line.db[0] = digit

    lookup = dict(zip(map(frozenset, line.db.values()), line.db.keys()))
    return int("".join([str(lookup[frozenset(digit)]) for digit in line.value]))

sum(map(solve, lines))