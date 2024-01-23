import copy

class VerticeInvalidoException(Exception):
    pass


class ArestaInvalidaException(Exception):
    pass


class MatrizInvalidaException(Exception):
    pass


class Grafo:
    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'
    __maior_vertice = 0

    def __init__(self, N=None, M=None):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        '''

        if N == None:
            N = list()
        if M == None:
            M = list()

        for v in N:
            if not (Grafo.vertice_valido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = N

        if M == []:
            for k in range(len(N)):
                M.append(list())
                for l in range(len(N)):
                    M[k].append(0)

        if len(M) != len(N):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(N):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(N)):
            for j in range(len(N)):
                aresta = N[i] + Grafo.SEPARADOR_ARESTA + N[j]
                if not (self.aresta_valida(aresta)):
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

        self.M = M

    def aresta_valida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        if not (self.existe_vertice(aresta[:i_traco])) or not (self.existe_vertice(aresta[i_traco + 1:])):
            return False

        return True

    @classmethod
    def vertice_valido(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existe_vertice(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.vertice_valido(vertice) and self.N.count(vertice) > 0

    def primeiro_vertice_aresta(self, a: str):
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def segundo_vertice_aresta(self, a: str):
        return a[a.index(Grafo.SEPARADOR_ARESTA) + 1:]

    def indice_primeiro_vertice_aresta(self, a: str):
        return self.N.index(self.primeiro_vertice_aresta(a))

    def indice_segundo_vertice_aresta(self, a: str):
        return self.N.index(self.segundo_vertice_aresta(a))

    def existe_aresta(self, a: str):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.aresta_valida(self, a):
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if self.M[self.indice_primeiro_vertice_aresta(a)][self.indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adiciona_vertice(self, v):
        if self.vertice_valido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v)
            self.M.append([])
            for k in range(len(self.N)):
                if k != len(self.N) - 1:
                    self.M[k].append(0)
                self.M[self.N.index(v)].append(0)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adiciona_aresta(self, a):
        if self.aresta_valida(a):
            self.M[self.indice_primeiro_vertice_aresta(a)][self.indice_segundo_vertice_aresta(a)] += 1
        else:
            raise ArestaInvalidaException('A aresta ' + self.N[a] + ' é inválida')

    def ha_laco(self):
        for i in range(len(self.N)):
            if self.M[i][i] != 0:
                return True
        return False

    def vertices_nao_adjacentes(self):
        vna = list()
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if self.M[i][j] == 0:
                    vna.append(self.N[i] + self.SEPARADOR_ARESTA + self.N[j])
        return vna

    def grau(self, V=""):
        grau = 0
        if self.vertice_valido(V):
            index_V = self.N.index(V)
            for i in range(len(self.N)):
                if self.M[index_V][i] != 0:  # linha
                    grau += self.M[index_V][i]
                if self.M[i][index_V] != 0 and i != index_V:  # coluna
                    grau += self.M[i][index_V]
        else:
            raise VerticeInvalidoException('O vértice ' + V + ' é inválido')
        return grau

    def ha_paralelas(self):
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if self.M[i][j] > 1:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        arestas = list()
        if self.vertice_valido(V):
            index_V = self.N.index(V)
            for i in range(len(self.N)):
                if self.M[index_V][i] != 0:  # linha
                    for k in range(self.M[index_V][i]):  # Se houver arestas paralelas
                        arestas.append(self.N[index_V] + '-' + self.N[i])
                if self.M[i][index_V] != 0 and i != index_V:  # coluna
                    for k in range(self.M[i][index_V]):  # Se houver arestas paralelas
                        arestas.append(self.N[i] + '-' + self.N[index_V])
        else:
            raise VerticeInvalidoException('O vértice ' + V + ' é inválido')
        return arestas

    def eh_completo(self):
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if self.M[i][j] == 0 and i != j:  # excluindo a diagonal principal
                    return False
        return True

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' ' * (self.__maior_vertice)

        grafo_str = espaco + ' '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(self.M)):
            grafo_str += self.N[l] + ' '
            for c in range(len(self.M)):
                grafo_str += str(self.M[l][c]) + ' '
            grafo_str += '\n'

        return grafo_str

    def warshall(self):
        copiaMatriz = copy.deepcopy(self.M)
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if copiaMatriz[i][j] > 1:
                    copiaMatriz[i][j] = 1
        for i in range(len(self.N)):
            for j in range(len(self.N)):
                if copiaMatriz[j][i] == 1:
                    for k in range(len(self.N)):
                        copiaMatriz[j][k] = max(copiaMatriz[j][k], copiaMatriz[i][k])
        return copiaMatriz

    def menorDistancia(self, table, fila):
        minDis = float('Inf')
        verticeMin = fila[0]

        for vertice in table.keys():
            if (table[vertice]['beta'] < minDis and vertice in fila):
                minDis = table[vertice]['beta']
                verticeMin = vertice
        return verticeMin

    def caminhoDrone(self, raiz, dest, carga, cargaMax, pontosDeRecarga):
        ## Criando tabela para usar no algoritmo de djarkstra
        table = dict()
        for vertice in self.N:
            table[vertice] = {
                'carga': None,
                'beta': float("Inf"),
                'pi': None
            }
        table[raiz]['beta'] = 0
        table[raiz]['carga'] = carga

        vertices = self.N[:]

        while vertices:
            vertMin = self.menorDistancia(table, vertices)

            minINdex = self.N.index(vertMin)

            vertices.remove(vertMin)

            for verticeIndex in range(len(self.N)):
                verticeCorrente = self.N[verticeIndex]

                conx = self.M[minINdex][verticeIndex]

                if (conx and verticeCorrente in vertices):
                    if table[vertMin]['carga'] and conx + table[vertMin]['beta'] < table[verticeCorrente]['beta']:
                        table[verticeCorrente]['carga'] = cargaMax if verticeCorrente in pontosDeRecarga else \
                        table[vertMin]['carga'] - 1
                        table[verticeCorrente]['beta'] = table[vertMin]['beta'] + conx
                        table[verticeCorrente]['pi'] = vertMin

        if table[dest]['carga'] is None:
            return []
        res = list()
        while (dest != None):
            res.append(dest)
            dest = table[dest]['pi']

        return res[::-1]