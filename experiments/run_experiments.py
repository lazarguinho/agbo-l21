import random
import sys
import os
import time
import networkx as nx
from concurrent.futures import ProcessPoolExecutor
from networkx.readwrite import json_graph
import csv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ga import genetic_algorithm_labeling
from experiments.plot_convergence import plot_convergence


def generate_complete_graph(num_nodes, seed):
    random.seed(seed)
    G = nx.complete_graph(num_nodes)
    nx.set_node_attributes(G, {i: str(i) for i in G.nodes()}, name="label")
    return G


def get_graph_path(index):
    return f"data/completo_{index+1}.graphml"


def save_graph(graph, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    nx.write_graphml(graph, path)


def load_or_generate_graph(index, num_nodes, seed):
    path = get_graph_path(index)
    if os.path.exists(path) and os.path.getsize(path) > 0:
        try:
            print(f"⚠️  Carregando grafo completo {index+1} com seed {seed}")
            return nx.read_graphml(path)
        except Exception as e:
            print(f"Erro ao carregar {path}, gerando novo grafo. Erro: {e}")

    print(f"⚠️  Gerando grafo completo aleatório {index+1} com seed {seed}")
    G = generate_complete_graph(num_nodes, seed)
    save_graph(G, path)
    return G


def run_single_execution(graph_data, population_size, generations, mutation_rate):
    # Esta função será executada em subprocessos
    import networkx as nx
    from src.ga import genetic_algorithm_labeling

    G = json_graph.node_link_graph(graph_data, edges="edges")

    start = time.time()
    solution, span_value, labeling, convergence = genetic_algorithm_labeling(
        G,
        population_size=population_size,
        generations=generations,
        mutation_rate=mutation_rate
    )
    end = time.time()
    return span_value, solution, labeling, convergence, end - start


def main():
    num_graphs = 7
    num_nodes = 10
    base_seed = 42

    population_size = 20
    generations = 100
    mutation_rate = 0.1
    runs_per_graph = 5

    os.makedirs("results", exist_ok=True)

    csv_data = []

    for i in range(num_graphs):
        seed = base_seed + i
        graph = load_or_generate_graph(i, num_nodes, seed)

        print(f"\n📊 Executando grafo completo {i+1}/{num_graphs} (|V| = {graph.number_of_nodes()})")

        span_values = []
        times = []
        all_convergences = []

        best_span = float('inf')
        best_result = None
        best_solution = None

        graph_data = json_graph.node_link_data(graph, edges="edges")

        with ProcessPoolExecutor() as executor:
            futures = [
                executor.submit(
                    run_single_execution,
                    graph_data,
                    population_size,
                    generations,
                    mutation_rate
                ) for _ in range(runs_per_graph)
            ]
            results = [f.result() for f in futures]

        for span_value, solution, labeling, convergence, duration in results:
            span_values.append(span_value)
            times.append(duration)
            all_convergences.append(convergence)

            if span_value < best_span:
                best_span = span_value
                best_result = labeling
                best_solution = solution

        avg_span = sum(span_values) / runs_per_graph
        avg_time = sum(times) / runs_per_graph

        min_time = min(times)
        max_time = max(times)
        lambda_g = 2 * graph.number_of_nodes() - 2

        print(f"✅ Melhor span(G) = {best_span}")
        print(f"📈 Span(G) médio = {avg_span:.2f}")
        print(f"⏱️ Tempo médio = {avg_time:.2f} segundos")

        # Gráfico
        plot_path = f"results/convergencia_{i+1}.png"
        plot_convergence(all_convergences, title=f"Convergência - Grafo K_{graph.number_of_nodes()}", save_path=plot_path)

        # TXT
        result_path = f"results/completo_{i+1}_result.txt"
        with open(result_path, "w") as f:
            f.write(f"Instância: completo_{i+1}.graphml\n")
            f.write(f"Número de vértices: {graph.number_of_nodes()}\n")
            f.write(f"Seed base: {seed}\n")
            f.write(f"Execuções por grafo: {runs_per_graph}\n\n")
            f.write(f"Melhor span(G): {best_span}\n")
            f.write(f"Melhor ordem: {best_solution}\n")
            f.write(f"Melhor solução encontrada: {best_result}\n\n")
            f.write(f"Span(G) médio: {avg_span:.2f}\n")
            f.write(f"Tempo médio: {avg_time:.2f} segundos\n")
            f.write(f"Valores individuais de span(G): {span_values}\n")
            f.write(f"Tempos individuais: {[round(t, 2) for t in times]}\n")

        print(f"📝 Resultados salvos em {result_path}")

        # Adiciona linha ao CSV
        csv_data.append([
            f"K_{graph.number_of_nodes()}",
            graph.number_of_nodes(),
            best_span,
            round(avg_span, 2),
            lambda_g,
            round(min_time, 2),
            round(avg_time, 2),
            round(max_time, 2)
        ])

        num_nodes += 10

    # Salva CSV no final
    csv_path = "results/resumo.csv"
    with open(csv_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Grafo", "|V|", "span minimo", "span medio", "λ(G)", "Tempo minimo", "Tempo medio", "Tempo maximo"])
        writer.writerows(csv_data)

    print(f"📁 CSV de resumo salvo em {csv_path}")


if __name__ == "__main__":
    main()