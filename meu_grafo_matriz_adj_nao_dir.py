from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        vertices = {}
        vna = set() #armazena arestas não existentes
        va = set() #armazena arestas existentes
        for v in self.vertices:
            vertices[str(v)] = self.vertices.index(v)

        for v in range(len(vertices)):
            for h in range(len(vertices)):
                par = f'{list(vertices.keys())[list(vertices.values()).index(v)]}-{list(vertices.keys())[list(vertices.values()).index(h)]}'
                if len(self.matriz[v][h]) > 0:
                    if par not in va and par[::-1] not in va:
                        va.add(par)
                elif v != h and par not in vna and par[::-1] not in vna:
                    vna.add(par)
        return vna

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for j in range(len(self.vertices)):
            if len(self.matriz[j][j]) > 0:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        g = 0

        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if str(self.vertices[i]) == V:
                    if i == j:
                        g += 2*len(self.matriz[i][j])
                    else:
                        g += len(self.matriz[i][j])
        return g


    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for j in range(len(self.vertices)):
            for i in range(len(self.vertices)):
                if len(self.matriz[j][i]) == 2:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        asv = set()
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if str(self.vertices[i]) == V or str(self.vertices[j]) == V:
                    for a in self.matriz[i][j]:
                        asv.add(a)
        return asv

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        for v in self.vertices:
            if self.grau(str(v)) != (len(self.vertices)-1):
                return False
        return True


    def minimum_spanning_tree_prim(self):
        '''
        :return: Mínima árvore geradora do grafo pelo algoritmo modificado de Prim.
        '''

        # loop de arestas para pegar a de menor peso, adicionar a arvore e indicar o último vértice visitado
        # já adiciona uma aresta e dois vértices a arvore, os demais vertices permanecem não visitados

        # loop de vértices
        # loop de arestas sob vertice
        # verificar se a aresta existe e o vertice adjascente existem

        pass

    def minimum_spanning_tree_kruskal(self, V):
        '''
        :return: Mínima árvore geradora do grafo pelo algoritmo modificado de Kruskal.
        :param V: Vértice de início.
        '''

        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError

        pass
