from meu_grafo_matriz_adj_dir import MeuGrafo

grafo_paraiba = MeuGrafo()
grafo_paraiba.adiciona_vertice("J")
grafo_paraiba.adiciona_vertice("C")
grafo_paraiba.adiciona_vertice("E")
grafo_paraiba.adiciona_vertice("P")
grafo_paraiba.adiciona_vertice("M")
grafo_paraiba.adiciona_vertice("T")
grafo_paraiba.adiciona_vertice("Z")
grafo_paraiba.adiciona_aresta('a1', 'J', 'C', 2)
grafo_paraiba.adiciona_aresta('a2', 'C', 'E', 3)
grafo_paraiba.adiciona_aresta('a3', 'E', 'C', 3)
grafo_paraiba.adiciona_aresta('a4', 'C', 'P', 1)
grafo_paraiba.adiciona_aresta('a5', 'P', 'C', 2)
grafo_paraiba.adiciona_aresta('a6', 'C', 'T', 2)
grafo_paraiba.adiciona_aresta('a7', 'M', 'C', 3)
grafo_paraiba.adiciona_aresta('a8', 'M', 'T', 4)
grafo_paraiba.adiciona_aresta('a9', 'T', 'Z', 1)

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

vertices = {}
for v in g_l1.vertices:
    vertices[str(v)] = g_l1.vertices.index(v)

print(g_l1.grau("A"))
print(g_l1.arestas_sobre_vertice("A"))

# print(list(vertices.keys())[list(vertices.values()).index(0)]) {grafo_paraiba.vertices[v]} - {grafo_paraiba.vertices[h]} ->

# g_l1.dijkstra("A", "B")

for v in range(len(grafo_paraiba.vertices)):
    for h in range(len(grafo_paraiba.vertices)):
        if (len(grafo_paraiba.matriz[v][h])) > 0:
            for a in grafo_paraiba.matriz[v][h]:
                print(f'{grafo_paraiba.vertices[v]} - {grafo_paraiba.vertices[h]} -> {grafo_paraiba.matriz[v][h][a].peso}')

print("\n\n")
print(grafo_paraiba.dijkstra("J", "T"))
