import math
import random

# initialize values of alpha & beta
MAX, MIN = 1000, -1000

# number of turns for Riyad (depth of the tree)
turns = int(input())
# calculating depth
depth = 2 * turns
print("Depth: ", depth)

# branches per each node
branch = int(input())
print("Branch: ", branch)

# range of the values of the leaf nodes
rangeValue = input().split()
x = int(rangeValue[0])
y = int(rangeValue[1])

# calculating leaf value of leaf nodes
leafNodeNumber = int(math.pow(branch, depth))
print("Terminal states(leaf nodes): ", leafNodeNumber)

# leaf node value assigning
leafNodes = random.sample(range(x, y), leafNodeNumber)
# print(str(leafNodes))

# given lab assignment leaf node values
assignmentValues = [3, 12, 8, 2, 4, 6, 14, 5, 2]

count = 0


def minimaxAlphaBeta(depthTree, nodeIndexValue, maximizingPlayer,
            values, alpha, beta, depth, branch):

    global count

    if depthTree == depth:
        return values[nodeIndexValue]

    if maximizingPlayer:

        bestValue = MIN

        # Recur for left and right children
        for i in range(0, branch):

            value = minimaxAlphaBeta(depthTree + 1, nodeIndexValue * branch + i,
                          False, values, alpha, beta, depth, branch)
            bestValue = max(bestValue, value)
            alpha = max(alpha, bestValue)

            # Alpha Beta Pruning
            if beta <= alpha:
                # counting the pruned nodes
                count += 1
                break

        return bestValue

    else:
        bestValue = MAX

        # Recur for left and
        # right children
        for i in range(0, branch):

            value = minimaxAlphaBeta(depthTree + 1, nodeIndexValue * branch + i,
                          True, values, alpha, beta, depth, branch)
            bestValue = min(bestValue, value)
            beta = min(beta, bestValue)

            # Alpha Beta Pruning
            if beta <= alpha:
                # counting the prune nodes
                count += 1
                break

        return bestValue


# Driver Code
if __name__ == "__main__":
    initialNode = 0
    initialDepth = 0
    amount = minimaxAlphaBeta(initialDepth, initialNode, True, leafNodes, MIN, MAX, depth, branch)
    print("Maximum amount:", amount)
    print("Comparisons:", leafNodeNumber)
    print("comparisons:", (leafNodeNumber - count))
    # print(count)
