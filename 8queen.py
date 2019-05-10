
from random import randint
from random import uniform
from queue import PriorityQueue
from copy import deepcopy
def mkboard():
    board = [[0 for i in range(8)] for j in range(8)]
    for i in range(8):
        board[randint(0, 7)][i] = 1
    return board
def draw(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is None:
                print(' ',end='  |')
            else:
                if board[i][j] > 9:
                    print(board[i][j],end=' |')
                else:
                    print(board[i][j],end='  |')
        print()


def is_threat(board, q1, q2 ):
    i_step = 0
    j_step = 0
    if q1[0] < q2[0]:i_step =  1
    if q1[0] > q2[0]: i_step = -1
    if q1[1] < q2[1]:j_step = 1
    if q1[1] > q2[1]:j_step = -1
    # print(q1,q2,j_step,i_step)
    if i_step == 0:
        # print(q2[1] + j_step)
        for j in range(q1[1]+j_step,q2[1]+j_step,j_step):
            # print( q1 , (q1[0],j))

            if board[q1[0]][j] == 1:
                # print(q1[0], q1[1], q2[0], q2[1])

                if q2 == (q1[0],j):
                    return True
                else:
                    return False
    if j_step == 0:
        for i in range(q1[0]+i_step,q2[0]+i_step,i_step):
            if board[i][q1[1]] == 1:
                if q2 == (i, q1[1]):
                    return True
                else:
                    return False

    slope =  (q2[1]-q1[1]) /  (q2[0]-q1[0])
    if abs(slope) == 1:

        for i in range(1,abs(q1[0]-q2[0])+1 ):
            # for j in range(q1[1]+j_step,q2[1]+j_step,j_step):
            #     print(q1[0]+i*i_step , q1[1]+i*j_step )
                if board[q1[0]+i*i_step][q1[1]+i*j_step] == 1 :
                    if q2 == (q1[0]+i*i_step, q1[1]+i*j_step) :
                        return True
                    else:
                        return False

    return False

def get_queens(board):
    queens = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                queens.append((i,j))
    # print('q:',queens)
    return queens

def threat_set(board,queens):
    threats = set()
    for q1 in queens:
        for q2 in queens:
            if q1 != q2:
                if is_threat(board,q1,q2) and (q2,q1) not in threats:
                    threats.add((q1,q2))
    return threats

def steepest_ascent(board,queen):
    h = len(threat_set(board,get_queens(board)))
    pq = PriorityQueue()
    for i in range(8):
        if i == queen[0]:
            continue
        board[queen[0]][queen[1]] = 0
        board[i][queen[1]] = 1
        new_h = len(threat_set(board,get_queens(board)))
        pq.put((new_h,deepcopy(board)))
        board[i][queen[1]] = 0
        board[queen[0]][queen[1]] = 1

    min = pq.get()
    if min[0] < h:
        return min[1]
    return False

# board = [[0 for i in range(8) ] for j in range(7)]
# board.append([1 for i in range(8)])
# board[0][0] = 1
# board[1][1] = 1
# board[0][7] = 1
# board[1][6] = 1
# board[2][5] = 1
# draw(board)
# print(threat_set(board,get_queens(board)))
boards = []
visited = []
final_steps = []
# random walking
random_walk = 0
for c in range(1000):
    board = [[0 for i in range(8)] for j in range(8)]
    for i in range(8):
        board[randint(0, 7)][i] = 1
    boards.append(board)
    # print('initial:')
    # draw(board)
    # print()
    for c1 in range(100):
        queens = get_queens(board)
        moving_q = queens[randint(0,7)]
        board[moving_q[0]][moving_q[1]] = 0
        board[randint(0,7)][moving_q[1]] = 1
        # draw(board)
        # print()
        if len(threat_set(board,get_queens(board))) == 0 and board not in visited:
            random_walk +=1
            visited.append(board)
            final_steps.append(c1)
        #     print("on {x}'th iteration we found solution using random_walk".format(x=c1))
        #     draw(board)
        #     print()
            break
print('random_walk: '+str((random_walk/1000)*100)+'%' , 'avg_steps:',sum(final_steps)/len(final_steps))
visited.clear()
final_steps = []
#hill
hill_climbing = 0
for c in range(1000):
    # board = [[0 for i in range(8)] for j in range(8)]
    # for i in range(8):
    #     board[randint(0,7)][i] = 1
    # draw(board)
    board = boards[c]
    for c1 in range(100):
        queens = get_queens(board)
        #
        q = queens[c1%8]
        # draw(board)
        # print(threat_set(board,get_queens(board)))
        new_board = steepest_ascent(deepcopy(board),q)
        if new_board is False:
            # print(c,c1)
            continue
        # draw(new_board)
        # print(threat_set(board,get_queens(board)))
        # board = new_board
        if len(threat_set(new_board,get_queens(new_board ))) == 0 and board not in visited:
            visited.append(board)
            hill_climbing += 1
            final_steps.append(c1)
            # print(c1)
            # print("on {x}'th iteration we found solution using hill climbing".format(x=c1))
            # draw(new_board)
            # print()
            break
        board = deepcopy(new_board)

print('hill_climbing: '+str((hill_climbing/1000)*100)+'%' , 'avg_steps:',sum(final_steps)/len(final_steps))

# Stochastic
visited.clear()
Stochastic = 0
p = 0.8
final_steps = []
for c in range(1000):
    # board = [[0 for i in range(8)] for j in range(8)]
    # for i in range(8):
    #     board[randint(0,7)][i] = 1
    # draw(board)
    board = boards[c]

    for c1 in range(100):
        queens = get_queens(board)

        if uniform(0, 1) < p:
            # print('hill')
            # queens = get_queens(board)
            q = queens[c1 % 8]
            # draw(board)
            # print(threat_set(board,get_queens(board)))
            new_board = steepest_ascent(deepcopy(board), q)
            if new_board is False:
                # print(c,c1)
                continue
            # draw(new_board)
            # print(threat_set(new_board,get_queens(new_board)))
            board = new_board
        else:
            # print('random')
            q = queens[randint(0, 7)]
            board[q[0]][q[1]] = 0
            board[randint(0, 7)][q[1]] = 1

        if len(threat_set(board, get_queens(board))) == 0 and board not in visited:
            Stochastic += 1
            final_steps.append(c1)
            # print('visited:',visited)
            # visited.append(board)
            # print(c1)
            # print("on {x}'th iteration we found solution using Stochastic Hill Climbing with p = {p}".format(x=c1,p=p))
            # draw(board)
            # print()
            break
print('Stochastic: ' + str((Stochastic / 1000) * 100) + '%' , 'avg_steps:',sum(final_steps)/len(final_steps))
#
#

# Stochastic = 0
# p = 0.9
# for c in range(1000):
#     board = [[0 for i in range(8)] for j in range(8)]
#     for i in range(8):
#         board[randint(0,7)][i] = 1
#     draw(board)
    # board = boards[c]
    #
    # for c1 in range(100):
    #     queens = get_queens(board)

        # if  uniform(0, 1) < p:
        #     print('hill')
            # queens = get_queens(board)
            # q = queens[c1 % 8]
            # draw(board)
            # print(threat_set(board,get_queens(board)))
            # new_board = steepest_ascent(deepcopy(board), q)
            # if new_board is False:
                # print(c,c1)
                # continue
            # draw(new_board)
            # print(threat_set(new_board,get_queens(new_board)))
            # board = new_board
        # else:
        #     print('random')
        #     q = queens[randint(0, 7)]
        #     board[q[0]][q[1]] = 0
        #     board[randint(0, 7)][q[1]] = 1

        # if len(threat_set(board, get_queens(board))) == 0:
        #     Stochastic += 1
        #     print("on {x}'th iteration we found solution using Stochastic Hill Climbing with p = {p}".format(x=c1,p=p))
            # draw(board)
            # print()
            # break
# print('Stochastic: ' + str((Stochastic / 1000) * 100) + '%')
