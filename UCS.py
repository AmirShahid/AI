from queue import PriorityQueue
import copy
import sys

def mkBoard():
    map = []
    for i in range(m):
        map.append([])
        for j in range(n):
            map[i].append(None)
    return map
def has_solution(queue):
    for i in queue:
        if i[1].blocking_heu == 0:
            return True , i[1]
    return False,None

def pop_min(l):
    mini = sys.maxsize
    b = None
    ind = None
    for i in range(len(l)):
        if l[i][0] < mini:
            mini = l[i][0]
            b = l[i][1]
            ind = i
    # print(l)
    l.pop(ind)
    return mini,b

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

def move(board, car, direction, step):
    Mboard = copy.copy(board)
    car_num = Mboard[car[0]][car[1]]
    car_len = car_length[car_num] - 1
    if direction == 'L':
        for i in range(car_len + 1):
            if Mboard[car[0]][car[1] + i - step] is None:
                Mboard[car[0]][car[1] + i - step] = car_num
                Mboard[car[0]][car[1] + i] = None
            else:
                print("can't move")
                break
    if direction == 'R':
        for i in range(car_len, -1, -1):
            # print('r :', i)
            if Mboard[car[0]][car[1] + i + step] is None:
                Mboard[car[0]][car[1] + i + step] = car_num
                Mboard[car[0]][car[1] + i] = None
            else:
                print("can't move")
                break
    if direction == 'U':
        for i in range(car_len + 1):
            if Mboard[car[0] + i - step][car[1]] is None:
                Mboard[car[0] + i - step][car[1]] = car_num
                Mboard[car[0] + i][car[1]] = None
            else:
                print("can't move")
                break
    if direction == 'D':
        for i in range(car_len, -1, -1):
            if Mboard[car[0] + i + step][car[1]] is None:
                Mboard[car[0] + i + step][car[1]] = car_num
                Mboard[car[0] + i][car[1]] = None
            else:
                print("cant' move")
                break
    return Mboard


def blocking_cars(board, car):
    blocking_cars = set()
    car_num = board[car[0]][car[1]]
    if car_dir[car_num] == 'h' and car_num != 0:
        for i in range(len(board[car[0]])):
            if board[car[0]][i] is not None:
                blocking_cars.add(board[car[0]][i])
    elif car_dir[car_num] == 'v':
        for j in range(len(board)):
            if board[j][car[1]] is not None:
                blocking_cars.add(board[j][car[1]])
    elif car_num == 0:
        for i in range(car[1] + car_length[car_num], len(board[car[0]])):
            if board[car[0]][i] is not None:
                blocking_cars.add(board[car[0]][i])
    return blocking_cars


def possible_moves(board, car):
    car_num = board[car[0]][car[1]]
    result = []
    if car_dir[car_num] == 'v':
        step = 0
        for i in range(car[0]):
            if board[car[0] - i - 1][car[1]] is None:
                step += 1
            else:
                break
        if step:
            result.append(('U', step))
        step = 0
        for i in range(car[0] + car_length[car_num], len(board)):
            if board[i][car[1]] is None:
                step += 1
            else:
                break
        if step:
            result.append(('D', step))
    elif car_dir[car_num] == 'h':
        step = 0
        for i in range(car[1] + car_length[car_num], len(board[car[0]])):
            # print(i)
            if board[car[0]][i] is None:
                step += 1
            else:
                break
        if step:
            result.append(('R',step))
        step = 0
        for i in range(car[1]-1,-1,-1):
            if board[car[0]][i] is None:
                step+=1
            else:
                break
        if step:
            result.append(('L',step))
    return result

def get_red_car(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j
def get_car(board,car_num):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == car_num:
                return i, j

class state:
    def __init__(self, current_board,current_cost,father_state):
        self.cost = int(current_cost)
        self.zero_heu = 0
        self.red_car = get_red_car(current_board)
        self.board = current_board
        self.father = father_state
        self.blocking_heu = len(blocking_cars(self.board, self.red_car))
        self.f = self.cost

    def __str__(self):
        return draw(self.board)

def NW(Nboard,car):
    car_num =  Nboard[car[0]][car[1]]
    if car_num is None:
        return False
    if car_dir[car_num] == 'v':
        if car[0] == 0:
            return True
        elif car_num != Nboard[car[0]-1][car[1]] or Nboard[car[0]-1][car[1]] is None:
            return True
        else:
            return False
    elif car_dir[car_num]=='h':
        if car[1] == 0:
            return True
        elif car_num != Nboard[car[0]][car[1]-1] or Nboard[car[0]][car[1]-1] is None:
            return True
        else:
            return False


visited_boards = []
def next_levels(STATE):
    board = STATE[1].board
    if STATE[1].blocking_heu == 0:
        # print('FOUND with cost :', STATE[1].cost + 1)
        # STATE[1].__str__()
        print(STATE[1].cost + 1)
        exit(0)
    # print('board :')
    # draw(board)
    cur_cost = STATE[0]
    for i in  range(len(board)):
        # print(board[i])
        for j in range(len(board[i])):
            if NW(board , (i,j)):
                next_moves = possible_moves(board,(i,j))
                # print(board[i][j],':',next_moves)
                # print('old:')
                # draw(board)
                for nex in next_moves:
                    new_board = copy.deepcopy(board)
                    for stat in range(nex[1]):
                        # print('moving :',board[i][j])
                        position = get_car(new_board,board[i][j])
                        new_board = move(new_board,position,nex[0],1)
                        new_state = state(copy.deepcopy(new_board), cur_cost + 1 ,STATE[1])

                        if new_board not in visited_boards:
                            # print('new state found')
                            # draw(new_board)
                            if new_state.blocking_heu == 0:
                                # print('FOUND with cost :' , new_state.cost+1)
                                # new_state.__str__()
                                print(new_state.cost+1)
                                # draw(new_state.father)
                                # while new_state.father is not None:
                                #     draw(new_state.board)
                                #     new_state = new_state.father
                                #     print(new_state.cost)
                                exit(0)
                            pq.append((new_state.f,new_state))
                            visited_boards.append(new_state.board)

line = input().split()
m = int(line[2]);
n = int(line[1]);
k = int(line[0])
Main_board = mkBoard()
car_length = {}
car_dir = {}

for i in range(k):
    line = input().split()
    for j in range(int(line[3])):
        if line[2] == 'h':
            Main_board[int(line[0]) - 1][int(line[1]) - 1 + j] = i
        elif line[2] == 'v':
            Main_board[int(line[0]) - 1 + j][int(line[1]) - 1] = i
        car_length[i] = int(line[3])
        car_dir[i] = line[2]

# draw(Main_board)
# a = []
# for i in range(len(Main_board)):
#     a.append([])
#     for j in range(len(Main_board[i])):
#         a[i].append(Main_board[i][j])

# board = move(copy.copy(Main_board),get_car(Main_board,10),'U',2)
# board = move(board,get_car(board,9),'U',2)
# board = move(board,get_car(board,8),'R',2)
# board = move(board,get_car(board,12),'R',2)
# board = move(board,get_car(board,6),'D',1)
# board = move(board,get_car(board,0),'R',2)
# board = move(board,get_car(board,11),'R',2)
# board = move(board,get_car(board,7),'D',1)
# board = move(board,get_car(board,1),'D',2)
# board = move(board,get_car(board,2),'D',2)
# board = move(board,get_car(board,3),'L',3)
# board = move(board,get_car(board,4),'L',2)
# board = move(board,get_car(board,5),'L',2)
# board = move(board,get_car(board,9),'U',2)
# board = move(board,get_car(board,10),'U',2)

# draw(board)

# print(blocking_cars(board, get_car(board, 0)))

# print(possible_moves(board, get_car(board, 3)))


pq = list()
init_state = state(Main_board,0,None)
# print(blocking_cars(Main_board, get_car(Main_board, 0)))
pq.append((0,init_state))
visited_boards.append(Main_board)
# draw(Main_board)
# pq.put((1,Main_board))
# pq.put((1,board))
# print(pq.get())
# next_levels(pop_min(pq))
# print('level 2')
# next_levels(pop_min(pq))
level = 0
while True:
    level+=1
    # print('level:',level)
    next_levels(pop_min(pq))
    if has_solution(pq)[1] is not None:
        # print('YYYYYYYYYYYYYYYYYYYYYEEEEEEEEEEEEEEEEEEEEEESSSSSSSSSS')
        print(has_solution(pq)[1].cost+1)
        break
#
# print('printing visited boards')
# for v in visited_boards:
#     draw(v)
#     print()

# print(has_solution(pq)[1])
# for i in pq:
#     draw(Main_board)
#     print('printing states with cost = ', i[0])
#     draw(i[1])
#     print()
# draw(Main_board)
# print()
# draw(board)
# print(possible_moves(board, (5, 0)))
# print(possible_moves(board, (5, 4)))
