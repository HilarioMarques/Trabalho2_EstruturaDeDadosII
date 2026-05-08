from grafo.grafo import Grafo

class GrafoListaAdjacencia(Grafo):
    def __init__(self, num_vertices, ponderado):
        #chama o construtor da superclasse Grafo, evita repetições
        super().__init__(num_vertices, ponderado)

        # Dicionário da lista de adjacência
        # Exemplo:
        # {
        #     1: [],
        #     2: [],
        #     3: []
        # }
        self.adj = {}

        #inicializando todos os vértices com listas vazias
        for i in range(1, self.num_vertices+1):
            self.adj[i] = []

    def inserir_aresta(self, u, v, peso=None):
        """
        Adiciona uma aresta no grafo.
        Como o grafo é não direcionado,
        adicionamos nos dois sentidos.
        
        Para u: vértice origem
        Para v: vértice destino
        Para peso: peso da aresta (opcional)
        """
        
        self.adj[u].append((v, peso))
        self.adj[v].append((u, peso))


    def Print(self):
        """Exibe a lista de adjacência do grafo"""

        for vertice in self.adj:
            print(f"{vertice}: ", end="")

            for vizinho, peso in self.adj[vertice]:

                if self.ponderado:
                    print(f"{vizinho}({peso}) ", end="")
                else:
                    print(f"{vizinho}: ", end="")
            print()

    def info(self):
        "Informa número de vértices, arestas e grau médio"
        n = self.num_vertices

        #soma dos graus de todos os vértices
        soma_graus = 0

        for vertice in self.adj:
            soma_graus += len(self.adj[vertice])

        # Como o grafo não direcionado armazena cada aresta duas vezes:
        m = soma_graus // 2

        grau_medio = soma_graus / n
        
        print(f"n = {n}")
        print(f"m = {m}")
        print(f"grau médio = {grau_medio}")
