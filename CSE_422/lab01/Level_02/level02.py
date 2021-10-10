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

goal = input("Enter Lina's position: ")

# attacker's dictionary
position = {}

position['Nora'] = input("Enter Nora's position: ")
position['lara'] = input("Enter lara's position: ")

# print(position)

# loop with function for DFS traversal

# list of minimum distances of nora and lara
score = []
# dictionary of minimum distances of nora and lara
minimum ={}
for x in position:
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
                        # print((len(new_path) - 1))
                        score.append((len(new_path) - 1))
                        minimum[x] = (len(new_path) - 1)
                        return
                visited.append(node)
        print("so sorry, path dose not exist :(")


    BFS(graph, position[x], goal)
# print(BFS(graph, position, goal))
# print(min(score))
print(min(minimum))