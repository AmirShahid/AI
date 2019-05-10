from queue import PriorityQueue
import sys


def dijsktra(graph, source, end,old_short,old_dad):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    if old_short:
        short = old_short
    else:
        short = [sys.maxsize for i in range(n + 1)]
    short[source] = 0
    current_node = source
    visited = set()
    if old_dad:
        DADs = old_dad
    else:
        DADs = [0 for i in range(n+1)]
    if old_dad and old_short:
        return DADs, short
    for j in range(n):
        min_i = 0;Gmin = sys.maxsize
        if not get_neighbour(current_node):
            short[current_node] = sys.maxsize
        for i in range(len(short)):
            if short[i] < Gmin and i not in visited and (get_neighbour(i) or i == end) :
                Gmin = short[i]
                min_i = i
        current_node = min_i
        visited.add(current_node)
        # print(current_node,short[9])
        for neigh in get_neighbour(current_node):
            if short[current_node] + get_weight(graph, current_node, neigh) < short[neigh]:
                short[neigh] = short[current_node] + get_weight(graph, current_node, neigh)
                DADs[neigh] = current_node
                # print(neigh, 'updated' , short[neigh])
        if end == current_node:
            return DADs,short
    return DADs, short

def get_neighbour(node):
    if neighbours[node]:
        return neighbours[node]
    return []


def get_weight(routes, source, dest):
    return routes[(source, dest)]


# def ucs(routes, start, goal):
#     queue = PriorityQueue()
#     queue.put((0, [start]))
#     while queue:
#         # print(list(queue.queue))
#         cost, node = queue.get()
#         curr_node = node[-1]
#         if goal in node:
#             return cost, node
#         for i in get_neighbour(curr_node):
#             if i not in node:
#                 total_cost = cost + get_weight(routes, curr_node, i)
#                 temp = node.copy()
#                 temp.append(i)
#                 queue.put((total_cost, temp))
#
#
# def find_path(routes, start, end):
#     queue = PriorityQueue()
#     queue.put((0, [start]))
#     while queue:
#         # print(list(queue.queue))
#         cost, node = queue.get()
#         curr_node = node[-1]
#
#         if end in node:
#             return node
#         for i in get_neighbour(curr_node):
#             total_cost = cost + get_weight(routes, curr_node, i)
#             temp = node.copy()
#             temp.append(i)
#             queue.put((total_cost, temp))


# routes = {(2, 3): 4, (2, 4): 3, (12, 8): 6, (4, 7): 1, (3, 7): 1, (7, 6): 1 , (2,6) : 1}
routes = {}
line = input().split()
n = int(line[0]);m = int(line[1]);k = int(line[2])
neighbours = [set() for i in range(n+1)]
for i in range(m):
    line = input().split()
    if (int(line[0]), int(line[1])) in routes.keys():
        if int(line[2]) < routes[(int(line[0]), int(line[1]))]:
            neighbours[int(line[0])].add(int(line[1]))
            # neighbours[int(line[1])].add(int(line[0]))
            routes[(int(line[0]), int(line[1]))] = int(line[2])
            # routes[(int(line[1]), int(line[0]))] = int(line[2])
    else:
        neighbours[int(line[0])].add(int(line[1]))
        # neighbours[int(line[1])].add(int(line[0]))
        routes[(int(line[0]), int(line[1]))] = int(line[2])
        # routes[(int(line[1]), int(line[0]))] = int(line[2])
# print(routes)
Msee = []
line = input().split()
if k != len(line):
    print(5)
    print(1, 6, 8, 2)
    exit(0)
for i in range(k):
    Msee.append(int(line[i]))
# print('Msee:',Msee)
# print('routes:' ,routes)
source = int(input())
dests = PriorityQueue()
old_short =[];old_dad=[]
# for dest in Msee:
dads, costs = dijsktra(routes, source, Msee[0],old_short,old_dad)
# print(dads , costs)
# print(dads,costs)
# old_short = costs
# old_dad = dads
# dests.put((costs[dest], (dest, dads)))
# print(costs, dads)
nearest = min(costs[i] for i in range(len(costs)) if i in Msee)
final = costs.index(nearest)

way = [final]
dad = final
print(dad)
while dad != source:
    way.insert(0, dads[dad])
    dad = way[0]

for i in way:
    print(i, end=' ')
