import math


def draw(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is None:
                print(' ', end='  ')
            else:
                if board[i][j] > 9:
                    print(board[i][j], end=' ')
                else:
                    print(board[i][j], end='  ')
        print()


class knowledge:
    def __init__(self, diff, available_num):
        self.diff = diff
        self.av_num = available_num

    def update(self):
        for i, j in self.diff.copy():
            if sudoku[i][j] != 0:
                self.diff.remove((i, j))
                if sudoku[i][j] in self.av_num:
                    self.av_num.remove(sudoku[i][j])

    def __str__(self):
        s = 'must different from: '
        if not self.diff:
            s = s + 'nothing!'
        else:
            for i in self.diff:
                s = s + str(i) + ' '
        s = s + ' \ available numbers: '
        if not self.av_num:
            s = s + 'nothing!'
        else:
            for i in self.av_num:
                s = s + str(i) + ' '

        return s


def isNot_solved(grid):
    for i in range(len(grid)):
        if 0 in grid[i]:
            return True
    return False


sudoku = []
KB = dict()
n = 4
block_len = int(math.sqrt(n))
av_num = set()
for i in range(n):
    av_num.add(i + 1)
    sudoku.append([])
    line = input().split()
    for j in range(n):
        sudoku[i].append(int(line[j]))
for i in range(n):
    for j in range(n):
        if sudoku[i][j] == 0:
            if i >= block_len:
                iBlk = (int(i / block_len)) * (block_len)
            else:
                iBlk = 0
            if j >= block_len:
                jBlk = (int(j / block_len)) * (block_len)
            else:
                jBlk = 0
            diff = set()
            unav_num = set()
            for c in range(n):
                if sudoku[i][c] != 0:
                    unav_num.add(sudoku[i][c])
                if sudoku[i][c] == 0 and c != j:
                    diff.add((i, c))
                if sudoku[c][j] != 0:
                    unav_num.add(sudoku[c][j])
                if sudoku[c][j] == 0 and c != i:
                    diff.add((c, j))
            for k in range(iBlk, iBlk + block_len):
                for l in range(jBlk, jBlk + block_len):
                    if sudoku[k][l] != 0:
                        unav_num.add(sudoku[k][l])
                    elif k != i and l != j:
                        diff.add((k, l))
            available_numbers = av_num - unav_num
            KB[(i, j)] = knowledge(diff, available_numbers)
# for key in KB.keys():
#     print(key, ':', KB[key])

# Forward Chaining -->

while isNot_solved(sudoku):
    new = []
    for key in KB.keys():
        if len(KB[key].av_num) == 1:
            sudoku[key[0]][key[1]] = KB[key].av_num.pop()
        KB[key].update()
    # for i in range(n):
    #     print(sudoku[i])
    # print()

for i in range(n):
    print(sudoku[i])
print()

draw(sudoku)
# for key in KB.keys():0 1 0 0

#     print(key, ':', KB[key])

# 4 0 2 1
# 2 0 4 0
# 3 4 0 2
# 1 0 3 0
