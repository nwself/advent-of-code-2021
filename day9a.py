lines = [list(line.strip()) for line in open("./example9.txt")]

winners = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if all([
            lines[i - 1][j] > lines[i][j] if i - 1 >= 0 else True,
            lines[i][j - 1] > lines[i][j] if j - 1 >= 0 else True,
            lines[i + 1][j] > lines[i][j] if i + 1 < len(lines) else True,
            lines[i][j + 1] > lines[i][j] if j + 1 < len(lines[i]) else True,
        ]):
            winners.append(lines[i][j])

sum([int(x) + 1 for x in winners])