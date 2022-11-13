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

grafo = MeuGrafo()
grafo.adiciona_vertice("A")
grafo.adiciona_vertice("B")
grafo.adiciona_vertice("C")
grafo.adiciona_vertice("D")
grafo.adiciona_vertice("E")
grafo.adiciona_vertice("F")
grafo.adiciona_aresta("a1", "A", "B", 2)
grafo.adiciona_aresta("a2", "A", "C", 1)
grafo.adiciona_aresta("a3", "B", "D", 1)
grafo.adiciona_aresta("a4", "C", "D", 3)
grafo.adiciona_aresta("a5", "C", "F", 15)
grafo.adiciona_aresta("a6", "D", "E", 2)
grafo.adiciona_aresta("a7", "E", "F", 3)

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

for v in range(len(grafo.vertices)):
    for h in range(len(grafo.vertices)):
        if (len(grafo.matriz[v][h])) > 0:
            for a in grafo.matriz[v][h]:
                print(f'{grafo.matriz[v][h][a]}')

print("\n\n")
#print(grafo.arestas_sobre_vertice("A"))
print(grafo_paraiba.dijkstra("J", "M"))