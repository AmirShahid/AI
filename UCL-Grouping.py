import random
import sys
import copy
def can_play(t1, t2):
    if countries[t1] != countries[t2] and group[t1] != group[t2] and t1 % 2 != t2 % 2:
        return True
    return False

def min_arg_count(l):
    min = sys.maxsize
    for arg in l.values():
        if len(arg) < min:
            min = len(arg)
        if min == 0:
            break
    return min

def is_done(l):
    max = 0
    for arg in l.values():
        if len(arg) == 1:
            max +=1
    if max == len(l):
        return True
    else:return False

def make_new_arc(th, ta):
    for i in range(2 * n):
        if ta in possib_teams[i]:
            possib_teams[i].remove(ta)
        if th in possib_teams[i]:
            possib_teams[i].remove(th)
    possib_teams[ta] = [th]
    possib_teams[th] = [ta]

def against(t1,possib_teams):
    states = [possib_teams]
    i = 0
    while True:
        home = i
        i += 1
        # print(home, possib_teams)
        try:
            away = random.choice(possib_teams[home])
        except:
            print('impossible')
            exit(0)
        # for o in range(len(possib_teams[home])) :
        #     temp = random.choice(possib_teams[home])
        #     if home in possib_teams[temp]:
        #         away = temp
        #         break
        # if away is None:
        #     possib_teams = states.pop()
        if len(possib_teams[home]) > 1:
            possib_teams[home].remove(away)
            states.append(copy.deepcopy(possib_teams))
        make_new_arc(home, away)
        if not states:
            print('impossible')
            exit(0)
        if min_arg_count(possib_teams) == 0:
            # print('here')
            # print(home, possib_teams)
            possib_teams = states.pop()
            i = 0
        if is_done(possib_teams):
            break

    return possib_teams[t1]

countries = dict()
possib_teams = dict()
group = dict()
n = int(input())
res = dict()
for i in range(0, 2 * n, 2):
    line = input().split()
    countries[i] = line[0]
    countries[i + 1] = line[1]
    group[i] = int(i / 2)
    group[i + 1] = int(i / 2)

# print('countries:', countries)
# print('group:', group)

for i in range(2 * n):
    possib_teams[i] = list()
    for j in range(2 * n):
        if can_play(i, j):
            possib_teams[i].append(j)

# print('possib_teams', possib_teams)




for i in range(2*n):
    print(against(int(input()),possib_teams)[0])
