import random

def select_parents(population, fitness_values):
    total_fitness = sum(fitness_values)
    inverse_probabilities = [1 - fitness / total_fitness for fitness in fitness_values]
    probabilities = [inverse_probability / sum(inverse_probabilities) for inverse_probability in inverse_probabilities]
    selected_parents = random.choices(population, weights=probabilities, k=2)
    return selected_parents