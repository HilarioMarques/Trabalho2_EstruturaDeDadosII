from grafo.grafo_lista_adj import GrafoListaAdjacencia

def ler_arquivo(caminho_arquivo):
    "Lê um arquivo de grafo e retorna um objeto GrafoListaAdj pronto."

    with open(caminho_arquivo, "r") as arquivo:
        #lê a primeira linha
        primeira_linha = arquivo.readline().split()
        
        #pega informações
        num_vertices = int(primeira_linha[0])

        #converte 0/1 para False/True
        ponderado = bool(int(primeira_linha[1]))

        #cria o grafo
        grafo = GrafoListaAdjacencia(num_vertices, ponderado)

        for linha in arquivo:
            dados = linha.split()

            if ponderado:
                u = int(dados[0])
                v = int(dados[1])
                peso = int(dados[2])

                grafo.inserir_aresta(u, v, peso)
            else:
                u = int(dados[0])
                v = int(dados[1])

                grafo.inserir_aresta(u, v)

    return grafo