
from functools import reduce
from collections import namedtuple

Stat = namedtuple('Stat',['d','x','a'], defaults={'a': 0})

print(reduce(
    lambda p, n: Stat(p.d, p.x, n.d + p.a) if n.d != 0 else Stat(p.d + (n.x * p.a), (n.x + p.x), p.a),
    map(lambda pair: Stat(
            pair[1] if pair[0] == "down" else -pair[1] if pair[0] == "up" else 0,
            pair[1] if pair[0] == "forward" else 0,
        ), [(p[0], int(p[1])) for p in [line.split(" ") for line in open("./input2.txt")]]),
    Stat(0, 0, 0)
))
