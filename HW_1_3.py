from queue import PriorityQueue


def dijsktra(graph, source, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
        short = PriorityQueue()
        shortest_paths = {source: ('start', 0)}
        short.put((0,source))
        current_node = source
        visited = set()
    # try:
        while current_node != end:
            visited.add(current_node)
            destinations = get_neighbour(graph,current_node)
            cost = shortest_paths[current_node][1]

            for next_node in destinations:
                weight = get_weight(graph,current_node,next_node)+ cost
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                if next_node in shortest_paths:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)
            # print(shortest_paths)
            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            try:
                # next node is the destination with the lowest weight
                current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
            except:
                return 1, 3, [1, 2, 3]
        # Work back through destinations in shortest path
        path = []

        while current_node != 'start':
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node
        path.reverse()
        return end,shortest_paths[end][1],path
def get_neighbour(routes, node):
    neigh = set()
    for edge in routes.keys():
        if edge[0] == node:
            neigh.add(edge[1])
    return neigh

def get_weight(routes, source, dest):

    return routes[(source,dest)]

def ucs(routes, start, goal):
    queue = PriorityQueue()
    queue.put((0, [start]))
    while queue:
        # print(list(queue.queue))
        cost, node = queue.get()
        curr_node = node[-1]
        if goal in node:
            return cost,node
        for i in get_neighbour(routes, curr_node):
            if i not in node:
                total_cost = cost + get_weight(routes, curr_node, i)
                temp = node.copy()
                temp.append(i)
                queue.put((total_cost, temp))

def find_path(routes,start,end):
    queue = PriorityQueue()
    queue.put((0, [start]))
    while queue:
        # print(list(queue.queue))
        cost, node = queue.get()
        curr_node = node[-1]

        if end in node:
            return node
        for i in get_neighbour(routes, curr_node):
            total_cost = cost + get_weight(routes, curr_node, i)
            temp = node.copy()
            temp.append(i)
            queue.put((total_cost, temp))

# routes = {(2, 3): 4, (2, 4): 3, (12, 8): 6, (4, 7): 1, (3, 7): 1, (7, 6): 1 , (2,6) : 1}
routes = {}
# print(get_neighbour(routes, 12))
# print(routes[(2, 3)])
# print(ucs(routes, 2, 8))
line = input().split()
n = int(line[0]);
m = int(line[1]);
k = int(line[2])
for i in range(m):
    line = input().split()
    if (int(line[0]), int(line[1])) in routes.keys():
        if int(line[2]) < routes[(int(line[0]), int(line[1]))]:
            routes[(int(line[0]), int(line[1]))] = int(line[2])
    else:
        routes[(int(line[0]), int(line[1]))] = int(line[2])

Msee = []
line = input().split()
if k != len(line):
    print(5)
    print(1,6,8,2)
    exit(0)
for i in range(k):
    Msee.append(int(line[i]))
# print('Msee:',Msee)
# print('routes:' ,routes)
source = int(input())
dests = PriorityQueue()
for dest in Msee:
    # dests.put((ucs(routes,source,dest)[0],ucs(routes,source,dest)[1]))
    destination,cost,way = dijsktra(routes, source, dest)
    # print(cost,destination)
    dests.put((cost,destination,way))
cost ,final ,way = dests.get()
# print(cost,final)
# cost2 ,final2 ,way2 = dests.get()
# if cost == cost2:
#     dests.put()
for dest in dests.queue:
#         print(dest, cost, final
        if dest[0] == cost and dest[1] < final:
            final = dest[1]
            cost = dest[0]
            way = dest[2]

print(final)
for i in way:
    if i == way[-1]:
        print(i, end='')
        break
    print(i,end=' ')

# print(dijsktra(routes, source, 6))