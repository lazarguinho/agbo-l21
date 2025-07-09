import random

def mutate(individual, mutation_rate):
    mutated_individual = individual.copy()
    if random.random() < mutation_rate:
       index1, index2 = random.sample(range(len(individual)), 2)
       mutated_individual[index1], mutated_individual[index2] = individual[index2], individual[index1]

    return mutated_individual