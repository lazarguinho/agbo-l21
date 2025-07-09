import matplotlib.pyplot as plt
import os


def plot_convergence(convergence, title="Curva de Convergência do AGBO", save_path="results/convergencia.png"):
    if not convergence:
        print("⚠️ Lista de convergência vazia. Nenhum gráfico gerado.")
        return

    os.makedirs(os.path.dirname(save_path), exist_ok=True)

    plt.figure(figsize=(8, 5))
    plt.plot(convergence, marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel("Geração")
    plt.ylabel("λ(G)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

    print(f"📈 Gráfico de convergência salvo em: {save_path}")