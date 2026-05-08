class Grafo:
    def __init__(self, num_vertices, ponderado):
        self.num_vertices = num_vertices
        self.ponderado = ponderado
        self.num_arestas = 0

    def inserir_aresta(self, u, v, peso=1):
        raise NotImplemented("Esse método deve ser sobrescrito pela subclasse!")
    
    def info(self):
        "Informa número de vértices, arestas e grau médio"
        grau_medio = (2 * self.num_arestas) / self.num_vertices
        print(f"n = {self.num_vertices}")
        print(f"m = {self.num_arestas}")
        print(f"d_médio = {grau_medio:.1f}")
