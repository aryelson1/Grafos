from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
import copy
import operator

class MeuGrafo(GrafoListaAdjacencia):

    visited = list()
    linha = list()


    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        aux = list()
        vertices = list()
        for i in self.A:
            aux.append(self.A[i].getV1()+"-"+self.A[i].getV2())
            aux.append(self.A[i].getV2()+"-"+self.A[i].getV1())
        for i in self.N:
            for x in self.N:
                if i != x:
                    if str(i)+"-"+str(x) not in aux and str(x)+"-"+str(i) not in vertices:
                        vertices.append(str(i)+"-"+str(x))
        return vertices


    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        #FEITO POR ARYELSON GONÇALVES
        '''
        for i in self.A:
            if self.A[i].getV1() == self.A[i].getV2():
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        #FEITO POR ARYELSON GONÇALVES
        '''
        if V not in self.N:
            raise VerticeInvalidoException
        cont = 0
        for i in self.A:
            if self.A[i].getV1() == V or self.A[i].getV2() == V:
                if self.A[i].getV1() == self.A[i].getV2():
                    cont += 2
                else:
                    cont += 1
        return cont


    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        #FEITO POR ARYELSON GONÇALVES
        '''
        for i, v1 in enumerate(self.A):
            for x, v2 in enumerate(self.A):
                if x > i and ([self.A[v1].getV1() ,self.A[v1].getV2()] == [self.A[v2].getV2() ,self.A[v2].getV1()] or
                [self.A[v1].getV1() ,self.A[v1].getV2()] == [self.A[v2].getV1() ,self.A[v2].getV2()]):
                    return True
        return False

    def arestas_sobre_vertice(self, V=''):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice nãso exite no grafo
        #FEITO POR ARYELSON GONÇALVES
        '''
        if V not in self.N:
            raise VerticeInvalidoException
        arrestas = list()
        for i in self.A:
            if self.A[i].getV1() == V or self.A[i].getV2() == V:
                arrestas.append(self.A[i].getRotulo())
        return arrestas

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco() or self.vertices_nao_adjacentes():
            return False
        return True

    def dfs(self,V=''):
        linha =  list()
        visited = list()
        linha = self.dfs(visited,linha,V)
        return linha

    def dfs(self, V='' , aux=0 ):
        if V not in self.N:
            raise VerticeInvalidoException
        if V not in self.visited:
            arestas = self.arestas_sobre_vertice(V)
            self.visited.append(V)
            for i in arestas:
                if self.A[i].getV2() not in self.visited or self.A[i].getV1() not in self.visited:
                    if aux == 0:
                        self.linha.append(self.A[i].getV1())
                        self.linha.append(self.A[i].getRotulo())
                        self.linha.append(self.A[i].getV2())
                        aux = 1

                    else:
                        self.linha.append(self.A[i].getRotulo())
                        if self.A[i].getV2() in self.linha:
                            self.linha.append(self.A[i].getV1())
                        else:
                            self.linha.append(self.A[i].getV2())
                if V == self.A[i].getV1():
                    aux = 1
                    self.dfs2(self.A[i].getV2(), aux)
                else:
                    aux = 1
                    self.dfs2(self.A[i].getV1(), aux)

        return self.linha

    def dfs_1(self, visited,linha,V=''):
        if V not in self.N:
            raise VerticeInvalidoException
        if V not in visited:
            arestas = self.arestas_sobre_vertice(V)
            visited.append(V)
            for i in arestas:
                if self.A[i].getV2() not in visited or self.A[i].getV1() not in visited:
                    linha.append(self.A[i].getV1()+"-"+self.A[i].getV2())
                if V == self.A[i].getV1():
                    self.dfs_1(visited,linha,self.A[i].getV2())
                else:
                    self.dfs_1(visited,linha,self.A[i].getV1())

        return linha

    def bfs(self, V=''):
        if V not in self.N:
            raise VerticeInvalidoException
        visitados = dict()
        linha = list()
        for i in self.N:
            visitados[i] = False # {'J': FALSE, 'C':FALSE, 'E':FALSE, 'P':FALSE, 'M':FALSE ...}
        fila = []
        fila.append(V) # [V] No raiz
        visitados[V] = True # Digamos que V = J - {'J': True, 'C':FALSE, 'E':FALSE, 'P':FALSE, 'M':FALSE ...}
        while fila:
            s = fila.pop(0) # Pop remove o ultimo elemento da lista.
            g = self.arestas_sobre_vertice(s) #Digamos que V = 'J' - temos que g = ['a1']
            for i in g: # i é a chave de cada arresta encontrada na função arestas_sobre_vertice
                if self.A[i].getV1() != s: # a1(J-C), 1 J = getV1() e C = getV2()
                    a = self.A[i].getV1() # a = J
                else:
                    a = self.A[i].getV2() # a = C
                if visitados[a] == False:
                    fila.append(a)
                    linha.append(self.A[i].getV1() + "-" + self.A[i].getV2())
                    visitados[a] = True # {'J': True, 'C':True, 'E':FALSE, 'P':FALSE, 'M':FALSE ...}

        return linha

    def ha_ciclo(self, raiz = '', visitados = None, ciclo = None, arestas = None):

        if((visitados is None) and (ciclo is None) and (arestas is None) and (raiz == '')):
            raiz = self.N[0]
            visitados = ciclo = arestas = []
            for i in self.A:
                arestas.append(self.A[i].getV1()+"-"+self.A[i].getV2())
        visitados.append(raiz)
        if((len(visitados) > 1) and (visitados[0] == visitados[-1])):
            return ciclo

        for aresta in self.A:
            if(self.A[aresta].getV1() == raiz):
                for aux in self.A:
                    if (self.A[aux].getV1() == self.A[aresta].getV2()):
                        ciclo.append(aux)
                        break

                arestaAux = self.A[aresta].getV2()
                a = self.A[aresta].getV1() + "-" + self.A[aresta].getV2()
                if a in arestas:
                    arestas.remove(a)
                self.ha_ciclo(arestaAux,visitados,ciclo,arestas)

            elif (self.A[aresta].getV2() == raiz):
                for aux in self.A:

                    if (self.A[aux].getV2() == self.A[aresta].getV1()):
                        ciclo.append(aux)
                        break
                arestaAux = self.A[aresta].getV2()
                a = self.A[aresta].getV1()+"-"+self.A[aresta].getV2()
                if a in arestas:
                    arestas.remove(a)
                self.ha_ciclo(arestaAux, visitados, ciclo, arestas)

        for i in range(len(ciclo)):
            if(len(ciclo) > 1):
                if(ciclo[0] == ciclo[-1]):
                    return ciclo
                else:
                    ciclo.remove(ciclo[0])
            else:
                break
        return False

    def caminho(self, n):
        for vertice in self.N:
            caminho = self.dfs(vertice)
            if (len(caminho) == (n * 2 + 1)):
                return caminho
            elif (len(caminho) > (n * 2 + 1)):
                caminho = caminho[0:n * 2 + 1]
                return caminho
        return False

    def eh_conexo(self):
        arestas = list()
        for i in self.A:
            arestas.append(self.A[i].getV1()+"-"+self.A[i].getV2())

        vertices = self.N

        listaadj = []

        for vertice in vertices:

            if len(listaadj) < 1:
                listaadj.append(vertice)

            if vertice in listaadj:
                for aresta in arestas:
                    # Perguntamos se o vertice atual esta presente na aresta atual
                    if vertice in aresta:
                        if vertice == aresta[0] and aresta[2] not in listaadj:
                            listaadj.append(aresta[2])
                        elif vertice == aresta[2] and aresta[0] not in listaadj:
                            listaadj.append(aresta[0])
        if len(listaadj) == len(self.N):
            return True
        else:
            return False

    def retorna_graus(self):
        graus = list()
        for i in self.N:
            graus.append(self.grau(i))
        cont = list()
        for i,v1 in enumerate(graus):
            if v1 % 2 != 0:
                cont.append(graus[i])
        if len(cont) == 2 or len(cont) == 0:
            return cont
        else:
            return False


    def caminho_euleriano(self):
        caminho = list()
        if self.retorna_graus() == False or not self.eh_completo() and not self.eh_conexo():
            return "Não Possui Caminho Euleriano !!"
        v = self.retorna_graus()
        if len(v) == 2:
            v = self.N[v[0]]
        else:
            v = self.N[0]
        a = self.arestas_sobre_vertice(v)

        while a:
            for i in a:
                v1 = self.A[i].getV1()
                v2 = self.A[i].getV2()
                self.removeAresta(i)
                if self.eh_completo() and self.eh_conexo():
                    caminho.append(self.A[i].getV1())
                    caminho.append(self.A[i].getRotulo())
                    v = v2
                    break
                else:
                    self.adicionaAresta(i,v1,v2)
            a = self.arestas_sobre_vertice(v)

        return caminho

    def menorPeso(self, grafo_prim):
        if len(grafo_prim) == 0:
            return 0
        menorPeso = int(self.A[grafo_prim[0]].getPeso())
        aresta_menor = grafo_prim[0]
        for i in grafo_prim:
            if self.A[i].getPeso() < menorPeso:
                menorPeso = self.A[i].getPeso()
                aresta_menor = i
        return aresta_menor

    def primModificado(self, grafo):
        '''
        O algoritmo proposto é ligeiramente diferente do algoritmo de prim original. Este algoritmo de prim modificado
        identifica a aresta de peso mínimo do gráfico e torna seu único nó como um nó raiz. No prim original algoritmo,
        o nó raiz é selecionado aleatoriamente.
        '''
        clone_arestas = grafo
        caminhos = list()
        lista = self.N
        caminhoMin = list()
        b = list()
        for i in lista:
            aux = self.arestas_sobre_vertice(i)
            for x in aux:
                if x not in caminhoMin and x not in caminhos:
                    caminhos.append(x)
        menor = self.menorPeso(caminhos)
        caminhoMin.append(menor)
        b.append(clone_arestas.A[menor].getV1())
        b.append(clone_arestas.A[menor].getV2())
        clone_arestas.removeAresta(menor)
        while len(b) < len(self.N):
            caminhos = list()
            for i in lista:
                aux = self.arestas_sobre_vertice(i)
                for x in aux:
                    if x not in caminhoMin and x not in caminhos:
                        caminhos.append(x)
            while True:
                menor = self.menorPeso(caminhos)
                if menor == 0:
                    break
                if clone_arestas.A[menor].getV1() not in b and clone_arestas.A[menor].getV2() in b or clone_arestas.A[menor].getV1()  in b and clone_arestas.A[menor].getV2() not in b :
                    break
                caminhos.remove(menor)
            if menor == 0:
                break
            caminhoMin.append(menor)
            if clone_arestas.A[menor].getV1() in b:
                b.append(clone_arestas.A[menor].getV2())
            else:
                b.append(clone_arestas.A[menor].getV1())
            clone_arestas.removeAresta(menor)
        return caminhoMin



    def Kruskal(self,grafo):
        T = list()
        caminho = list()

        aux = grafo
        while len(caminho) != len(self.N)-1:
            arestas = list()
            for i in aux.A:
                arestas.append(i)
            menor = self.menorPeso(arestas)
            if menor == 0:
                break
            if aux.A[menor].getV1() in T and aux.A[menor].getV2() in T:
                pass
            elif aux.A[menor].getV1() not in T and aux.A[menor].getV2() not in T:
                T.append(aux.A[menor].getV1())
                T.append(aux.A[menor].getV2())
                caminho.append(menor)
            elif aux.A[menor].getV1() in T and aux.A[menor].getV2() not in T:
                T.append(aux.A[menor].getV2())
                caminho.append(menor)
            else:
                T.append(aux.A[menor].getV1())
                caminho.append(menor)
            aux.removeAresta(menor)

        return caminho

    def sorted_dic(self):
        ordenados = list()
        while len(ordenados) < len(self.A):
            menor = float("Inf")
            for i in self.A:
                if self.A[i].getPeso() < menor and i not in ordenados:
                    menor = self.A[i].getPeso()
                    aresta = i
            ordenados.append(aresta)
        return ordenados

    def ha_paralelas_sobre_vertice(self, v):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        lista = list()
        for i, v1 in enumerate(self.A):
            for x, v2 in enumerate(self.A):
                if self.A[v1].getV1() == v or self.A[v1].getV2() == v:
                    if x > i and (
                            [self.A[v1].getV1(), self.A[v1].getV2()] == [self.A[v2].getV2(), self.A[v2].getV1()] or
                            [self.A[v1].getV1(), self.A[v1].getV2()] == [self.A[v2].getV1(), self.A[v2].getV2()]):
                        lista.append(v2)
        return lista

    def gerarBuckets(self):
        buckets = list()
        while len(buckets) < len(self.A):
            menor = float("Inf")
            for i in self.A:
                if self.A[i].getPeso() < menor and i not in buckets:
                    menor = self.A[i].getPeso()
                    aresta = i
            buckets.append(aresta)
        return buckets

    def union(self, pais, x, y):
        a = self.find(pais, x)
        b = self.find(pais, y)
        pais[a] = b
        return pais

    def find(self, pais, x):
        while pais[x] != x:
            x = pais[x]
        return x

    def encontrarMenorAresta(self, buckets, pais):
        for i in buckets:
            if (self.find(pais, self.A[i].getV1()) != self.find(pais, self.A[i].getV2())):
                return i

    def KruskalModificado(self):
        buckets = self.gerarBuckets()
        T = []
        pais = {vertice: vertice for vertice in self.N}
        while (len(T) < len(self.N) - 1):
            menorAresta = self.encontrarMenorAresta(buckets, pais)
            pais = self.union(pais, self.A[menorAresta].getV1(), self.A[menorAresta].getV2())
            T.append(menorAresta)
        return T
