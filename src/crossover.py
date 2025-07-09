def cycle_crossover(parent1, parent2):
    child1 = [None] * len(parent1)
    child2 = [None] * len(parent2)

    remaining_indices = set(range(len(parent1)))

    current_index = remaining_indices.pop()
    cycle = [current_index]

    while True:
        next_index = parent2.index(parent1[current_index])
        if next_index == cycle[0]:
            break  # Cycle completed
        cycle.append(next_index)
        remaining_indices.remove(next_index)
        current_index = next_index

    for index in cycle:
        child1[index] = parent1[index]
        child2[index] = parent2[index]

    for index in remaining_indices:
        child1[index] = parent2[index]
        child2[index] = parent1[index]

    return child1, child2

def crossover(parent1, parent2):
    return cycle_crossover(parent1, parent2)