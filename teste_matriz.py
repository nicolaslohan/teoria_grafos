from meu_grafo_matriz_adj_nao_dir import MeuGrafo

grafo = MeuGrafo()
grafo_paraiba = MeuGrafo()
grafo_paraiba.adiciona_vertice("J")
grafo_paraiba.adiciona_vertice("C")
grafo_paraiba.adiciona_vertice("E")
grafo_paraiba.adiciona_vertice("P")
grafo_paraiba.adiciona_vertice("M")
grafo_paraiba.adiciona_vertice("T")
grafo_paraiba.adiciona_vertice("Z")
grafo_paraiba.adiciona_aresta('a1', 'J', 'C')
grafo_paraiba.adiciona_aresta('a2', 'C', 'E')
grafo_paraiba.adiciona_aresta('a3', 'C', 'E')
grafo_paraiba.adiciona_aresta('a4', 'P', 'C')
grafo_paraiba.adiciona_aresta('a5', 'P', 'C')
grafo_paraiba.adiciona_aresta('a6', 'T', 'C')
grafo_paraiba.adiciona_aresta('a7', 'M', 'C')
grafo_paraiba.adiciona_aresta('a8', 'M', 'T')
grafo_paraiba.adiciona_aresta('a9', 'T', 'Z')

g_c = MeuGrafo()
g_c.adiciona_vertice("J")
g_c.adiciona_vertice("C")
g_c.adiciona_vertice("E")
g_c.adiciona_vertice("P")
g_c.adiciona_aresta('a1', 'J', 'C')
g_c.adiciona_aresta('a2', 'J', 'E')
g_c.adiciona_aresta('a3', 'J', 'P')
g_c.adiciona_aresta('a4', 'E', 'C')
g_c.adiciona_aresta('a5', 'P', 'C')
g_c.adiciona_aresta('a6', 'P', 'E')

g_l1 = MeuGrafo()
g_l1.adiciona_vertice("A")
g_l1.adiciona_vertice("B")
g_l1.adiciona_vertice("C")
g_l1.adiciona_vertice("D")
g_l1.adiciona_aresta('a1', 'A', 'A')
g_l1.adiciona_aresta('a2', 'A', 'B')
g_l1.adiciona_aresta('a3', 'A', 'A')

dicionario_arestas = grafo_paraiba.matriz

vertices = {}
for v in g_l1.vertices:
    vertices[str(v)] = g_l1.vertices.index(v)

"""for j in range(len(vertices)):
    for i in range(len(vertices)):
        if len(grafo_paraiba.matriz[j][i]) == 2:
            print("Tem Paralela")"""

"""for j in range(len(vertices)):
    if len(grafo_paraiba.matriz[j][j]) > 0:
        print("Tem laço")
else:
    print("Não tem laço")
    """

"""for i in range(len(vertices)):
    for j in range(len(vertices)):
        print(g_l1.matriz[i][j])"""
print(g_l1.grau("A"))
print(g_l1.arestas_sobre_vertice("A"))
