import unittest
from meu_grafo import *
#from meu_grafo_matriz_adjacencia_nao_dir import *
#from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):

        #Grafo Exemplo Prim e Kruskal
        self.grafo_prim = MeuGrafo(['A', 'B', 'C', 'D', 'E', 'F'])
        self.grafo_prim.adicionaAresta('1', 'A', 'B', 1100)
        self.grafo_prim.adicionaAresta('2', 'A', 'F', 1200)
        self.grafo_prim.adicionaAresta('3', 'A', 'C', 1800)
        self.grafo_prim.adicionaAresta('4', 'B', 'C', 900)
        self.grafo_prim.adicionaAresta('5', 'B', 'D', 800)
        self.grafo_prim.adicionaAresta('6', 'B', 'E', 750)
        self.grafo_prim.adicionaAresta('7', 'A', 'D', 2000)
        self.grafo_prim.adicionaAresta('8', 'C', 'D', 700)
        self.grafo_prim.adicionaAresta('9', 'C', 'F', 850)
        self.grafo_prim.adicionaAresta('10', 'D', 'E', 1100)
        self.grafo_prim.adicionaAresta('11', 'E', 'F', 500)
        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C',2)
        self.g_p.adicionaAresta('a2', 'C', 'E',4)
        self.g_p.adicionaAresta('a3', 'C', 'E',1)
        self.g_p.adicionaAresta('a4', 'P', 'C',2)
        self.g_p.adicionaAresta('a5', 'P', 'C',6)
        self.g_p.adicionaAresta('a6', 'T', 'C',7)
        self.g_p.adicionaAresta('a7', 'M', 'C',8)
        self.g_p.adicionaAresta('a8', 'M', 'T',9)
        self.g_p.adicionaAresta('a9', 'T', 'Z',10)


        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C',1)
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E',6)
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C',2)
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C',1)
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C',8)
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T',3)
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z',1)


        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1','J','C',1)
        self.g_c.adicionaAresta('a2', 'J', 'E',10)
        self.g_c.adicionaAresta('a3', 'J', 'P',44)
        self.g_c.adicionaAresta('a4', 'E', 'C',109)
        self.g_c.adicionaAresta('a5', 'P', 'C',184)
        self.g_c.adicionaAresta('a6', 'P', 'E',199)

        # Grafos completos 2
        self.g_c2 = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c2.adicionaAresta('a1', 'J', 'C', 1399)
        self.g_c2.adicionaAresta('a2', 'J', 'E', 10)
        self.g_c2.adicionaAresta('a3', 'J', 'P', 44)
        self.g_c2.adicionaAresta('a4', 'E', 'C', 109)
        self.g_c2.adicionaAresta('a5', 'P', 'C', 184)
        self.g_c2.adicionaAresta('a6', 'P', 'E', 199)

        self.g_c3 = MeuGrafo(['Nina', 'Maria'])
        self.g_c3.adicionaAresta('amiga', 'Nina', 'Maria')



        # Grafos com laco
        self.g_l1 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l1.adicionaAresta('a1', 'A', 'A')
        self.g_l1.adicionaAresta('a2', 'A', 'B')
        self.g_l1.adicionaAresta('a3', 'A', 'A')

        self.g_l2 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l2.adicionaAresta('a1', 'A', 'B')
        self.g_l2.adicionaAresta('a2', 'B', 'B')
        self.g_l2.adicionaAresta('a3', 'B', 'A')

        self.g_l3 = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_l3.adicionaAresta('a1', 'C', 'A')
        self.g_l3.adicionaAresta('a2', 'C', 'C')
        self.g_l3.adicionaAresta('a3', 'D', 'D')
        self.g_l3.adicionaAresta('a4', 'D', 'D')

        self.g_l4 = MeuGrafo(['D'])
        self.g_l4.adicionaAresta('a1', 'D', 'D')

        self.g_l5 = MeuGrafo(['C', 'D'])
        self.g_l5.adicionaAresta('a1', 'D', 'C')
        self.g_l5.adicionaAresta('a2', 'C', 'C')

        # Grafos desconexos
        self.g_d = MeuGrafo(['A', 'B', 'C', 'D'])
        self.g_d.adicionaAresta('asd', 'A', 'B')

    def test_adiciona_aresta(self):
        self.assertTrue(self.g_p.adicionaAresta('a10', 'J', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', '', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.assertTrue(self.g_p.adicionaAresta('b1', 'A', 'C'))
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('aa-bb')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('x', 'J', 'V')
        with self.assertRaises(ArestaInvalidaException):
            self.g_p.adicionaAresta('a1', 'J', 'C')

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(), ['J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-Z', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-M', 'P-T', 'P-Z', 'M-Z'])
        self.assertEqual(self.g_c.vertices_nao_adjacentes(), [])
        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), [])

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertFalse(self.g_c2.ha_laco())
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
        with self.assertRaises(VerticeInvalidoException):
            self.assertEqual(self.g_p.grau('G'), 5)

        self.assertEqual(self.g_d.grau('A'), 1)
        self.assertEqual(self.g_d.grau('C'), 0)
        self.assertNotEqual(self.g_d.grau('D'), 2)

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
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), set(['a1']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), set(['a7', 'a8']))
        self.assertEqual(set(self.g_l2.arestas_sobre_vertice('B')), set(['a1', 'a2', 'a3']))
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('C')), set())
        self.assertEqual(set(self.g_d.arestas_sobre_vertice('A')), set(['asd']))
        with self.assertRaises(VerticeInvalidoException):
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

    def test_dfs(self):
        self.assertEqual(set(self.g_c3.dfs("Nina")),set(['Nina-Maria']))
        self.assertEqual(set(self.g_p.dfs("C")), set(['J-C', 'C-E', 'P-C', 'T-C', 'M-T', 'T-Z']))
        self.assertEqual(set(self.g_p.dfs("Z")), set(['C-E', 'J-C', 'P-C', 'T-C', 'M-C', 'T-Z']))
        self.assertEqual(set(self.g_p_sem_paralelas.dfs("J")),set(['J-C','C-E','P-C','T-C','M-T','T-Z']))
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.dfs('A')

    def test_bfs(self):
        self.assertEqual(set(self.g_p.bfs("C")), set(['J-C', 'C-E', 'P-C', 'T-C', 'M-C', 'T-Z']))
        self.assertEqual(set(self.g_c3.bfs("Nina")), set(['Nina-Maria']))
        self.assertEqual(set(self.g_p.bfs("Z")), set(['T-Z', 'T-C', 'M-T', 'J-C', 'C-E', 'P-C']))
        self.assertEqual(set(self.g_p_sem_paralelas.bfs("J")), set(['T-Z','T-C','M-C','C-E','P-C','J-C']))
        with self.assertRaises(VerticeInvalidoException):
            self.g_p.bfs('A')


    def test_KruskalModificado(self):
        self.assertEqual(self.g_p.KruskalModificado(),['a3', 'a1', 'a4', 'a6', 'a7', 'a9'])
        self.assertEqual(self.g_p_sem_paralelas.KruskalModificado(), ['a1', 'a4', 'a7', 'a3', 'a6', 'a2'])
        self.assertEqual(self.g_c.KruskalModificado(), ['a1', 'a2', 'a3'])
        self.assertEqual(self.g_c2.KruskalModificado(), ['a2', 'a3', 'a4'])
        self.assertEqual(self.g_c3.KruskalModificado(), ['amiga'])
        self.assertEqual(self.grafo_prim.KruskalModificado(), ['11', '8', '6', '5', '1'])


    def test_PrimModificado(self):
        self.assertEqual(self.g_p.primModificado(self.g_p),['a3', 'a1', 'a4', 'a6', 'a7', 'a9'])
        self.assertEqual(self.g_p_sem_paralelas.primModificado(self.g_p_sem_paralelas), ['a1', 'a4', 'a7', 'a3', 'a6', 'a2'])
        self.assertEqual(self.g_c.primModificado(self.g_c), ['a1', 'a2', 'a3'])
        self.assertEqual(self.g_c2.primModificado(self.g_c2), ['a2', 'a3', 'a4'])
        self.assertEqual(self.g_c3.primModificado(self.g_c3), ['amiga'])
        self.assertEqual(self.grafo_prim.primModificado(self.grafo_prim), ['11', '6', '5', '8', '1'])


