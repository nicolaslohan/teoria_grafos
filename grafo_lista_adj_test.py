import unittest

from bibgrafo.vertice import Vertice

from meu_grafo_lista_adj import *
from bibgrafo.grafo_errors import *
from bibgrafo.aresta import Aresta


class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = MeuGrafo()
        self.g_p.adiciona_vertice("J")
        self.g_p.adiciona_vertice("C")
        self.g_p.adiciona_vertice("E")
        self.g_p.adiciona_vertice("P")
        self.g_p.adiciona_vertice("M")
        self.g_p.adiciona_vertice("T")
        self.g_p.adiciona_vertice("Z")
        self.g_p.adiciona_aresta('a1', 'J', 'C')
        self.g_p.adiciona_aresta('a2', 'C', 'E')
        self.g_p.adiciona_aresta('a3', 'C', 'E')
        self.g_p.adiciona_aresta('a4', 'P', 'C')
        self.g_p.adiciona_aresta('a5', 'P', 'C')
        self.g_p.adiciona_aresta('a6', 'T', 'C')
        self.g_p.adiciona_aresta('a7', 'M', 'C')
        self.g_p.adiciona_aresta('a8', 'M', 'T')
        self.g_p.adiciona_aresta('a9', 'T', 'Z')

        # grafo da paraíba Kruskall
        self.g_p_kruskall = MeuGrafo()
        self.g_p_kruskall.adiciona_vertice("J")
        self.g_p_kruskall.adiciona_vertice("C")
        self.g_p_kruskall.adiciona_vertice("E")
        self.g_p_kruskall.adiciona_vertice("P")
        self.g_p_kruskall.adiciona_vertice("M")
        self.g_p_kruskall.adiciona_vertice("T")
        self.g_p_kruskall.adiciona_vertice("Z")
        self.g_p_kruskall.adiciona_aresta('a1', 'J', 'C')
        self.g_p_kruskall.adiciona_aresta('a2', 'C', 'E')
        self.g_p_kruskall.adiciona_aresta('a4', 'P', 'C')
        self.g_p_kruskall.adiciona_aresta('a6', 'T', 'C')
        self.g_p_kruskall.adiciona_aresta('a7', 'M', 'C')
        self.g_p_kruskall.adiciona_aresta('a9', 'T', 'Z')

        # Clone do Grafo da Paraíba para ver se o método equals está funcionando
        self.g_p2 = MeuGrafo()
        self.g_p2.adiciona_vertice("J")
        self.g_p2.adiciona_vertice("C")
        self.g_p2.adiciona_vertice("E")
        self.g_p2.adiciona_vertice("P")
        self.g_p2.adiciona_vertice("M")
        self.g_p2.adiciona_vertice("T")
        self.g_p2.adiciona_vertice("Z")
        self.g_p2.adiciona_aresta('a1', 'J', 'C')
        self.g_p2.adiciona_aresta('a2', 'C', 'E')
        self.g_p2.adiciona_aresta('a3', 'C', 'E')
        self.g_p2.adiciona_aresta('a4', 'P', 'C')
        self.g_p2.adiciona_aresta('a5', 'P', 'C')
        self.g_p2.adiciona_aresta('a6', 'T', 'C')
        self.g_p2.adiciona_aresta('a7', 'M', 'C')
        self.g_p2.adiciona_aresta('a8', 'M', 'T')
        self.g_p2.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na primeira aresta
        self.g_p3 = MeuGrafo()
        self.g_p3.adiciona_vertice("J")
        self.g_p3.adiciona_vertice("C")
        self.g_p3.adiciona_vertice("E")
        self.g_p3.adiciona_vertice("P")
        self.g_p3.adiciona_vertice("M")
        self.g_p3.adiciona_vertice("T")
        self.g_p3.adiciona_vertice("Z")
        self.g_p3.adiciona_aresta('a', 'J', 'C')
        self.g_p3.adiciona_aresta('a2', 'C', 'E')
        self.g_p3.adiciona_aresta('a3', 'C', 'E')
        self.g_p3.adiciona_aresta('a4', 'P', 'C')
        self.g_p3.adiciona_aresta('a5', 'P', 'C')
        self.g_p3.adiciona_aresta('a6', 'T', 'C')
        self.g_p3.adiciona_aresta('a7', 'M', 'C')
        self.g_p3.adiciona_aresta('a8', 'M', 'T')
        self.g_p3.adiciona_aresta('a9', 'T', 'Z')

        # Outro clone do Grafo da Paraíba para ver se o método equals está funcionando
        # Esse tem um pequena diferença na segunda aresta
        self.g_p4 = MeuGrafo()
        self.g_p4.adiciona_vertice("J")
        self.g_p4.adiciona_vertice("C")
        self.g_p4.adiciona_vertice("E")
        self.g_p4.adiciona_vertice("P")
        self.g_p4.adiciona_vertice("M")
        self.g_p4.adiciona_vertice("T")
        self.g_p4.adiciona_vertice("Z")
        self.g_p4.adiciona_aresta('a1', 'J', 'C')
        self.g_p4.adiciona_aresta('a2', 'J', 'E')
        self.g_p4.adiciona_aresta('a3', 'C', 'E')
        self.g_p4.adiciona_aresta('a4', 'P', 'C')
        self.g_p4.adiciona_aresta('a5', 'P', 'C')
        self.g_p4.adiciona_aresta('a6', 'T', 'C')
        self.g_p4.adiciona_aresta('a7', 'M', 'C')
        self.g_p4.adiciona_aresta('a8', 'M', 'T')
        self.g_p4.adiciona_aresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo()
        self.g_p_sem_paralelas.adiciona_vertice("J")
        self.g_p_sem_paralelas.adiciona_vertice("C")
        self.g_p_sem_paralelas.adiciona_vertice("E")
        self.g_p_sem_paralelas.adiciona_vertice("P")
        self.g_p_sem_paralelas.adiciona_vertice("M")
        self.g_p_sem_paralelas.adiciona_vertice("T")
        self.g_p_sem_paralelas.adiciona_vertice("Z")
        self.g_p_sem_paralelas.adiciona_aresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adiciona_aresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adiciona_aresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adiciona_aresta('a7', 'T', 'Z')

        #grafo com pesos
        self.g2 = MeuGrafo()
        self.g2.adiciona_vertice("A")
        self.g2.adiciona_vertice("B")
        self.g2.adiciona_vertice("C")
        self.g2.adiciona_vertice("D")
        self.g2.adiciona_vertice("E")
        self.g2.adiciona_aresta("a1", "A", "B", 1)
        self.g2.adiciona_aresta("a2", "A", "E", 3)
        self.g2.adiciona_aresta("a3", "A", "D", 3)
        self.g2.adiciona_aresta("a4", "B", "D", 4)
        self.g2.adiciona_aresta("a5", "B", "C", 3)
        self.g2.adiciona_aresta("a6", "D", "C", 2)
        self.g2.adiciona_aresta("a7", "D", "E", 2)

        #g2 Prim
        self.g2_prim = MeuGrafo()
        self.g2_prim.adiciona_vertice("A")
        self.g2_prim.adiciona_vertice("B")
        self.g2_prim.adiciona_vertice("C")
        self.g2_prim.adiciona_vertice("D")
        self.g2_prim.adiciona_vertice("E")
        self.g2_prim.adiciona_aresta("a1", "A", "B", 1)
        self.g2_prim.adiciona_aresta("a5", "B", "C", 3)
        self.g2_prim.adiciona_aresta("a6", "D", "C", 2)
        self.g2_prim.adiciona_aresta("a7", "D", "E", 2)

        #g3
        self.g3 = MeuGrafo()
        self.g3.adiciona_vertice("A")
        self.g3.adiciona_vertice("B")
        self.g3.adiciona_vertice("C")
        self.g3.adiciona_vertice("D")
        self.g3.adiciona_vertice("E")
        self.g3.adiciona_vertice("F")
        self.g3.adiciona_aresta("a1", "A", "B", 1)
        self.g3.adiciona_aresta("a2", "A", "C", 2)
        self.g3.adiciona_aresta("a3", "B", "D", 2)
        self.g3.adiciona_aresta("a4", "D", "C", 1)
        self.g3.adiciona_aresta("a5", "C", "F", 3)
        self.g3.adiciona_aresta("a6", "B", "E", 2)
        self.g3.adiciona_aresta("a7", "E", "F", 1)

        #g3 Prim
        self.g3_prim = MeuGrafo()
        self.g3_prim.adiciona_vertice("A")
        self.g3_prim.adiciona_vertice("B")
        self.g3_prim.adiciona_vertice("C")
        self.g3_prim.adiciona_vertice("D")
        self.g3_prim.adiciona_vertice("E")
        self.g3_prim.adiciona_vertice("F")
        self.g3_prim.adiciona_aresta("a1", "A", "B", 1)
        self.g3_prim.adiciona_aresta("a3", "B", "D", 2)
        self.g3_prim.adiciona_aresta("a4", "D", "C", 1)
        self.g3_prim.adiciona_aresta("a5", "C", "F", 3)
        self.g3_prim.adiciona_aresta("a7", "E", "F", 1)

        #g3 Kruskall
        self.g3_kruskall = MeuGrafo()
        self.g3_kruskall.adiciona_vertice("A")
        self.g3_kruskall.adiciona_vertice("B")
        self.g3_kruskall.adiciona_vertice("C")
        self.g3_kruskall.adiciona_vertice("D")
        self.g3_kruskall.adiciona_vertice("E")
        self.g3_kruskall.adiciona_vertice("F")
        self.g3_kruskall.adiciona_aresta("a1", "A", "B", 1)
        self.g3_kruskall.adiciona_aresta("a2", "A", "C", 2)
        self.g3_kruskall.adiciona_aresta("a4", "D", "C", 1)
        self.g3_kruskall.adiciona_aresta("a6", "B", "E", 2)
        self.g3_kruskall.adiciona_aresta("a7", "E", "F", 1)

        # Grafos completos
        self.g_c = MeuGrafo()
        self.g_c.adiciona_vertice("J")
        self.g_c.adiciona_vertice("C")
        self.g_c.adiciona_vertice("E")
        self.g_c.adiciona_vertice("P")
        self.g_c.adiciona_aresta('a1', 'J', 'C')
        self.g_c.adiciona_aresta('a2', 'J', 'E')
        self.g_c.adiciona_aresta('a3', 'J', 'P')
        self.g_c.adiciona_aresta('a4', 'E', 'C')
        self.g_c.adiciona_aresta('a5', 'P', 'C')
        self.g_c.adiciona_aresta('a6', 'P', 'E')

        #g_c com pesos
        self.g_c_pesos = MeuGrafo()
        self.g_c_pesos.adiciona_vertice("J")
        self.g_c_pesos.adiciona_vertice("C")
        self.g_c_pesos.adiciona_vertice("E")
        self.g_c_pesos.adiciona_vertice("P")
        self.g_c_pesos.adiciona_aresta('a1', 'J', 'C', 1)
        self.g_c_pesos.adiciona_aresta('a2', 'J', 'E', 2)
        self.g_c_pesos.adiciona_aresta('a3', 'J', 'P', 2)
        self.g_c_pesos.adiciona_aresta('a4', 'E', 'C', 1)
        self.g_c_pesos.adiciona_aresta('a5', 'P', 'C', 2)
        self.g_c_pesos.adiciona_aresta('a6', 'P', 'E', 1)

        #grafo completo Kruskall
        self.g_c_kruskall = MeuGrafo()
        self.g_c_kruskall.adiciona_vertice("J")
        self.g_c_kruskall.adiciona_vertice("C")
        self.g_c_kruskall.adiciona_vertice("E")
        self.g_c_kruskall.adiciona_vertice("P")
        self.g_c_kruskall.adiciona_aresta('a1', 'J', 'C', 1)
        self.g_c_kruskall.adiciona_aresta('a4', 'E', 'C', 1)
        self.g_c_kruskall.adiciona_aresta('a6', 'P', 'E', 1)

        #grafo completo Prim
        self.g_c_prim = MeuGrafo()
        self.g_c_prim.adiciona_vertice("J")
        self.g_c_prim.adiciona_vertice("C")
        self.g_c_prim.adiciona_vertice("E")
        self.g_c_prim.adiciona_vertice("P")
        self.g_c_prim.adiciona_aresta('a1', 'J', 'C', 1)
        self.g_c_prim.adiciona_aresta('a4', 'E', 'C', 1)
        self.g_c_prim.adiciona_aresta('a6', 'P', 'E', 1)


        self.g_c2 = MeuGrafo()
        self.g_c2.adiciona_vertice("Nina")
        self.g_c2.adiciona_vertice("Maria")
        self.g_c2.adiciona_aresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo()
        self.g_c3.adiciona_vertice("Único")

        # Grafos com laco
        self.g_l1 = MeuGrafo()
        self.g_l1.adiciona_vertice("A")
        self.g_l1.adiciona_vertice("B")
        self.g_l1.adiciona_vertice("C")
        self.g_l1.adiciona_vertice("D")
        self.g_l1.adiciona_aresta('a1', 'A', 'A')
        self.g_l1.adiciona_aresta('a2', 'A', 'B')
        self.g_l1.adiciona_aresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo()
        self.g_l2.adiciona_vertice("A")
        self.g_l2.adiciona_vertice("B")
        self.g_l2.adiciona_vertice("C")
        self.g_l2.adiciona_vertice("D")
        self.g_l2.adiciona_aresta('a1', 'A', 'B')
        self.g_l2.adiciona_aresta('a2', 'B', 'B')
        self.g_l2.adiciona_aresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo()
        self.g_l3.adiciona_vertice("A")
        self.g_l3.adiciona_vertice("B")
        self.g_l3.adiciona_vertice("C")
        self.g_l3.adiciona_vertice("D")
        self.g_l3.adiciona_aresta('a1', 'C', 'A')
        self.g_l3.adiciona_aresta('a2', 'C', 'C')
        self.g_l3.adiciona_aresta('a3', 'D', 'D')
        self.g_l3.adiciona_aresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo()
        self.g_l4.adiciona_vertice("D")
        self.g_l4.adiciona_aresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo()
        self.g_l5.adiciona_vertice("C")
        self.g_l5.adiciona_vertice("D")
        self.g_l5.adiciona_aresta('a1', 'D', 'C')
        self.g_l5.adiciona_aresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo()
        self.g_d.adiciona_vertice("A")
        self.g_d.adiciona_vertice("B")
        self.g_d.adiciona_vertice("C")
        self.g_d.adiciona_vertice("D")
        self.g_d.adiciona_aresta('asd', 'A', 'B')

        self.g_d2 = MeuGrafo()
        self.g_d2.adiciona_vertice("A")
        self.g_d2.adiciona_vertice("B")
        self.g_d2.adiciona_vertice("C")
        self.g_d2.adiciona_vertice("D")

        # dfs
        self.g_p_dfs = MeuGrafo()
        self.g_p_dfs.adiciona_vertice("J")
        self.g_p_dfs.adiciona_vertice("C")
        self.g_p_dfs.adiciona_vertice("E")
        self.g_p_dfs.adiciona_vertice("P")
        self.g_p_dfs.adiciona_vertice("T")
        self.g_p_dfs.adiciona_vertice("M")
        self.g_p_dfs.adiciona_vertice("Z")
        self.g_p_dfs.adiciona_aresta('a1', 'J', 'C')
        self.g_p_dfs.adiciona_aresta('a2', 'C', 'E')
        self.g_p_dfs.adiciona_aresta('a4', 'C', 'P')
        self.g_p_dfs.adiciona_aresta('a6', 'C', 'T')
        self.g_p_dfs.adiciona_aresta('a8', 'M', 'T')
        self.g_p_dfs.adiciona_aresta('a9', 'T', 'Z')

        # bfs
        self.g_p_bfs = MeuGrafo()
        self.g_p_bfs.adiciona_vertice("J")
        self.g_p_bfs.adiciona_vertice("C")
        self.g_p_bfs.adiciona_vertice("E")
        self.g_p_bfs.adiciona_vertice("P")
        self.g_p_bfs.adiciona_vertice("T")
        self.g_p_bfs.adiciona_vertice("M")
        self.g_p_bfs.adiciona_vertice("Z")
        self.g_p_bfs.adiciona_aresta('a1', 'J', 'C')
        self.g_p_bfs.adiciona_aresta('a2', 'C', 'E')
        self.g_p_bfs.adiciona_aresta('a4', 'C', 'P')
        self.g_p_bfs.adiciona_aresta('a6', 'C', 'T')
        self.g_p_bfs.adiciona_aresta('a7', 'C', 'M')
        self.g_p_bfs.adiciona_aresta('a9', 'T', 'Z')

        # grafo teste 1
        self.grafo_teste = MeuGrafo()
        self.grafo_teste.adiciona_vertice("A")
        self.grafo_teste.adiciona_vertice("B")
        self.grafo_teste.adiciona_vertice("C")
        self.grafo_teste.adiciona_vertice("D")
        self.grafo_teste.adiciona_vertice("E")
        self.grafo_teste.adiciona_vertice("F")
        self.grafo_teste.adiciona_aresta("a1", "A", "B")
        self.grafo_teste.adiciona_aresta("a2", "A", "D")
        self.grafo_teste.adiciona_aresta("a3", "B", "C")
        self.grafo_teste.adiciona_aresta("a4", "B", "D")
        self.grafo_teste.adiciona_aresta("a5", "D", "C")
        self.grafo_teste.adiciona_aresta("a6", "D", "E")
        self.grafo_teste.adiciona_aresta("a7", "C", "E")
        self.grafo_teste.adiciona_aresta("a8", "E", "F")

        # grafo teste kruskall
        self.grafo_teste_kruskall = MeuGrafo()
        self.grafo_teste_kruskall.adiciona_vertice("A")
        self.grafo_teste_kruskall.adiciona_vertice("B")
        self.grafo_teste_kruskall.adiciona_vertice("C")
        self.grafo_teste_kruskall.adiciona_vertice("D")
        self.grafo_teste_kruskall.adiciona_vertice("E")
        self.grafo_teste_kruskall.adiciona_vertice("F")
        self.grafo_teste_kruskall.adiciona_aresta("a1", "A", "B")
        self.grafo_teste_kruskall.adiciona_aresta("a2", "A", "D")
        self.grafo_teste_kruskall.adiciona_aresta("a3", "B", "C")
        self.grafo_teste_kruskall.adiciona_aresta("a6", "D", "E")
        self.grafo_teste_kruskall.adiciona_aresta("a8", "E", "F")

        # grafo teste dfs D
        self.grafo_teste_dfs = MeuGrafo()
        self.grafo_teste_dfs.adiciona_vertice("A")
        self.grafo_teste_dfs.adiciona_vertice("B")
        self.grafo_teste_dfs.adiciona_vertice("C")
        self.grafo_teste_dfs.adiciona_vertice("D")
        self.grafo_teste_dfs.adiciona_vertice("E")
        self.grafo_teste_dfs.adiciona_vertice("F")
        self.grafo_teste_dfs.adiciona_aresta("a2", "A", "D")
        self.grafo_teste_dfs.adiciona_aresta("a1", "A", "B")
        self.grafo_teste_dfs.adiciona_aresta("a3", "B", "C")
        self.grafo_teste_dfs.adiciona_aresta("a7", "C", "E")
        self.grafo_teste_dfs.adiciona_aresta("a8", "E", "F")

        # grafo teste bfs D
        self.grafo_teste_bfs = MeuGrafo()
        self.grafo_teste_bfs.adiciona_vertice("A")
        self.grafo_teste_bfs.adiciona_vertice("B")
        self.grafo_teste_bfs.adiciona_vertice("C")
        self.grafo_teste_bfs.adiciona_vertice("D")
        self.grafo_teste_bfs.adiciona_vertice("E")
        self.grafo_teste_bfs.adiciona_vertice("F")
        self.grafo_teste_bfs.adiciona_aresta("a2", "A", "D")
        self.grafo_teste_bfs.adiciona_aresta("a4", "B", "D")
        self.grafo_teste_bfs.adiciona_aresta("a5", "D", "C")
        self.grafo_teste_bfs.adiciona_aresta("a6", "D", "E")
        self.grafo_teste_bfs.adiciona_aresta("a8", "E", "F")

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adiciona_aresta('a10', 'J', 'C'))
        a = Aresta("zxc", self.g_p.get_vertice("C"), self.g_p.get_vertice("Z"))
        self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(ArestaInvalidaError):
            self.assertTrue(self.g_p.adiciona_aresta(a))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', '', 'C'))
        with self.assertRaises(VerticeInvalidoError):
            self.assertTrue(self.g_p.adiciona_aresta('b1', 'A', 'C'))
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('')
        with self.assertRaises(NotImplementedError):
            self.g_p.adiciona_aresta('aa-bb')
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.adiciona_aresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaError):
            self.g_p.adiciona_aresta('a1', 'J', 'C')

    def test_eq(self):
        self.assertEqual(self.g_p, self.g_p2)
        self.assertNotEqual(self.g_p, self.g_p3)
        self.assertNotEqual(self.g_p, self.g_p_sem_paralelas)
        self.assertNotEqual(self.g_p, self.g_p4)

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         {'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z',
                          'M-Z'})
        self.assertEqual(self.g_d.vertices_nao_adjacentes(), {'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_d2.vertices_nao_adjacentes(), {'A-B', 'A-C', 'A-D', 'B-C', 'B-D', 'C-D'})
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), set())
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), set())

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p2.ha_laco())
        self.assertFalse(self.g_p3.ha_laco())
        self.assertFalse(self.g_p4.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_d.ha_laco())
        self.assertFalse(self.g_c.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
        self.assertFalse(self.g_c3.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)
        with self.assertRaises(VerticeInvalidoError):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)
        self.assertEqual(self.g_d2.grau('A'), 0)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)

        # Com laço. Lembrando que cada laço conta 2 vezes por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 5)
        self.assertEqual(self.g_l2.grau('B'), 4)
        self.assertEqual(self.g_l4.grau('D'), 2)

    def test_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(self.g_p.arestas_sobre_vertice('J'), {'a1'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('C'), {'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7'})
        self.assertEqual(self.g_p.arestas_sobre_vertice('M'), {'a7', 'a8'})
        self.assertEqual(self.g_l2.arestas_sobre_vertice('B'), {'a1', 'a2', 'a3'})
        self.assertEqual(self.g_d.arestas_sobre_vertice('C'), set())
        self.assertEqual(self.g_d.arestas_sobre_vertice('A'), {'asd'})
        with self.assertRaises(VerticeInvalidoError):
            self.g_p.arestas_sobre_vertice('A')

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertFalse((self.g_l4.eh_completo()))
        self.assertFalse((self.g_l5.eh_completo()))
        self.assertFalse((self.g_d.eh_completo()))
        self.assertFalse((self.g_d2.eh_completo()))

    def test_dfs(self):
        self.assertEqual(self.g_p.dfs("J"), self.g_p_dfs)
        self.assertEqual(self.grafo_teste.dfs("D"), self.grafo_teste_dfs)

    def test_bfs(self):
        self.assertEqual(self.g_p.bfs("J"), self.g_p_bfs)
        self.assertEqual(self.grafo_teste.bfs("D"), self.grafo_teste_bfs)

    def test_conexo(self):
        self.assertTrue(self.grafo_teste.conexo())
        self.assertTrue(self.g_p.conexo())
        self.assertTrue(self.g_c.conexo())
        self.assertTrue(self.g_c2.conexo())
        self.assertFalse(self.g_l1.conexo())
        self.assertFalse(self.g_l2.conexo())
        self.assertFalse(self.g_l3.conexo())
        self.assertFalse(self.g_d.conexo())

    def test_prim(self):
        self.assertEqual(self.g2.mst_prim(), self.g2_prim)
        self.assertEqual(self.g3.mst_prim(), self.g3_prim)
        self.assertEqual(self.g_c_pesos.mst_prim(), self.g_c_prim)

    def test_kruskall(self):
        self.assertEqual(self.grafo_teste.mst_kruskal("A"), self.grafo_teste_kruskall)
        self.assertEqual(self.g_p.mst_kruskal("J"), self.g_p_kruskall)
        self.assertEqual(self.g3.mst_kruskal("A"), self.g3_kruskall)
