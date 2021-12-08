crabs = list(map(int, next(open("./input7.txt")).split(",")))

print(min([
    sum([
        (abs(crab - winner) * (abs(crab - winner) + 1)) / 2 for crab in crabs
    ]) for winner in range(0, max(crabs))
]))
