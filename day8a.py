
def part1():
    sum(
        [
            len(
                list(filter(
                    lambda x: x in [2, 3, 4, 7],
                    map(len, line.partition("|")[2].strip().split())
                ))
            ) for line in open("./input8.txt")
        ]
    )
