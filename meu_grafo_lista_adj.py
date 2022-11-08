from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        existente = []
        conj = set()

        for a in self.arestas:
            ar = f'{self.arestas[a].v1.rotulo}-{self.arestas[a].v2.rotulo}'
            existente.append(ar)

        for v1 in self.vertices:
            for v2 in self.vertices:
                if v1.rotulo != v2.rotulo:
                    par = f'{v1.rotulo}-{v2.rotulo}'
                    if par not in existente and par not in conj:
                        if par[::-1] not in existente and par[::-1] not in conj:
                            conj.add(par)

        return conj

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.arestas:
            if self.arestas[a].v1 == self.arestas[a].v2:
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
        else:
            g = 0
            for a in self.arestas:
                if self.arestas[a].v1.rotulo == V:
                    g += 1
                if self.arestas[a].v2.rotulo == V:
                    g += 1
            return g

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        existente = []
        for a in self.arestas:
            ar = f'{self.arestas[a].v1.rotulo}-{self.arestas[a].v2.rotulo}'
            existente.append(ar)

        for par in range(len(existente)):
            for i in range(len(existente)):
                if i != par:
                    if existente[par] == existente[i] or existente[par][::-1] == existente[i]:
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
        else:
            conj = set()
            for a in self.arestas:
                if self.arestas[a].v1.rotulo == V or self.arestas[a].v2.rotulo == V:
                    conj.add(a)
            return conj

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        for v in self.vertices:
            if not self.grau(v.rotulo) == (len(self.vertices) - 1):
                return False
        return True

    def dijkstra_drone(self, vi, vf, carga: int, carga_max: int, pontos_recarga: list()):
        pass

    def dfs(self, V=''):
        '''
        Retorna uma busca em profundidade.
        :param V: O rótudo do vértice de início da busca.
        :return: Uma árvore do grafo.
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError
        else:
            arvore_dfs = MeuGrafo()
            arvore_dfs.adiciona_vertice(V)
            self.dfs_rec(V, arvore_dfs)
        return arvore_dfs

    def dfs_rec(self, V, arvore_dfs):
        '''
        :param V: Vértice a ser analisado.
        :param arvore_dfs: Grafo que irá representar a árvore resultante da busca.
        '''
        asv = list(self.arestas_sobre_vertice(V))
        asv.sort()
        for a in asv:
            v1 = self.arestas[a].v1.rotulo
            v2 = self.arestas[a].v2.rotulo
            if v1 != v2:
                if v1 == V and arvore_dfs.existe_rotulo_vertice(v2) is False and a not in arvore_dfs.arestas:
                    arvore_dfs.adiciona_vertice(v2)
                    arvore_dfs.adiciona_aresta(a, v1, v2)
                    self.dfs_rec(v2, arvore_dfs)
                elif v2 == V and arvore_dfs.existe_rotulo_vertice(v1) is False and a not in arvore_dfs.arestas:
                    arvore_dfs.adiciona_vertice(v1)
                    arvore_dfs.adiciona_aresta(a, v2, v1)
                    self.dfs_rec(v1, arvore_dfs)

    def bfs(self, V=''):
        '''
        Retorna uma busca em largura.
        :param V: O rótudo do vértice de início da busca.
        :return: Uma árvore do grafo.
        '''
        if self.existe_rotulo_vertice(V) is False:
            raise VerticeInvalidoError
        arvore_bfs = MeuGrafo()
        arvore_bfs.adiciona_vertice(V)
        return self.bfs_rec(V, arvore_bfs)

    def bfs_rec(self, V, arvore_bfs):
        '''
        :param V: Vértice a ser analisado.
        :param arvore_dfs: Grafo que irá representar a árvore resultante da busca.
        '''

        if len(self.vertices) == len(arvore_bfs.vertices):
            return arvore_bfs

        for a in self.arestas:
            if self.arestas[a].v1.rotulo == V and self.arestas[a].v1.rotulo != self.arestas[a].v2.rotulo:
                aux = self.arestas[a].v1.rotulo
                prox = self.arestas[a].v2.rotulo

                if arvore_bfs.existe_rotulo_vertice(aux) and not arvore_bfs.existe_rotulo_vertice(prox):
                    arvore_bfs.adiciona_vertice(prox)
                    arvore_bfs.adiciona_aresta(self.arestas[a])
            elif self.arestas[a].v2.rotulo == V and self.arestas[a].v1.rotulo != self.arestas[a].v2.rotulo:
                aux = self.arestas[a].v2.rotulo
                prox = self.arestas[a].v1.rotulo

                if arvore_bfs.existe_rotulo_vertice(aux) and not arvore_bfs.existe_rotulo_vertice(prox):
                    arvore_bfs.adiciona_vertice(prox)
                    arvore_bfs.adiciona_aresta(self.arestas[a])

        self.bfs_rec(prox, arvore_bfs)

        return arvore_bfs

    def caminho(self, n):
        '''
        :param n: tamanho do caminho desejado.
        :return: uma lista com o caminho, se existir.
        '''
        caminho = []

        if n < 0 or n > len(list(self.arestas)):
            return False

        tam = 0
        for a in self.arestas:

            if tam == n:  # se o tamanho do caminho já foi obtido
                return caminho

            v1 = self.arestas[a].v1.rotulo
            v2 = self.arestas[a].v2.rotulo

            if not caminho:  # se a lista do caminho estiver vazia
                caminho.append(v1)  # recebe o primeiro vértice elemento da primeira aresta lida

            if v1 == caminho[-1]:  # se o vértice 1 for o último adicionado na lista
                r = v2
            elif v2 == caminho[-1]:  # se o vértice 2 for o último adicionado na lista
                r = v1

            grau = self.grau(r)
            if n > 2 and (
                    n - tam) > 1:  # se o tamanho do caminho for maior que 2 e a quantidade de arestas a serem adicionadas for maior que 1
                if grau > 2 and r not in caminho:
                    caminho.append(a)
                    caminho.append(r)
                    tam += 1
            else:
                if r not in caminho:
                    caminho.append(a)
                    caminho.append(r)
                    tam += 1
        return False

    def ha_ciclo(self):

        for a in self.arestas:
            retorno = list()
            ciclo = MeuGrafo()
            V = self.arestas[a].v1.rotulo
            ciclo.adiciona_vertice(V)

            self.ciclo_rec(retorno, V, ciclo)
            return retorno

    def ciclo_rec(self, retorno, V, ciclo):

        if len(retorno) > 0:
            return True

        if len(self.vertices) == len(ciclo.vertices):
            return False

        rotulo = self.arestas_sobre_vertice(V)
        rotulos = list(rotulo)
        rotulos.sort()

        for a in rotulos:
            if not ciclo.existe_rotulo_vertice(a):
                if V == self.arestas[a].v1.rotulo:
                    r = self.arestas[a].v2.rotulo
                else:
                    r = self.arestas[a].v1.rotulo

                if ciclo.existe_rotulo_vertice(r):
                    retorno.append(a)
                else:
                    ciclo.adiciona_vertice(r)
                    ciclo.adiciona_aresta(self.arestas[a])
                self.ciclo_rec(retorno, r, ciclo)
        return ciclo

    def caminho(self, n):
        '''
        Verifica a existencia de um caminho de cumprimento N.
        :param n: tamanho do caminho
        :return: se o caminho de tamanho N existir é retornada uma lista, caso contrário retorna False
        '''
        tam = 0
        V = self.vertices[0].rotulo
        caminho = [V]
        arv = self.dfs(V)
        for i in range(n):
            asv = arv.arestas_sobre_vertice(V)
            for a in asv:
                v1 = arv.arestas[a].v1.rotulo
                v2 = arv.arestas[a].v2.rotulo
                if (n - tam) > 1:
                    if v1 != v2:
                        if v1 == V and v2 not in caminho and len(arv.arestas_sobre_vertice(v2)) > 2:
                            caminho.append(a)
                            caminho.append(v2)
                            V = v2
                            tam += 1
                        elif v2 == V and v1 not in caminho and len(arv.arestas_sobre_vertice(v1)) > 2:
                            caminho.append(a)
                            caminho.append(v1)
                            V = v1
                            tam += 1
                else:
                    if v1 != v2:
                        if v1 == V and v2 not in caminho:
                            caminho.append(a)
                            caminho.append(v2)
                            V = v2
                            tam += 1
                        elif v2 == V and v1 not in caminho:
                            caminho.append(a)
                            caminho.append(v1)
                            V = v1
                            tam += 1
        return caminho

    def conexo(self):
        '''
        Verifica se o grafo é conexo
        :return: Retorna um valor booleano
        '''

        vertices_self = len(self.vertices)
        arvore = self.dfs(str(self.vertices[0]))
        vertices_dfs = len(arvore.vertices)

        if vertices_self == vertices_dfs:
            return True
        else:
            return False