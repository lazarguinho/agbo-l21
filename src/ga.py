import random
from src.greedy import greedy_labeling
from src.selection import select_parents
from src.crossover import crossover
from src.mutation import mutate
from src.utils import initialize_population


def fitness_function(graph, order):
    return greedy_labeling(graph, order)


def genetic_algorithm_labeling(graph, population_size, generations, mutation_rate):
    population = initialize_population(population_size, graph.nodes())
    for _ in range(generations):
        fitness_values = [fitness_function(graph, individual) for individual in population]

        elites = sorted(population, key=lambda x: fitness_function(graph, x), reverse=False)[:2]
        new_population = elites

        while len(new_population) < population_size:
            parent1, parent2 = select_parents(population, fitness_values)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population

    return min(population, key=lambda x: fitness_function(graph, x))