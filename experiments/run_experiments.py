import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import networkx as nx
from src.ga import genetic_algorithm_labeling
import time


def generate_default_graph(path):
    """
    Gera um grafo caminho (P10) e salva no formato GraphML.
    """
    print("⚠️  Arquivo de grafo está vazio ou ausente. Gerando P₁₀ como fallback...")
    G = nx.path_graph(10)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    nx.write_graphml(G, path)


def load_graph(path):
    """
    Carrega um grafo no formato GraphML.
    Se o arquivo estiver vazio ou ausente, gera um grafo P₁₀.
    """
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        generate_default_graph(path)

    try:
        return nx.read_graphml(path)
    except Exception as e:
        print(f"Erro ao carregar o grafo: {e}")
        print("Gerando grafo padrão P₁₀...")
        generate_default_graph(path)
        return nx.read_graphml(path)


def main():
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

    best_solution, lambda_value, labeling = genetic_algorithm_labeling(
        graph,
        population_size=population_size,
        generations=generations,
        mutation_rate=mutation_rate
    )

    end = time.time()
    duration = end - start

    print(f"\nMelhor ordem encontrada: {best_solution}")
    print(f"λ(G) = {lambda_value}")
    print(f"Melhor solução encontrada: {labeling}")
    print(f"Tempo de execução: {duration:.2f} segundos")

    # Salvar resultado em arquivo
    os.makedirs("results", exist_ok=True)
    with open("results/caminho_result.txt", "w") as f:
        f.write(f"Instância: {graph_path}\n")
        f.write(f"Número de vértices: {graph.number_of_nodes()}\n")
        f.write(f"Melhor ordem: {best_solution}\n")
        f.write(f"λ(G): {lambda_value}\n")
        f.write(f"Melhor solução encontrada: {labeling}\n")
        f.write(f"Tempo: {duration:.2f} segundos\n")

    print("\n✅ Resultado salvo em results/caminho_result.txt")


if __name__ == "__main__":
    main()