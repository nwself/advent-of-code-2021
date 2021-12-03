import collections
lines = [list(n.strip()) for n in open("./input3.txt")]
print([
    v * (v ^ (2 ** len(lines[0]) - 1)) for v in [
        int("".join(
            [
                collections.Counter([
                    row[i] for row in lines
                ]).most_common(1)[0][0] for i in range(len(lines[0]))
            ]
        ),
        2)
    ]
][0])
