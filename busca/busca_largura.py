from collections import deque
from busca.busca import Busca

class BuscaLargura(Busca):

    def buscar(self, raiz):
        """
        Executa busca em largura (BFS) a partir do vértice raiz.

        Retorna:
        - pai
        - nivel
        """

        visitados = set()

        pai = {}
        nivel = {}

        fila = deque()

        #iniciar a raiz
        visitados.add(raiz)

        pai[raiz] = None
        nivel[raiz] = 0

        fila.append(raiz)

        while fila:

            vertice_atual = fila.popleft()

            for vizinho, __ in self.grafo.adj[vertice_atual]:

                if vizinho not in visitados:
                    visitados.add(vizinho)

                    pai[vizinho] = vertice_atual
                    nivel[vizinho] = nivel[vertice_atual] + 1

                    fila.append(vizinho)
        return pai, nivel
    
    def imprimir_busca(self, pai, nivel):
        "Imprime o resultado da BFS do jeito que o trabalho pede"

        for vertice in nivel:
            pai_vertice = pai[vertice]

            if pai_vertice is None:
                pai_vertice = "x"

            print(
                f"No {vertice}; "
                f"Pai {pai_vertice}; "
                f"Level {nivel[vertice]};"
            )