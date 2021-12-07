import functools
import itertools

@functools.lru_cache(maxsize=None)
def recurse(number, total_days):
    spawn_days = list(
        itertools.takewhile(
            lambda x: x < total_days,
            itertools.count(number + 7, 7)
        )
    )
    kid_days = [x + 2 for x in spawn_days if x + 2 < total_days]

    if len(spawn_days) == 0:
        return 1
    return 1 + len(spawn_days) + sum([
        recurse(day, total_days) for day in kid_days
    ])


print(
    sum([x + 1 for x in itertools.starmap(recurse, itertools.zip_longest(map(int, next(open("./example6.txt")).split(",")), [], fillvalue=18))])
)
