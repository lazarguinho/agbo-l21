import random

def initialize_population(population_size, nodes):
    population = []
    nodes = list(nodes)  # pode ser NodeView
    for _ in range(population_size):
        individual = nodes.copy()
        random.shuffle(individual)
        population.append(individual)
    return population