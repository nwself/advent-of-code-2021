

class Self():
    def __init__(self):
        self.lines = [list(map(int, list(line.strip()))) for line in open("./input11.txt")]
        self.count = 0

        self.marked = []

    def flash(self, row, col):
        if (
            (row, col) in self.marked or
            row < 0 or
            row >= len(self.lines) or
            col < 0 or
            col >= len(self.lines[0])
        ):
            return 

        self.lines[row][col] += 1

        if self.lines[row][col] <= 9:
            return

        self.count += 1
        self.marked.append((row, col))

        self.flash(row - 1, col - 1)
        self.flash(row, col - 1)
        self.flash(row + 1, col - 1)
        self.flash(row - 1, col)
        self.flash(row + 1, col)
        self.flash(row - 1, col + 1)
        self.flash(row, col + 1)
        self.flash(row + 1, col + 1)

    def run(self, n):
        for i in range(n):
            self.marked = []
            self.count = 0
            for row in range(len(self.lines)):
                for col in range(len(self.lines[0])):
                    self.lines[row][col] += 1

            for row in range(len(self.lines)):
                for col in range(len(self.lines[0])):
                    if self.lines[row][col] > 9:
                        # print(f"{row},{col} is > 9")
                        self.flash(row, col)

            for row in range(len(self.lines)):
                for col in range(len(self.lines[0])):
                    if self.lines[row][col] > 9:
                        self.lines[row][col] = 0

            print(self.count)
            if self.count == 100:
                print(f"First all flash at {i+1}")
                break


s = Self()

s.run(1000)
# print(s.count)
# s.lines