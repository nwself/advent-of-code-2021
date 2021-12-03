# from functools import reduce
# from collections import namedtuple

# Stat = namedtuple('Stat',['d','x'])
# reduce(
#     lambda p, n: n.d += p.d; n.x += p.x, 
#     map(lambda pair: Stat(pair[1] if pair[0] == "down" else -pair[1] if pair[0] == "up" else 0, pair[1] if pair[0] == "forward" else 0), [line.split(" ") for line in open("./example2.txt")]), 
#     Stat(0, 0)
# )


# map(lambda pair: Stat(
#         pair[1] if pair[0] == "down" else -pair[1] if pair[0] == "up" else 0,
#         pair[1] if pair[0] == "forward" else 0
#     ), [(p[0], int(p[1])) for p in [line.split(" ") for line in open("./example2.txt")]])

from functools import reduce
from collections import namedtuple

Stat = namedtuple('Stat',['d','x'])

print(reduce(
    lambda p, n: Stat(n.d + p.d, n.x + p.x),
    map(lambda pair: Stat(
            pair[1] if pair[0] == "down" else -pair[1] if pair[0] == "up" else 0,
            pair[1] if pair[0] == "forward" else 0
        ), [(p[0], int(p[1])) for p in [line.split(" ") for line in open("./input2.txt")]]),
    Stat(0, 0)
))
