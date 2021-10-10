# number of nodes user input
node = int(input("Enter the number of node: "))
# print(node)

# number of connections from user input
connections = int(input("Enter the number of connections: "))
# print(connections)

# initializing dictionary
graph = {}

# loop to store connection of nodes from user input
for i in range(connections):
    # key = input()
    # value = input()
    text = input().split()
    if text[0] not in graph:
        graph[text[0]] = list()
    graph[text[0]].extend(text[1])
# print(graph)

goal = input("Enter goal node: ")


# function for DFS traversal
def BFS(graph, source, destination):
    visited = []

    queue = [[source]]
    if source == destination:
        print("same node")
        return
    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            neighbours = graph[node]

            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour == goal:
                    # print("shortest path = ", *new_path)
                    print((len(new_path)-1))
                    return
            visited.append(node)
    print("so sorry, path dose not exist :(")


print(BFS(graph, '0', goal))
