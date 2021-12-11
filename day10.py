from collections import deque

db = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

c_scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

score = 0
incompletes = []

for line in [line.strip() for line in open("./input10.txt")]:
    # print()
    # print(line)
    state = deque()
    for char in list(line):
        if char in db.keys():
            state.append(db[char])
        else:
            expecting = state.pop()
            if char != expecting:
                # print("Expected {}, but found {} instead.".format(expecting, char))
                score += scores[char]
                break
    else:
        # print("Incomplete: {}")
        # print("".join(reversed(list(state))))
        score = 0
        for x in reversed(list(state)):
            # print(score, i, x, c_scores[x])
            score = (score * 5) + c_scores[x]
            # print(score)
        # print(score)
        # print()
        incompletes.append(score)
        # print(sum([
        #     c_scores[x] * i
        #     for i, x in enumerate(reversed(list(state)))
        # ]))

sorted(incompletes)[len(incompletes) // 2]
# print(score)