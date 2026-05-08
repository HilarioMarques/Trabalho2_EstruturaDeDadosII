from grafo.grafo_lista_adj import GrafoListaAdjacencia

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


if __name__ == "__main__":
    main()