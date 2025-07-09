import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import networkx as nx
from src.ga import genetic_algorithm_labeling
import time


def load_graph(path):
    """
    Carrega um grafo no formato GraphML.
    """
    return nx.read_graphml(path)


def main():
    # Caminho da instância
    graph_path = "data/caminho.graphml"
    graph = load_graph(graph_path)

    print(f"Instância carregada: {graph_path}")
    print(f"Número de vértices: {graph.number_of_nodes()}")

    # Parâmetros do algoritmo
    population_size = 50
    generations = 100
    mutation_rate = 0.1

    print("\nExecutando AGBO...")
    start = time.time()

    best_solution = genetic_algorithm_labeling(
        graph,
        population_size=population_size,
        generations=generations,
        mutation_rate=mutation_rate
    )

    end = time.time()
    duration = end - start

    print(f"\nMelhor ordem encontrada: {best_solution}")
    # print(f"λ(G) = {lambda_value}")
    print(f"Tempo de execução: {duration:.2f} segundos")

    # Salvar resultado em arquivo
    os.makedirs("results", exist_ok=True)
    with open("results/caminho_result.txt", "w") as f:
        f.write(f"Instância: {graph_path}\n")
        f.write(f"Número de vértices: {graph.number_of_nodes()}\n")
        f.write(f"Melhor ordem: {best_solution}\n")
        # f.write(f"λ(G): {lambda_value}\n")
        f.write(f"Tempo: {duration:.2f} segundos\n")

    print("\nResultado salvo em results/caminho_result.txt")


if __name__ == "__main__":
    main()