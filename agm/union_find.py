class UnionFind:
    """
    - Estrutura Union-Find (Disjoint Set).
    - Usada para detectar ciclos no algoritmo de Kruskal.
    """

    def __init__(self, num_vertices):
        """
        Inicializa os conjuntos. Cada vértice começa sendo pai dele mesmo.
        """

        self.pai = []

        for i in range(num_vertices + 1):
            self.pai.append(i)

    def find(self, x):
        """ Encontra o representante (líder do conjunto)."""

        if self.pai[x] == x:
            return x
        
        return self.find(self.pai[x])
    
    def union(self, x, y):
        """ Une dois conjuntos """

        raiz_x = self.find(x)
        raiz_y = self.find(y)

        if raiz_x != raiz_y:
            self.pai[raiz_y] = raiz_x

