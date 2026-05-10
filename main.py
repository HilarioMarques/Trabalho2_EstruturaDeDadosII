from grafo.grafo_lista_adj import GrafoListaAdjacencia
from utils.leitor_arquivo import ler_arquivo
from busca.busca_largura import BuscaLargura

def main():
    
    grafo = ler_arquivo("entrada.txt")

    print("=== PRINT DO GRAFO ===")
    grafo.Print()

    print("\n=== INFO ===")
    grafo.info()

    print("\n=== BFS ===")
    bfs = BuscaLargura(grafo)

    pai, nivel = bfs.buscar(1)

    bfs.imprimir_busca(pai, nivel)

if __name__ == "__main__":
    main()