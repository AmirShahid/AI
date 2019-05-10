import sys
import random
from copy import deepcopy
class Graph:
    def __init__(self,vertice_count):
        self.adjacency = dict()
        self.possible_colors = dict()
        self.color = dict()
        for i in range(1,vertice_count+1):
            self.adjacency[i] = set()
            self.possible_colors[i] = []
            self.color[i] = None

    def add_edge(self,u,v):
        self.adjacency[u].add(v)
        self.adjacency[v].add(u)

    def add_color(self,node,color):
        self.possible_colors[node].append(color)

    def update_possib_color(self,u):
        self.possible_colors[u].remove(self.color[u])
        for neigh in self.adjacency[u]:
            if self.color[u] in self.possible_colors[neigh]:
                self.possible_colors[neigh].remove(self.color[u])

    def lowest_col_count(self):
        min = sys.maxsize
        lowest_count_node = None
        for node in range(1,n+1):
            if len(self.possible_colors[node]) < min and self.color[node] is None:
                min = len(self.possible_colors[node])
                lowest_count_node = node
                if min == 0:
                    return False

        return lowest_count_node
    def is_done(self):
         for node in range(1,n+1):
             if self.color[node] is None:
                return False
         return True
line = input().split()

n = int(line[0]);m = int(line[1]);k = int(line[2])
graph = Graph(n)
for node in range(1,n+1):
    colors = input().split()
    for color in colors:
        graph.add_color(node,int(color))

for i in range(m):
    line = input().split()
    u = int(line[0])
    v = int(line[1])
    graph.add_edge(u,v)
coloring_node = 1
generation = 0
states = list()
states.append(graph)

while not graph.is_done() and coloring_node is not False:
    # print(generation)
    if len(graph.possible_colors[coloring_node]) > 1:
        states.append(deepcopy(graph))

    c=random.choice(graph.possible_colors[coloring_node])
    graph.color[coloring_node] = c
    # print(coloring_node,'is coloring:',c)
    graph.update_possib_color(coloring_node)
    # for node in range(1,n+1):
        # print('possible colors for {node}:'.format(node = node),graph.possible_colors[node])
    coloring_node = graph.lowest_col_count()
    while coloring_node is False:
        if not states:
            print('NO')
            exit(1)
        graph = states.pop()
        coloring_node = graph.lowest_col_count()

    generation+=1

for node in range(1,n+1):
    print(graph.color[node])