from functools import reduce
f = open("./input4.txt")
# make a db of number -> time when that number is called
nums = {n: i for i, n in enumerate(map(int, next(f).strip().split(",")))}
lines = [r.strip() for r in f]


print([sum([sum([n[0] if n[1] > winner[1] else 0 for n in row]) for row in winner[0]]) * list(nums.keys())[winner[1]] for winner in [sorted(
    map(
        lambda board: (board, 
            min([ # find min of all row and column maxes, aka when this board wins
                max(row[i][1] for row in board) for i in range(0, len(board[0])) # find max t_n per column (aka when this column wins)
            ] + [
                max([x[1] for x in row]) for row in board # find max t_n per row
            ])
        ),
        [list(
            map(lambda row: [
                    (int(n), nums[int(n)] if int(n) in nums else len(nums) + 1) for n in row.split() # convert each number to (number, time that number is called)
                ],
                lines[i:i+6]))[1:] for i in range(0, len(lines), 6) # get each board, drop empty lines
        ]
    ),
    key=lambda b: b[1],
    # reverse=True  # uncomment this for part 2
)[0]]][0])

