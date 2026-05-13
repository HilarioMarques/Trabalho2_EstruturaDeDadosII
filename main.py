from grafo.grafo_lista_adj import GrafoListaAdjacencia
from utils.leitor_arquivo import ler_arquivo
from busca.busca_largura import BuscaLargura
from agm.union_find import UnionFind
from agm.kruskal import Kruskal

def main():
    
   grafo = ler_arquivo("entrada_ponderada.txt")
   print("---PRINT---")
   grafo.Print()

   print("\n---INFO---")
   grafo.info()

   print("\n---BFS---")
   bfs = BuscaLargura(grafo)
   pai, nivel = bfs.buscar(1)

   bfs.imprimir_busca(pai, nivel)

   print("\n---MST KRUSKAL---")
   kruskal = Kruskal(grafo)
   mst, peso_total = (kruskal.executar())

   kruskal.imprimir_MST(mst, peso_total)

if __name__ == "__main__":
    main()