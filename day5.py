import collections
import itertools

Point = collections.namedtuple("Point", ["x", "y"])

print(len([v for v in collections.Counter(itertools.chain.from_iterable([
    [
        (
            int(line[0].x - i * (line[0].x - line[1].x) / abs(line[0].x - line[1].x) if line[0].x != line[1].x else line[0].x),
            int(line[0].y - i * (line[0].y - line[1].y) / abs(line[0].y - line[1].y) if line[0].y != line[1].y else line[0].y)
        ) for i in range(max([abs(line[0].x - line[1].x), abs(line[0].y - line[1].y)]) + 1)
    ]
    for line in map(
        lambda line: [Point(*map(int, c.split(","))) for c in line],
        (line.strip().split(" -> ") for line in open("./input5.txt"))
    )
])).values() if v >= 2]))

