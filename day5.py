import collections
import itertools

print(len([v for v in collections.Counter(itertools.chain.from_iterable([
    [
        (
            int(line[0][0] - i * (line[0][0] - line[1][0]) / abs(line[0][0] - line[1][0]) if line[0][0] != line[1][0] else line[0][0]),
            int(line[0][1] - i * (line[0][1] - line[1][1]) / abs(line[0][1] - line[1][1]) if line[0][1] != line[1][1] else line[0][1])
        ) for i in range(max([abs(line[0][0] - line[1][0]), abs(line[0][1] - line[1][1])]) + 1)
    ]
    for line in map(
        lambda line: [tuple(map(int, c.split(","))) for c in line],
        (line.strip().split(" -> ") for line in open("./input5.txt"))
    )
])).values() if v >= 2]))

