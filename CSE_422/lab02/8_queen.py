import random
import itertools

'This may take a long time to show' \
 'desired result as i am picking random values so the result' \
 'will be varying each time'

# maximum fitness = n(n-1)/2 = 28 --> n = queens number
maximumFitness = 28


# fitness checking of individual population
def fitness(populationIndividual):
    diagonalCollisions = 0
    horizontalCollisions = sum([populationIndividual.count(queen) - 1 for queen in populationIndividual]) // 2

    leftDiagonal = [0] * len(populationIndividual) * 2
    rightDiagonal = [0] * len(populationIndividual) * 2
    for i in range(len(populationIndividual)):
        leftDiagonal[i + populationIndividual[i] - 1] += 1
        rightDiagonal[len(populationIndividual) - i + populationIndividual[i] - 2] += 1

    for i in range(2 * len(populationIndividual) - 1):
        count = 0
        if leftDiagonal[i] > 1:
            count += leftDiagonal[i] - 1
        if rightDiagonal[i] > 1:
            count += rightDiagonal[i] - 1
        diagonalCollisions += count / (len(populationIndividual) - abs(i - len(populationIndividual) + 1))

    return int(maximumFitness - (horizontalCollisions + diagonalCollisions))


# probablity of ftiness of the individual population
def probability(populationIndividual, fitness):
    return fitness(populationIndividual) / maximumFitness


def randomPick(population, probabilities):
    total = sum(a for c, a in itertools.zip_longest(population, probabilities))
    r = random.uniform(0, total)
    iterate = 0
    for c, a in itertools.zip_longest(population, probabilities):
        num = iterate + a
        if num >= r:
            return c
        iterate += a


def crossOver(parent1, parent2):
    cutPoint = random.randint(0, len(parent1) - 1)
    return parent1[0:cutPoint] + parent2[cutPoint:len(parent1)]


def mutate(child):
    x = random.randint(0, len(child) - 1)
    y = random.randint(1, len(child))
    child[x] = y
    return child


def geneticTesting(population, fitness):
    mutationProbability = 0.4
    newPopulation = []
    probabilities = [probability(n, fitness) for n in population]
    for i in range(len(population)):
        x = randomPick(population, probabilities)
        y = randomPick(population, probabilities)
        child = crossOver(x, y)
        if random.random() < mutationProbability:
            child = mutate(child)
        printIndividual(child)
        newPopulation.append(child)
        if fitness(child) == 28:
            break
    return newPopulation


def printIndividual(child):
    print("{},  Fitness = {}, Probability = {:.6f}"
          .format(str(child), fitness(child), probability(child, fitness)))
    return


def populationInitialization(size):
    return [random.randrange(1, size, 1) for _ in range(size)]


numberOfQueens = 8
populationNumber = 10
population = [populationInitialization(numberOfQueens) for _ in range(populationNumber)]
generation = 1


def geneticAlgorithm(fitness, population, generation, geneticTesting, printIndividual):
    while 28 not in [fitness(i) for i in population]:
        print(" Generation {} =".format(generation))
        population = geneticTesting(population, fitness)
        print("Fitness of the population = {}".format(max([fitness(n) for n in population])))
        generation += 1

    print("Solved in Generation {}".format(generation - 1))
    for x in population:
        if fitness(x) == 28:
            printIndividual(x)

    return


geneticAlgorithm(fitness, population, generation, geneticTesting, printIndividual)
