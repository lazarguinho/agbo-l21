import matplotlib.pyplot as plt
import os


import matplotlib.pyplot as plt


def plot_convergence(convergences, title=None, save_path=None):
    """
    Plota múltiplas curvas de convergência.

    Parameters:
    - convergences: lista de listas, onde cada sublista representa a evolução de uma execução.
    - title: título do gráfico.
    - save_path: caminho para salvar o gráfico.
    """
    plt.figure()

    for i, curve in enumerate(convergences):
        plt.plot(curve, label=f'Execução {i+1}', linewidth=1)

    plt.xlabel("Geração")
    plt.ylabel("λ(G)")
    if title:
        plt.title(title)
    plt.legend()
    plt.grid(True)

    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
        print(f"📈 Gráfico de convergência salvo em: {save_path}")
    else:
        plt.show()

    plt.close()