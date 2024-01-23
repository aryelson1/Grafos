from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        aux = list()
        vertices = list()
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                for x in self.M[i][j]:
                    if len(self.M[i][j]) > 0 and self.M[i][j] != '-':
                        aux.append(self.M[i][j][x].getV1() + "-" + self.M[i][j][x].getV2())
                        aux.append(self.M[i][j][x].getV2() + "-" + self.M[i][j][x].getV1())
        for i in self.N:
            for x in self.N:
                if i != x:
                    if str(i) + "-" + str(x) not in aux and str(x) + "-" + str(i) not in vertices:
                        vertices.append(str(i) + "-" + str(x))
        return vertices

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in range(len(self.M)):
            if len(self.M[i][i]) > 0:
                return True
        return False


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException
        cont = 0
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                for x in self.M[i][j]:
                    if len(self.M[i][j]) > 0 and self.M[i][j] != '-':
                        if self.M[i][j][x].getV1() == V or self.M[i][j][x].getV2() == V:
                            if self.M[i][j][x].getV1() == self.M[i][j][x].getV2():
                                cont += 2
                            else:
                                cont += 1
        return cont

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                for x,v1 in enumerate(self.M[i][j]):
                    for z, v2 in enumerate(self.M[i][j]):
                        if x > z and ([self.M[i][j][v1].getV1(), self.M[i][j][v1].getV2()] == [self.M[i][j][v2].getV2(), self.M[i][j][v2].getV1()] or
                                      [self.M[i][j][v1].getV1(), self.M[i][j][v1].getV2()] == [self.M[i][j][v2].getV1(), self.M[i][j][v2].getV2()]):
                            return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException
        arrestas = list()
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                for x in self.M[i][j]:
                    if len(self.M[i][j]) > 0 and self.M[i][j] != '-':
                        if self.M[i][j][x].getV1() == V or self.M[i][j][x].getV2() == V:
                            arrestas.append(self.M[i][j][x].getRotulo())
        return arrestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco() or self.vertices_nao_adjacentes():
            return False
        return True