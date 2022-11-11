from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_errors import *

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        vna = set()  # armazena arestas não existentes
        for v in range(len(self.vertices)):
            for h in range(len(self.vertices)):
                par = f'{self.vertices[v]}-{self.vertices[h]}'
                if v != h and par not in vna and len(self.matriz[v][h]) < 1:
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
                if str(self.vertices[i]) == V or str(self.vertices[j]) == V:
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
            if self.grau(str(v)) != (len(self.vertices) - 1):
                return False
        return True

    def warshall(self):
        '''
        Provê a matriz de alcançabilidade de Warshall do grafo
        :return: Uma lista de listas que representa a matriz de alcançabilidade de Warshall associada ao grafo
        '''
        pass

    def dijkstra(self, vi, vf):
        '''
        Provê o menor caminho entre dois vértices no grafo.
        :param vi: Vértice inicial
        :param vf: Vértice final
        :return: Lista contendo o menor caminho entre os dois vértices
        :raises: VerticeInvalidoException se algum dos vértices não existe no grafo
        '''
        if not self.existe_rotulo_vertice(vi) or not self.existe_rotulo_vertice(vf):
            raise VerticeInvalidoError

        pred = {} #predecessor do vértice
        visitados = {}
        beta = {}  #tamanho do caminho até o vértice
        for v in self.vertices:
            if v.rotulo == vi:
                visitados[v.rotulo] = 1
                beta[v.rotulo] = 0
            else:
                visitados[v.rotulo] = 0
                beta[v.rotulo] = float('inf')
            pred[v.rotulo] = 0
        w = vi
        for v in range(len(self.vertices)):
            for h in range(len(self.vertices)):
                if (len(self.matriz[v][h])) > 0 and self.vertices[v] == w: #percorrendo cada aresta existente
                    for a in range(len(self.matriz[v][h])):
                        v2 = self.matriz[v][h][a].v2.rotulo
                        calc = v2

        return print(beta)
