from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        pass

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        pass


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        pass

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
                        if self.M[i][j][x].getV1() == V:
                            arrestas.append(self.M[i][j][x].getRotulo())
        return arrestas


    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        pass

    def warshall(self):
        '''
        Provê a matriz de alcançabilidade de Warshall do grafo
        :return: Uma lista de listas que representa a matriz de alcançabilidade de Warshall associada ao grafo
        '''
        G2 = self.M
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if len(self.M[j][i]) >= 1:
                    G2[j][i] = 1
                else:
                    G2[j][i] = 0


        for i in range(len(self.M)):
            for j in range(len(self.M)):
                if G2[j][i] == 1 :
                    for k in range(len(self.M)):
                        G2[j][k] = max(G2[j][k],G2[i][k])

        grafo_str = '  '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(G2)):
            grafo_str += self.N[l] + ' '
            for c in range(len(G2)):
                if bool(G2[l][c]):
                    grafo_str += '1' + ' '
                else:
                    grafo_str += '0' + ' '
            grafo_str += '\n'

        return grafo_str



    def menorDistancia(self, tabela):
        menor = float('Inf')
        verticeMin = 0

        for i in self.N:
            if tabela[i]['beta'] < menor and tabela[i]['pi'] == None:
                menor = tabela[i]['beta']
                verticeMin = i
        return verticeMin

  

    def djarkstra(self, saida, chegada): #cargaIni, cargaMax, pontosDeRecarga):
        
        tabela = dict()
        for vertice in self.N:
            '''Usando float ('inf') e float ('- inf'):
            Como infinito pode ser positivo e negativo, 
            eles podem ser representados como float ('inf') e float ('- inf') respectivamente.'''
            tabela[vertice] = {'carga': 0,'beta': float("Inf"), 'pi': None, 'pred': None}
        tabela[saida]['beta'] = 0
        tabela[saida]['pi'] = 1
        tabela[saida]['pred'] = 0
        #tabela[saida]['carga'] = cargaIni
        w = saida
        while w != chegada:
            arrestas = self.arestas_sobre_vertice(w)

            for arresta in arrestas:
                for i in range(len(self.M)):
                    for j in range(len(self.M)):
                        if arresta in self.M[i][j]:
                            peso = self.M[i][j][arresta].getPeso()
                            aux = self.M[i][j][arresta].getV2()
                            break
                if tabela[aux]['beta'] > tabela[w]['beta'] + peso:# and tabela[w]['carga'] - peso >= 0:
                    tabela[aux]['beta'] = tabela[w]['beta'] + peso
                    tabela[aux]['pred'] = w
                    '''
                    if aux in pontosDeRecarga:
                        tabela[aux]['carga'] = cargaMax
                    else:
                        tabela[aux]['carga'] = tabela[w]['carga'] - peso
                    '''
            r =  self.menorDistancia(tabela)
            if r == 0:
                break
            tabela[r]['pi'] = 1
            w = r
        a = chegada
        if tabela[chegada]['pred'] == None:
            return "Não Existe Caminho Para o Vertice " + str(chegada) + " !"
        caminho = list()
        while a != saida:
            caminho.insert(0,tabela[a]['pred'])
            a = tabela[a]['pred']
        caminho.append(chegada)
        return caminho


    def raizes(self):
        vertices_visitados = set()
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                for x in self.M[i][j]:
                    if len(self.M[i][j]) > 0 and self.M[i][j] != '-':
                            vertices_visitados.add(self.M[i][j][x].getV2())
        v_raizes = self.N.copy()
        for i in vertices_visitados:
            v_raizes.remove(i)
        return v_raizes

    def ordenacao_topologica(self):
        ordem = list()
        parada = self.N.copy()
        while len(ordem) != len(parada):
            v_raizes = self.raizes()
            for i in v_raizes:
                aux = self.arestas_sobre_vertice(i)
                self.N.remove(i)
                for j in aux:

                    self.removeAresta(j)
                ordem.append(i)

        return ordem


    def removeAresta(self, aresta):
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                for x in self.M[i][j]:
                    if len(self.M[i][j]) > 0 and self.M[i][j] != '-':
                        if self.M[i][j][x].getRotulo() == aresta:
                            self.M[i][j].pop(aresta)
                            return 0


        '''grafo_str = '  '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(G2)):
            grafo_str += self.N[l] + ' '
            for c in range(len(G2)):
                if bool(G2[l][c]):
                    grafo_str += '1' + ' '
                else:
                    grafo_str += '0' + ' '
            grafo_str += '\n'

        return grafo_str'''



