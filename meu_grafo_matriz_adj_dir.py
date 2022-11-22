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
        warshallM = []
        for i in range(len(self.vertices)):
            aux = []
            for j in range(len(self.vertices)):
                if len(self.matriz[i][j]) > 0:
                    aux.append(1)
                else:
                    aux.append(0)
            warshallM.append(aux)

        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if warshallM[j][i] == 1:
                    for k in range(len(self.vertices)):
                        warshallM[j][k] = max(warshallM[j][k], warshallM[i][k])
        return warshallM

    def dijkstra(self, vi, vf):
        '''
        Provê o menor caminho entre dois vértices no grafo.
        :param vi: Vértice inicial
        :param vf: Vértice final
        :return: Lista contendo o menor caminho entre os dois vértices
        :raises: VerticeInvalidoException se algum dos vértices não existe no grafo
        '''
        if vi == vf:
            return "Não é possível fazer Dijkstra de um vértice para ele mesmo."
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

        return self.aux_dijkstra(vi, w, vf, pred, beta, visitados)

    def aux_dijkstra(self, vi,  w, vf, pred, beta, visitados):

        for asv in self.arestas_sobre_vertice(w):
            for v in range(len(self.vertices)):
                for h in range(len(self.vertices)):
                    if v != h:
                        for a in self.matriz[v][h]:
                            if a == asv:
                                if self.vertices[v].rotulo == w and visitados[self.vertices[h].rotulo] == 0:
                                    v2 = self.vertices[h].rotulo
                                    calc = beta[w] + self.matriz[v][h][a].peso
                                    if beta[v2] > calc:
                                        beta[v2] = calc
                                        pred[v2] = w
        not_visted_beta = {}
        for vis in visitados:
            if vis != vi:
                if visitados[vis] == 0:
                    not_visted_beta[vis] = beta[vis]

        menor = min(not_visted_beta, key=not_visted_beta.get)
        #equal = len(list(set(list(beta.values())))) == 1
        #if equal:
        #    return "Não há caminho entre os vértices."
        if visitados[menor] == 0:
            visitados[menor] = 1
            w = menor
            if w == vf:
                if pred[w] == 0:
                    return "Não há caminho entre os vértices."
                caminho = []
                atual = w
                for i in range(len(pred)):
                    caminho.append(atual)
                    if pred[atual] == 0:
                        return caminho[::-1]
                    atual = pred[atual]
            return self.aux_dijkstra(vi, w, vf, pred, beta, visitados)