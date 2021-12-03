
lines = [n.strip() for n in open("./input3.txt")]
def recurse(lines, i, default, rank):
    return lines[0] if len(lines) == 1 else recurse(
        [
            r for r in lines if r[i] == (
                default if collections.Counter(r[i] for r in lines).most_common()[rank][1] == len(lines) / 2.0 else collections.Counter(r[i] for r in lines).most_common()[rank][0]
            )
        ],
        i+1,
        default,
        rank)

print(int(recurse(lines, 0, "1", 0), 2) * int(recurse(lines, 0, "0", 1), 2))
