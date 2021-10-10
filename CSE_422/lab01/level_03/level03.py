# number of nodes user input
node = int(input("Enter the number of node: "))
# print(node)

# number of connections from user input
connections = int(input("Enter the number of connections: "))
# print(connections)

# initializing dictionary
graph = {}

print(graph)
# loop to store connection of nodes from user input
for i in range(connections):
    text = input().split()
    key = int(text[0])
    value = int(text[1])
    graph[key] = []
    graph[key].append(value)
    graph[value].append(key)

print(graph)

goal = input("Enter lina's position: ")
participants = int(input("Enter the number of participants: "))

attacker = []
score = []
for i in range(participants):
    warrior = int(input("Enter warior's position: "))
    attacker.append(warrior)
# print(attacker)
for x in attacker:
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
                        return
                visited.append(node)
        print("so sorry, path dose not exist :(")
    BFS(graph, goal,attacker[x])
print(min(score))
