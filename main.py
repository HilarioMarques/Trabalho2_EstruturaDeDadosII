from grafo.grafo_lista_adj import GrafoListaAdjacencia
from utils.leitor_arquivo import ler_arquivo

def main():
    
    grafo = GrafoListaAdjacencia(5, False)

    grafo.inserir_aresta(1, 2)
    grafo.inserir_aresta(2, 5)
    grafo.inserir_aresta(5, 3)
    grafo.inserir_aresta(4, 5)
    grafo.inserir_aresta(1, 5)

    print("=== PRINT DO GRAFO ===")
    grafo.Print()

    print("\n=== INFORMAÇÕES DO GRAFO ===")
    grafo.info()

    print("\n=== TESTANDO O LEITOR DE ARQUIVO ===")
    
    caminho = "entrada.txt"
    grafoLeitor = ler_arquivo(caminho)

    grafoLeitor.Print()
    grafoLeitor.info()

if __name__ == "__main__":
    main()