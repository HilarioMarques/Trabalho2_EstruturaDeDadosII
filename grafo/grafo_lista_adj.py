from grafo import Grafo

class GrafoListaAdjacencia(Grafo):
    def __init__(self, num_vertices, ponderado):
        #chama o construtor da superclasse Grafo, evita repetições
        super().__init__(num_vertices, ponderado)

        #a lista de adjacencia será inicializada na forma de um dicionário
        #a chave será o vértice e o valor é uma lista de vizinhos
        self.adj = {i: [] for i in range(1, num_vertices + 1)}

    def inserir_aresta(self, u, v, peso=None):

        if self.ponderado:
            #armazena em tuplas (vizinho, peso)
            self.adj[u].append((v, peso))
            self.adj[v].append((u, peso))
        else:
            #como não é ponderado, armazena apenas o vizinho
            self.adj[u].append(v)
            self.adj[v].append(u)

        self.num_arestas += 1

    def Print(self):
        for i in range(1, num_vertices + 1):
            if self.ponderado:
                vizinhos = " ".join([f"{v}({p})" for v, p in self.adj[i]])
            else:
                vizinhos = " ".join(map(str, self.adj[i]))

            print(f"{i}: {vizinhos}")

            #IMCOMPLETO 
