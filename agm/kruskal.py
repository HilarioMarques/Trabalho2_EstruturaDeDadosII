from agm.agm import AGM
from agm.union_find import UnionFind

class Kruskal(AGM):

    def executar(self):
        """
        Executa o algoritmo de Kruskal.

        Retorna:
        - mst (lista de arestas)
        - peso_total
        """

        if not self.grafo.ponderado:
            raise ValueError("Para fazer a MST, o grafo precisa ser ponderado!!")
        
        arestas = []

        for u in self.grafo.adj:
            for v, peso in self.grafo.adj[u]:
                #evitando repetir (u, v) e (v, u)
                if u < v:
                    arestas.append((u, v, peso))
        
        arestas_ordenadasPeso = sorted(arestas, key=lambda aresta: aresta[2])

        uf = UnionFind(self.grafo.num_vertices)

        mst = []
        peso_total = 0

        for u, v, peso in arestas_ordenadasPeso:

            if uf.find(u) != uf.find(v):
                uf.union(u, v)

                mst.append((u, v, peso))
                peso_total += peso
        
        return mst, peso_total

    def imprimir_MST(self, mst, peso_total):
        """ Imprime a árvore geradora mínima """

        print(f"Peso total: {peso_total}")

        for u, v, peso in mst:
            print(f"Aresta {u} - {v}; peso {peso}")