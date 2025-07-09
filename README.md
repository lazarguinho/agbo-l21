# AGBO-L21

Algoritmo Genético Baseado em Ordem (AGBO) para o problema de rotulação–L(2,1) em grafos, utilizando representação por permutação e heurística gulosa.

## 📘 Descrição

Este projeto implementa uma abordagem baseada em algoritmos genéticos para resolver o problema de rotulação–L(2,1), onde o objetivo é rotular os vértices de um grafo de modo que:

- Vértices adjacentes recebam rótulos com diferença de pelo menos 2;
- Vértices a distância 2 recebam rótulos diferentes.

A heurística gulosa é utilizada como função de aptidão, avaliando o valor de $\lambda(G)$ associado à ordem dos vértices proposta por cada indivíduo da população.

## 📂 Estrutura do Projeto

- `src/`: Código-fonte do algoritmo genético
  - `ga.py`: Funções para execução do algoritmo genético
  - `greedy.py`: Heurística gulosa para avaliação de indivíduos
  - `crossover.py`: Função de crossover para cruzamento de indivíduos
  - `mutation.py`: Função de mutação para alteração de indivíduos
  - `selection.py`: Função de seleção para escolha de pais
  - `utils.py`: Funções auxiliares para manipulação de grafos e ordenações
- `data/`: Instâncias de grafos (formato .graphml)
  - `caminho.graphml`: Exemplo de instância de grafo
- `experiments/`: Scripts para execução e análise
  - `run_experiments.py`: Script para execução de experimentos
- `figures/`: Figuras utilizadas em relatórios
- `results/`: Resultados gerados pelos experimentos
- `requirements.txt`: Dependências do projeto
- `README.md`: Este arquivo

## 🚀 Execução

1. Clone o repositório:

```bash
git clone https://github.com/lazarguinho/agbo-l21
cd agbo-l21
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute os experimentos:

```bash
python experiments/run_experiments.py
```

Os resultados serão salvos no diretório `results/`.