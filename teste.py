#from meu_grafo import MeuGrafo
from meu_grafo_matriz_adj_dir import MeuGrafo
#from meu_grafo_matriz_adjacencia_nao_dir import MeuGrafo

p = MeuGrafo(['K', 'J', 'G', 'H', 'F', 'B', 'C', 'D', 'E', 'A', 'I'])
p.adicionaAresta('5','K','J')
p.adicionaAresta('6','J','G')
p.adicionaAresta('9','G','H')
p.adicionaAresta('10','H','F')
p.adicionaAresta('11','F','B')
p.adicionaAresta('13','B','C')
p.adicionaAresta('14','C','D')
p.adicionaAresta('15','D','E')
p.adicionaAresta('1','B','A')
p.adicionaAresta('8','G','I')

#print(p.dfs2("K"))


grafo_djarkstra_1 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
grafo_djarkstra_1.adicionaAresta('a1','J','C',11)
grafo_djarkstra_1.adicionaAresta('a2','C','E',3)
grafo_djarkstra_1.adicionaAresta('a3','E','C',2)
grafo_djarkstra_1.adicionaAresta('a4','C','P',5)
grafo_djarkstra_1.adicionaAresta('a5','P','C',3)
grafo_djarkstra_1.adicionaAresta('a6','C','M',6)
grafo_djarkstra_1.adicionaAresta('a7','C','T',7)
grafo_djarkstra_1.adicionaAresta('a8','M','T',8)
grafo_djarkstra_1.adicionaAresta('a9','T','Z',9)
grafo_djarkstra_1.adicionaAresta('a10','Z','C',10)

#print(grafo_djarkstra_1.djarkstra('T','Z',40,40,['C','T','Z']))
print(grafo_djarkstra_1.djarkstra('J','Z'))
'''
#print(grafo_djarkstra_1.primModificado(grafo_djarkstra_1))#['a3', 'a5', 'a6', 'a7', 'a9', 'a1']
#print(grafo_djarkstra_1.Kruskal(grafo_djarkstra_1))#['a3', 'a5', 'a6', 'a7', 'a9', 'a1']
#print(grafo_djarkstra_1.ha_paralelas_sobre_vertice('C'))

#['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a10', 'a2', 'a3']


grafo_djarkstra_2 = MeuGrafo(["A","B","C","D"])
grafo_djarkstra_2.adicionaAresta('1', 'A', 'A',2)
grafo_djarkstra_2.adicionaAresta('2', 'A', 'C',1)
grafo_djarkstra_2.adicionaAresta('3', 'C', 'B',4)
grafo_djarkstra_2.adicionaAresta('4', 'B', 'B',7)
grafo_djarkstra_2.adicionaAresta('5', 'C', 'D',9)

grafo_djarkstra_3 = MeuGrafo(['A','B','C','D','E'])
grafo_djarkstra_3.adicionaAresta('1', 'A', 'B',1)
grafo_djarkstra_3.adicionaAresta('2', 'A', 'C',2)
grafo_djarkstra_3.adicionaAresta('3', 'C', 'B',1)
grafo_djarkstra_3.adicionaAresta('4', 'B', 'C',1)
grafo_djarkstra_3.adicionaAresta('5', 'C', 'D',1)
grafo_djarkstra_3.adicionaAresta('6', 'D', 'E',4)
print(grafo_djarkstra_3.warshall())
#print(grafo_djarkstra_3.arestas_sobre_vertice('A')
print(grafo_djarkstra_1.djarkstra("J",'Z',3,4,['C','M','Z','E']))
print(grafo_djarkstra_2.djarkstra('A', 'D', 1, 12, ['C']))
print(grafo_djarkstra_3.djarkstra('A', 'E', 3, 4, ['D']))

grafo_prim = MeuGrafo(['A','B', 'C','D','E','F'])
grafo_prim.adicionaAresta('1', 'A', 'B',1100)
grafo_prim.adicionaAresta('2', 'A', 'F',1200)
grafo_prim.adicionaAresta('3', 'A', 'C',1800)
grafo_prim.adicionaAresta('4', 'B', 'C',900)
grafo_prim.adicionaAresta('5', 'B', 'D',800)
grafo_prim.adicionaAresta('6', 'B', 'E',750)
grafo_prim.adicionaAresta('7', 'A', 'D',2000)
grafo_prim.adicionaAresta('8', 'C', 'D',700)
grafo_prim.adicionaAresta('9', 'C', 'F',850)
grafo_prim.adicionaAresta('10', 'D', 'E',1100)
grafo_prim.adicionaAresta('11', 'E', 'F',500)

#print(grafo_prim.primModificado(grafo_prim))#['11', '6', '5', '8', '1']

grafo_prim = MeuGrafo(['A','B', 'C','D','E','F'])
grafo_prim.adicionaAresta('1', 'A', 'B',1100)
grafo_prim.adicionaAresta('2', 'A', 'F',1200)
grafo_prim.adicionaAresta('3', 'A', 'C',1800)
grafo_prim.adicionaAresta('4', 'B', 'C',900)
grafo_prim.adicionaAresta('5', 'B', 'D',800)
grafo_prim.adicionaAresta('6', 'B', 'E',750)
grafo_prim.adicionaAresta('7', 'A', 'D',2000)
grafo_prim.adicionaAresta('8', 'C', 'D',700)
grafo_prim.adicionaAresta('9', 'C', 'F',850)
grafo_prim.adicionaAresta('10', 'D', 'E',1100)
grafo_prim.adicionaAresta('11', 'E', 'F',500)
#print(grafo_prim.KruskalModificado())#['11', '8', '6', '5', '1']



grafo_prim_2 = MeuGrafo(['A','B', 'C','D','E','F','G','H'])
grafo_prim_2.adicionaAresta('a1','A','B',9)
grafo_prim_2.adicionaAresta('a2','A','G',4)
grafo_prim_2.adicionaAresta('a3','B','G',10)
grafo_prim_2.adicionaAresta('a4','B','H',7)
grafo_prim_2.adicionaAresta('a5','B','C',6)
grafo_prim_2.adicionaAresta('a6','C','F',8)
grafo_prim_2.adicionaAresta('a7','C','E',12)
grafo_prim_2.adicionaAresta('a8','C','D',8)
grafo_prim_2.adicionaAresta('a9','D','E',14)
grafo_prim_2.adicionaAresta('a10','G','F',1)
grafo_prim_2.adicionaAresta('a11','F','E',2)
grafo_prim_2.adicionaAresta('a12','F','H',2)

#print(grafo_prim_2.arestas_sobre_vertice('C'))
#print(grafo_prim_2.djarkstra('B','H',10,10,['A','C','D']))
#print(grafo_prim_2.ordenacao_topologica())
#print(grafo_prim_2.prim(grafo_prim_2))

ordenacao_topo = MeuGrafo(['2','7','5','3','8','9','10','11'])
ordenacao_topo.adicionaAresta('a1','7','8',9)
ordenacao_topo.adicionaAresta('a2','7','11',4)
ordenacao_topo.adicionaAresta('a3','5','11',10)
ordenacao_topo.adicionaAresta('a4','3','8',7)
ordenacao_topo.adicionaAresta('a5','3','10',6)
ordenacao_topo.adicionaAresta('a6','11','2',8)
ordenacao_topo.adicionaAresta('a7','11','9',12)
ordenacao_topo.adicionaAresta('a8','11','10',8)
ordenacao_topo.adicionaAresta('a9','8','9',14)
ordenacao_topo.adicionaAresta('a10','10','8',14)

print(ordenacao_topo.ordenacao_topologica())


ordenacao_topo2 = MeuGrafo(['0','1','2','3','4','5','6','7'])
ordenacao_topo2.adicionaAresta('a1','0','1',9)
ordenacao_topo2.adicionaAresta('a2','0','2',4)
ordenacao_topo2.adicionaAresta('a3','0','3',10)
ordenacao_topo2.adicionaAresta('a4','1','2',7)
ordenacao_topo2.adicionaAresta('a5','1','5',6)
ordenacao_topo2.adicionaAresta('a6','1','6',8)
ordenacao_topo2.adicionaAresta('a7','2','5',12)
ordenacao_topo2.adicionaAresta('a8','2','6',8)
ordenacao_topo2.adicionaAresta('a9','3','5',14)
ordenacao_topo2.adicionaAresta('a10','4','6',14)
ordenacao_topo2.adicionaAresta('a11','4','7',14)

#print(ordenacao_topo2.ordenacao_topologica())

Letras = MeuGrafo(['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24',
                                '25', '26', '27', '31', '32', '33', '34', '35', '36', '37', '41', '42', '43',
                                '44', '45', '46', '47', '51', '52', '53', '54', '55', '56', '57', '61', '62', '63',
                                '64', '65', '66', '67', '68','71', '72', '73', '74', '75', '76', '77', '78', '81', '82',
                                '83', '84', '85', '86', '87', '88'])

        # Primeiro Periodo e Segundo Periodo
Letras.adicionaAresta('a1', '11', '21')
Letras.adicionaAresta('a2', '11', '22')
Letras.adicionaAresta('a3', '12', '23')
Letras.adicionaAresta('a4', '12', '25')
Letras.adicionaAresta('a5', '17', '26')

        # Segundo Periodo e Terceiro Periodo
Letras.adicionaAresta('a6', '21', '31')
Letras.adicionaAresta('a7', '21', '32')
Letras.adicionaAresta('a8', '21', '33')
Letras.adicionaAresta('a9', '24', '34')
Letras.adicionaAresta('a10', '25', '35')

        # Terceiro Periodo e Quarto Periodo
Letras.adicionaAresta('a11', '31', '41')
Letras.adicionaAresta('a12', '33', '42')
Letras.adicionaAresta('a13', '25', '43')
Letras.adicionaAresta('a14', '25', '44')
Letras.adicionaAresta('a15', '36', '44')
Letras.adicionaAresta('a16', '23', '46')
Letras.adicionaAresta('a17', '35', '46')
Letras.adicionaAresta('a18', '37', '47')

        # Quarto Periodo e Quinto Periodo
Letras.adicionaAresta('a19', '31', '51')
Letras.adicionaAresta('a20', '35', '52')
Letras.adicionaAresta('a21', '13', '53')
Letras.adicionaAresta('a22', '45', '54')
Letras.adicionaAresta('a23', '35', '55')
Letras.adicionaAresta('a24', '22', '56')
Letras.adicionaAresta('a25', '37', '57')

        # Quinto Periodo e Sexto Periodo
Letras.adicionaAresta('a26', '31', '61')
Letras.adicionaAresta('a27', '31', '62')
Letras.adicionaAresta('a28', '35', '63')
Letras.adicionaAresta('a29', '54', '64')
Letras.adicionaAresta('a30', '37', '67')
Letras.adicionaAresta('a31', '54', '68')

        # Sexto Periodo e Setimo Periodo
Letras.adicionaAresta('a32', '31', '71')
Letras.adicionaAresta('a33', '31', '72')
Letras.adicionaAresta('a34', '31', '73')
Letras.adicionaAresta('a35', '64', '74')
Letras.adicionaAresta('a36', '35', '75')
Letras.adicionaAresta('a37', '45', '76')
Letras.adicionaAresta('a38', '27', '77')
Letras.adicionaAresta('a39', '53', '77')
Letras.adicionaAresta('a40', '64', '78')
Letras.adicionaAresta('a41', '68', '78')

        # Setimo Periodo e Oitavo
Letras.adicionaAresta('a42', '17', '83')
Letras.adicionaAresta('a43', '74', '84')
Letras.adicionaAresta('a44', '77', '87')
Letras.adicionaAresta('a45', '74', '88')
Letras.adicionaAresta('a46', '78', '88')

#print(Letras.ordenacao_topologica())


Fisica = MeuGrafo(['11','12', '13', '14', '15', '16', '17', '21', '22', '23', '24',
                    '25','26', '27', '31', '32', '33', '34', '35', '36', '37', '41', '42', '43',
                    '44','45', '46', '51', '52', '53', '54', '55', '56', '61', '62', '63', '64', '65',
                    '66','71', '72', '73', '74', '75', '81', '82', '83', '84', '85', '86'])

        # Primeiro Periodo e Segundo Periodo
Fisica.adicionaAresta('a1', '11', '21')
Fisica.adicionaAresta('a2', '12', '21')
Fisica.adicionaAresta('a3', '11', '22')
Fisica.adicionaAresta('a4', '12', '22')
Fisica.adicionaAresta('a5', '12', '23')
Fisica.adicionaAresta('a6', '12', '24')
Fisica.adicionaAresta('a7', '14', '24')
Fisica.adicionaAresta('a8', '15', '25')

        # SeguFndo Periodo e Terceiro Periodo
Fisica.adicionaAresta('a9', '21', '31')
Fisica.adicionaAresta('a10', '23', '31')
Fisica.adicionaAresta('a11', '21', '32')
Fisica.adicionaAresta('a12', '22', '32')
Fisica.adicionaAresta('a13', '23', '33')

        # Terceiro Periodo e Quarto Periodo
Fisica.adicionaAresta('a14', '31', '41')
Fisica.adicionaAresta('a15', '31', '42')
Fisica.adicionaAresta('a16', '32', '42')
Fisica.adicionaAresta('a17', '33', '45')
Fisica.adicionaAresta('a18', '31', '46')

        # Quarto Periodo e Quinto Periodo
Fisica.adicionaAresta('a19', '41', '51')
Fisica.adicionaAresta('a20', '45', '51')
Fisica.adicionaAresta('a21', '41', '52')
Fisica.adicionaAresta('a22', '42', '52')
Fisica.adicionaAresta('a23', '45', '53')
Fisica.adicionaAresta('a24', '31', '54')
Fisica.adicionaAresta('a25', '43', '55')

        # Quinto Periodo e Sexto Periodo
Fisica.adicionaAresta('a26', '51', '61')
Fisica.adicionaAresta('a27', '51', '62')
Fisica.adicionaAresta('a28', '52', '62')
Fisica.adicionaAresta('a29', '21', '63')
Fisica.adicionaAresta('a30', '53', '63')
Fisica.adicionaAresta('a31', '51', '64')
Fisica.adicionaAresta('a32', '56', '66')

        # Sexto Periodo e Setimo Periodo
Fisica.adicionaAresta('a33', '61', '71')
Fisica.adicionaAresta('a34', '41', '72')
Fisica.adicionaAresta('a35', '45', '72')
Fisica.adicionaAresta('a36', '66', '73')
Fisica.adicionaAresta('a37', '31', '74')
Fisica.adicionaAresta('a38', '43', '74')

        # Setimo Periodo e Oitavo
Fisica.adicionaAresta('a39', '65', '81')
Fisica.adicionaAresta('a40', '74', '82')
Fisica.adicionaAresta('a41', '73', '83')
Fisica.adicionaAresta('a42', '54', '84')
Fisica.adicionaAresta('a43', '71', '84')
Fisica.adicionaAresta('a44', '16', '85')
Fisica.adicionaAresta('a45', '25', '85')

#print(Fisica.ordenacao_topologica())

'''