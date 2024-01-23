import unittest
from meu_grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # https://estudante.ifpb.edu.br/media/cursos/43/documentos/Fluxograma_Matriz_Curricular_2017_Letras_EaD_.pdf
        self.Letras = MeuGrafo(['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24',
                                '25', '26', '27', '31', '32', '33', '34', '35', '36', '37', '41', '42', '43',
                                '44', '45', '46', '47', '51', '52', '53', '54', '55', '56', '57', '61', '62', '63',
                                '64', '65', '66', '67', '68','71', '72', '73', '74', '75', '76', '77', '78', '81', '82',
                                '83', '84', '85', '86', '87', '88'])

        # Primeiro Periodo e Segundo Periodo
        self.Letras.adicionaAresta('a1', '11', '21')
        self.Letras.adicionaAresta('a2', '11', '22')
        self.Letras.adicionaAresta('a3', '12', '23')
        self.Letras.adicionaAresta('a4', '12', '25')
        self.Letras.adicionaAresta('a5', '17', '26')

        # Segundo Periodo e Terceiro Periodo
        self.Letras.adicionaAresta('a6', '21', '31')
        self.Letras.adicionaAresta('a7', '21', '32')
        self.Letras.adicionaAresta('a8', '21', '33')
        self.Letras.adicionaAresta('a9', '24', '34')
        self.Letras.adicionaAresta('a10', '25', '35')

        # Terceiro Periodo e Quarto Periodo
        self.Letras.adicionaAresta('a11', '31', '41')
        self.Letras.adicionaAresta('a12', '33', '42')
        self.Letras.adicionaAresta('a13', '25', '43')
        self.Letras.adicionaAresta('a14', '25', '44')
        self.Letras.adicionaAresta('a15', '36', '44')
        self.Letras.adicionaAresta('a16', '23', '46')
        self.Letras.adicionaAresta('a17', '35', '46')
        self.Letras.adicionaAresta('a18', '37', '47')

        # Quarto Periodo e Quinto Periodo
        self.Letras.adicionaAresta('a19', '31', '51')
        self.Letras.adicionaAresta('a20', '35', '52')
        self.Letras.adicionaAresta('a21', '13', '53')
        self.Letras.adicionaAresta('a22', '45', '54')
        self.Letras.adicionaAresta('a23', '35', '55')
        self.Letras.adicionaAresta('a24', '22', '56')
        self.Letras.adicionaAresta('a25', '37', '57')

        # Quinto Periodo e Sexto Periodo
        self.Letras.adicionaAresta('a26', '31', '61')
        self.Letras.adicionaAresta('a27', '31', '62')
        self.Letras.adicionaAresta('a28', '35', '63')
        self.Letras.adicionaAresta('a29', '54', '64')
        self.Letras.adicionaAresta('a30', '37', '67')
        self.Letras.adicionaAresta('a31', '54', '68')

        # Sexto Periodo e Setimo Periodo
        self.Letras.adicionaAresta('a32', '31', '71')
        self.Letras.adicionaAresta('a33', '31', '72')
        self.Letras.adicionaAresta('a34', '31', '73')
        self.Letras.adicionaAresta('a35', '64', '74')
        self.Letras.adicionaAresta('a36', '35', '75')
        self.Letras.adicionaAresta('a37', '45', '76')
        self.Letras.adicionaAresta('a38', '27', '77')
        self.Letras.adicionaAresta('a39', '53', '77')
        self.Letras.adicionaAresta('a40', '64', '78')
        self.Letras.adicionaAresta('a41', '68', '78')

        # Setimo Periodo e Oitavo
        self.Letras.adicionaAresta('a42', '17', '83')
        self.Letras.adicionaAresta('a43', '74', '84')
        self.Letras.adicionaAresta('a44', '77', '87')
        self.Letras.adicionaAresta('a45', '74', '88')
        self.Letras.adicionaAresta('a46', '78', '88')

        # https://estudante.ifpb.edu.br/media/cursos/27/documentos/matriz_telematica_2017_0kGhNJj.pdf
        self.telematica = MeuGrafo(['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24',
                                    '25', '26', '27', '31', '32', '33', '34', '35', '36', '37', '41', '42', '43',
                                    '44', '45', '46', '47', '51', '52', '53', '54', '55', '56', '57', '61', '62', '63',
                                    '64', '65', '66'])

        # Primeiro Periodo e Segundo Periodo
        self.telematica.adicionaAresta('a1', '11', '21')
        self.telematica.adicionaAresta('a2', '12', '22')
        self.telematica.adicionaAresta('a3', '12', '23')
        self.telematica.adicionaAresta('a4', '13', '24')
        self.telematica.adicionaAresta('a5', '16', '26')
        self.telematica.adicionaAresta('a6', '16', '22')
        self.telematica.adicionaAresta('a7', '16', '23')

        # Segundo Periodo e Terceiro Periodo
        self.telematica.adicionaAresta('a8', '21', '31')
        self.telematica.adicionaAresta('a9', '26', '32')
        self.telematica.adicionaAresta('a10', '22', '33')
        self.telematica.adicionaAresta('a11', '23', '33')
        self.telematica.adicionaAresta('a12', '26', '33')
        self.telematica.adicionaAresta('a13', '14', '34')
        self.telematica.adicionaAresta('a14', '25', '35')
        self.telematica.adicionaAresta('a15', '21', '36')
        self.telematica.adicionaAresta('a16', '24', '36')

        # Terceiro Periodo e Quarto Periodo
        self.telematica.adicionaAresta('a17', '31', '41')
        self.telematica.adicionaAresta('a18', '31', '42')
        self.telematica.adicionaAresta('a19', '32', '43')
        self.telematica.adicionaAresta('a20', '32', '44')
        self.telematica.adicionaAresta('a21', '33', '44')
        self.telematica.adicionaAresta('a22', '33', '45')
        self.telematica.adicionaAresta('a23', '21', '46')
        self.telematica.adicionaAresta('a24', '34', '46')

        # Quarto Periodo e Quinto Periodo
        self.telematica.adicionaAresta('a25', '41', '51')
        self.telematica.adicionaAresta('a26', '41', '52')
        self.telematica.adicionaAresta('a27', '44', '53')
        self.telematica.adicionaAresta('a28', '44', '54')
        self.telematica.adicionaAresta('a29', '37', '55')
        self.telematica.adicionaAresta('a30', '41', '55')
        self.telematica.adicionaAresta('a31', '44', '55')

        # Quinto Periodo e Sexto Periodo
        self.telematica.adicionaAresta('a32', '42', '61')
        self.telematica.adicionaAresta('a33', '51', '61')
        self.telematica.adicionaAresta('a34', '53', '62')

        # https://estudante.ifpb.edu.br/media/cursos/26/documentos/Fluxograma_do_Curso_de_Física.pdf
        self.Fisica = MeuGrafo(['11','12', '13', '14', '15', '16', '17', '21', '22', '23', '24',
                                '25','26', '27', '31', '32', '33', '34', '35', '36', '37', '41', '42', '43',
                                '44','45', '46', '51', '52', '53', '54', '55', '56', '61', '62', '63', '64', '65',
                                '66','71', '72', '73', '74', '75', '81', '82', '83', '84', '85', '86'])

        # Primeiro Periodo e Segundo Periodo
        self.Fisica.adicionaAresta('a1', '11', '21')
        self.Fisica.adicionaAresta('a2', '12', '21')
        self.Fisica.adicionaAresta('a3', '11', '22')
        self.Fisica.adicionaAresta('a4', '12', '22')
        self.Fisica.adicionaAresta('a5', '12', '23')
        self.Fisica.adicionaAresta('a6', '12', '24')
        self.Fisica.adicionaAresta('a7', '14', '24')
        self.Fisica.adicionaAresta('a8', '15', '25')

        # SeguFndo Periodo e Terceiro Periodo
        self.Fisica.adicionaAresta('a9', '21', '31')
        self.Fisica.adicionaAresta('a10', '23', '31')
        self.Fisica.adicionaAresta('a11', '21', '32')
        self.Fisica.adicionaAresta('a12', '22', '32')
        self.Fisica.adicionaAresta('a13', '23', '33')

        # Terceiro Periodo e Quarto Periodo
        self.Fisica.adicionaAresta('a14', '31', '41')
        self.Fisica.adicionaAresta('a15', '31', '42')
        self.Fisica.adicionaAresta('a16', '32', '42')
        self.Fisica.adicionaAresta('a17', '33', '45')
        self.Fisica.adicionaAresta('a18', '31', '46')

        # Quarto Periodo e Quinto Periodo
        self.Fisica.adicionaAresta('a19', '41', '51')
        self.Fisica.adicionaAresta('a20', '45', '51')
        self.Fisica.adicionaAresta('a21', '41', '52')
        self.Fisica.adicionaAresta('a22', '42', '52')
        self.Fisica.adicionaAresta('a23', '45', '53')
        self.Fisica.adicionaAresta('a24', '31', '54')
        self.Fisica.adicionaAresta('a25', '43', '55')

        # Quinto Periodo e Sexto Periodo
        self.Fisica.adicionaAresta('a26', '51', '61')
        self.Fisica.adicionaAresta('a27', '51', '62')
        self.Fisica.adicionaAresta('a28', '52', '62')
        self.Fisica.adicionaAresta('a29', '21', '63')
        self.Fisica.adicionaAresta('a30', '53', '63')
        self.Fisica.adicionaAresta('a31', '51', '64')
        self.Fisica.adicionaAresta('a32', '56', '66')

        # Sexto Periodo e Setimo Periodo
        self.Fisica.adicionaAresta('a33', '61', '71')
        self.Fisica.adicionaAresta('a34', '41', '72')
        self.Fisica.adicionaAresta('a35', '45', '72')
        self.Fisica.adicionaAresta('a36', '66', '73')
        self.Fisica.adicionaAresta('a37', '31', '74')
        self.Fisica.adicionaAresta('a38', '43', '74')

        # Setimo Periodo e Oitavo
        self.Fisica.adicionaAresta('a39', '65', '81')
        self.Fisica.adicionaAresta('a40', '74', '82')
        self.Fisica.adicionaAresta('a41', '73', '83')
        self.Fisica.adicionaAresta('a42', '54', '84')
        self.Fisica.adicionaAresta('a43', '71', '84')
        self.Fisica.adicionaAresta('a44', '16', '85')
        self.Fisica.adicionaAresta('a45', '25', '85')

        # https://estudante.ifpb.edu.br/media/cursos/16/documentos/Matriz_Curricular_CE2016.2.pdf
        self.Const_Edificios = MeuGrafo(['11', '12', '13', '14', '15', '16', '17', '18', '21', '22', '23', '24',
                                         '25', '26', '27', '31', '32', '33', '34', '35', '36', '37', '38', '41', '42',
                                         '43',
                                         '44', '45', '46', '47', '51', '52', '53', '54', '55', '56', '57', '58', '61',
                                         '62', '63', '64', '65', '66', '67', '68', '71', '72', '73'])

        # Primeiro Periodo e Segundo Periodo
        self.Const_Edificios.adicionaAresta('a1', '15', '21')
        self.Const_Edificios.adicionaAresta('a2', '14', '23')
        self.Const_Edificios.adicionaAresta('a3', '11', '24')
        self.Const_Edificios.adicionaAresta('a4', '17', '24')
        self.Const_Edificios.adicionaAresta('a5', '15', '25')
        self.Const_Edificios.adicionaAresta('a6', '17', '26')
        self.Const_Edificios.adicionaAresta('a7', '17', '27')

        # Segundo Periodo e Terceiro Periodo
        self.Const_Edificios.adicionaAresta('a8', '15', '32')
        self.Const_Edificios.adicionaAresta('a9', '21', '32')
        self.Const_Edificios.adicionaAresta('a10', '21', '33')
        self.Const_Edificios.adicionaAresta('a11', '25', '33')
        self.Const_Edificios.adicionaAresta('a12', '15', '34')
        self.Const_Edificios.adicionaAresta('a13', '11', '35')
        self.Const_Edificios.adicionaAresta('a14', '27', '35')
        self.Const_Edificios.adicionaAresta('a15', '25', '35')
        self.Const_Edificios.adicionaAresta('a16', '26', '36')
        self.Const_Edificios.adicionaAresta('a17', '23', '37')
        self.Const_Edificios.adicionaAresta('a18', '24', '38')

        # Terceiro Periodo e Quarto Periodo
        self.Const_Edificios.adicionaAresta('a19', '17', '41')
        self.Const_Edificios.adicionaAresta('a20', '21', '41')
        self.Const_Edificios.adicionaAresta('a21', '17', '42')
        self.Const_Edificios.adicionaAresta('a22', '21', '42')
        self.Const_Edificios.adicionaAresta('a23', '23', '43')
        self.Const_Edificios.adicionaAresta('a24', '24', '44')
        self.Const_Edificios.adicionaAresta('a25', '36', '45')
        self.Const_Edificios.adicionaAresta('a26', '37', '45')
        self.Const_Edificios.adicionaAresta('a27', '17', '46')
        self.Const_Edificios.adicionaAresta('a28', '32', '46')
        self.Const_Edificios.adicionaAresta('a29', '11', '47')
        self.Const_Edificios.adicionaAresta('a30', '37', '47')

        # Quarto Periodo e Quinto Periodo
        self.Const_Edificios.adicionaAresta('a31', '37', '51')
        self.Const_Edificios.adicionaAresta('a32', '43', '51')
        self.Const_Edificios.adicionaAresta('a33', '45', '51')
        self.Const_Edificios.adicionaAresta('a34', '46', '51')
        self.Const_Edificios.adicionaAresta('a35', '41', '52')
        self.Const_Edificios.adicionaAresta('a36', '42', '52')
        self.Const_Edificios.adicionaAresta('a37', '45', '52')
        self.Const_Edificios.adicionaAresta('a38', '46', '52')
        self.Const_Edificios.adicionaAresta('a39', '17', '53')
        self.Const_Edificios.adicionaAresta('a40', '32', '53')
        self.Const_Edificios.adicionaAresta('a41', '47', '54')
        self.Const_Edificios.adicionaAresta('a42', '17', '55')
        self.Const_Edificios.adicionaAresta('a43', '32', '55')
        self.Const_Edificios.adicionaAresta('a44', '46', '56')
        self.Const_Edificios.adicionaAresta('a45', '43', '57')

        # Quinto Periodo e Sexto Periodo
        self.Const_Edificios.adicionaAresta('a46', '31', '62')
        self.Const_Edificios.adicionaAresta('a47', '44', '62')
        self.Const_Edificios.adicionaAresta('a48', '22', '64')
        self.Const_Edificios.adicionaAresta('a49', '27', '64')
        self.Const_Edificios.adicionaAresta('a50', '33', '64')
        self.Const_Edificios.adicionaAresta('a51', '36', '64')
        self.Const_Edificios.adicionaAresta('a52', '47', '65')
        self.Const_Edificios.adicionaAresta('a53', '22', '66')
        self.Const_Edificios.adicionaAresta('a54', '31', '67')

        # https://estudante.ifpb.edu.br/media/c ursos/9/documentos/matriz_curricular_RzPjUPE.pdf
        self.Matematica = MeuGrafo(['11', '12','13', '14', '15', '16', '21', '22', '23', '24',
                                    '25', '31', '32', '33', '34', '35', '36', '41', '42', '43',
                                    '44', '45', '46', '47', '51', '52', '53', '54', '55', '56', '57', '61', '62', '63',
                                    '64', '65', '66', '67', '71', '72', '73', '74', '75', '76', '77'])

        # Primeiro Periodo e Segundo Periodo
        self.Matematica.adicionaAresta('a1', '12', '21')
        self.Matematica.adicionaAresta('a2', '13', '21')
        self.Matematica.adicionaAresta('a3', '13', '23')

        # Segundo Periodo e Terceiro Periodo
        self.Matematica.adicionaAresta('a4', '21', '31')
        self.Matematica.adicionaAresta('a5', '21', '32')
        self.Matematica.adicionaAresta('a6', '22', '32')
        self.Matematica.adicionaAresta('a7', '23', '33')
        self.Matematica.adicionaAresta('a8', '24', '34')
        self.Matematica.adicionaAresta('a9', '25', '35')
        self.Matematica.adicionaAresta('a10', '16', '36')

        # Terceiro Periodo e Quarto Periodo
        self.Matematica.adicionaAresta('a11', '22', '52')
        self.Matematica.adicionaAresta('a12', '21', '53')
        self.Matematica.adicionaAresta('a13', '33', '53')
        self.Matematica.adicionaAresta('a14', '45', '54')
        self.Matematica.adicionaAresta('a15', '46', '56')
        self.Matematica.adicionaAresta('a16', '47', '57')

        # Quarto Periodo e Quinto Periodo
        self.Matematica.adicionaAresta('a17', '51', '61')
        self.Matematica.adicionaAresta('a18', '41', '62')
        self.Matematica.adicionaAresta('a19', '56', '64')
        self.Matematica.adicionaAresta('a20', '55', '65')
        self.Matematica.adicionaAresta('a21', '57', '67')

        # Quinto Periodo e Sexto Periodo
        self.Matematica.adicionaAresta('a22', '41', '71')
        self.Matematica.adicionaAresta('a23', '41', '72')
        self.Matematica.adicionaAresta('a24', '56', '73')
        self.Matematica.adicionaAresta('a25', '64', '73')
        self.Matematica.adicionaAresta('a26', '64', '74')
        self.Matematica.adicionaAresta('a27', '65', '75')
        self.Matematica.adicionaAresta('a28', '67', '77')

        # https://estudante.ifpb.edu.br/media/cursos/28/documentos/Matriz_Engenharia_de_Computação_2018.pdf
        self.Eng_computacao = MeuGrafo(['11', '12', '13', '14', '15', '16', '17', '21', '22', '23', '24',
                                        '25', '26', '27', '31', '32', '33', '34', '35', '36', '41', '42', '43',
                                        '44', '45', '51', '52', '53', '54', '55', '56', '61', '62', '63', '64', '65',
                                        '71', '72', '73', '74', '75', '81', '82', '83', '84', '85', '91', '92', '93',
                                        '94', '95', '101', '102', '103'])

        # Primeiro Periodo e Segundo Periodo
        self.Eng_computacao.adicionaAresta('a1', '11', '21')
        self.Eng_computacao.adicionaAresta('a2', '14', '24')
        self.Eng_computacao.adicionaAresta('a3', '15', '24')
        self.Eng_computacao.adicionaAresta('a4', '14', '25')
        self.Eng_computacao.adicionaAresta('a5', '15', '25')
        self.Eng_computacao.adicionaAresta('a6', '16', '26')

        # SeguFndo Periodo e Terceiro Periodo
        self.Eng_computacao.adicionaAresta('a7', '21', '31')
        self.Eng_computacao.adicionaAresta('a8', '24', '33')
        self.Eng_computacao.adicionaAresta('a9', '14', '34')
        self.Eng_computacao.adicionaAresta('a10', '15', '34')
        self.Eng_computacao.adicionaAresta('a11', '14', '35')
        self.Eng_computacao.adicionaAresta('a12', '15', '35')
        self.Eng_computacao.adicionaAresta('a13', '26', '36')

        # Terceiro Periodo e Quarto Periodo
        self.Eng_computacao.adicionaAresta('a14', '21', '41')
        self.Eng_computacao.adicionaAresta('a15', '24', '43')
        self.Eng_computacao.adicionaAresta('a16', '24', '44')
        self.Eng_computacao.adicionaAresta('a17', '36', '44')
        self.Eng_computacao.adicionaAresta('a18', '36', '45')

        # Quarto Periodo e Quinto Periodo
        self.Eng_computacao.adicionaAresta('a19', '31', '51')
        self.Eng_computacao.adicionaAresta('a20', '31', '52')
        self.Eng_computacao.adicionaAresta('a21', '24', '53')
        self.Eng_computacao.adicionaAresta('a22', '24', '54')
        self.Eng_computacao.adicionaAresta('a23', '36', '55')
        self.Eng_computacao.adicionaAresta('a24', '44', '55')

        # Quinto Periodo e Sexto Periodo
        self.Eng_computacao.adicionaAresta('a25', '51', '61')
        self.Eng_computacao.adicionaAresta('a26', '43', '62')
        self.Eng_computacao.adicionaAresta('a27', '34', '63')
        self.Eng_computacao.adicionaAresta('a28', '35', '63')
        self.Eng_computacao.adicionaAresta('a29', '31', '64')
        self.Eng_computacao.adicionaAresta('a30', '55', '65')

        # Sexto Periodo e Setimo Periodo
        self.Eng_computacao.adicionaAresta('a31', '24', '72')
        self.Eng_computacao.adicionaAresta('a32', '63', '73')
        self.Eng_computacao.adicionaAresta('a33', '52', '75')
        self.Eng_computacao.adicionaAresta('a34', '64', '75')

        # Setimo Periodo e Oitavo
        self.Eng_computacao.adicionaAresta('a35', '34', '81')
        self.Eng_computacao.adicionaAresta('a36', '35', '81')
        self.Eng_computacao.adicionaAresta('a37', '54', '81')
        self.Eng_computacao.adicionaAresta('a38', '73', '82')
        self.Eng_computacao.adicionaAresta('a39', '74', '83')
        self.Eng_computacao.adicionaAresta('a40', '61', '84')
        self.Eng_computacao.adicionaAresta('a41', '64', '84')
        self.Eng_computacao.adicionaAresta('a42', '75', '85')

        # Oitavo Periodo e Nono Periodo
        self.Eng_computacao.adicionaAresta('a43', '83', '92')
        self.Eng_computacao.adicionaAresta('a44', '44', '93')
        self.Eng_computacao.adicionaAresta('a45', '45', '93')
        self.Eng_computacao.adicionaAresta('a46', '61', '94')
        self.Eng_computacao.adicionaAresta('a47', '75', '94')

        # Nono Periodo e Decimo Periodo
        self.Eng_computacao.adicionaAresta('a48', '92', '103')


        #Grafo teste na aula de ordenação topologica
        self.ordenacao_topo = MeuGrafo(['2', '3', '5', '7', '8', '9', '10', '11'])
        self.ordenacao_topo.adicionaAresta('a1', '7', '8', 9)
        self.ordenacao_topo.adicionaAresta('a2', '7', '11', 4)
        self.ordenacao_topo.adicionaAresta('a3', '5', '11', 10)
        self.ordenacao_topo.adicionaAresta('a4', '3', '8', 7)
        self.ordenacao_topo.adicionaAresta('a5', '3', '10', 6)
        self.ordenacao_topo.adicionaAresta('a6', '11', '2', 8)
        self.ordenacao_topo.adicionaAresta('a7', '11', '9', 12)
        self.ordenacao_topo.adicionaAresta('a8', '11', '10', 8)
        self.ordenacao_topo.adicionaAresta('a9', '8', '9', 14)

        # Grafo da Paraíba
        self.g_p = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p.adicionaAresta('a1', 'J', 'C')
        self.g_p.adicionaAresta('a2', 'C', 'E')
        self.g_p.adicionaAresta('a3', 'C', 'E')
        self.g_p.adicionaAresta('a4', 'P', 'C')
        self.g_p.adicionaAresta('a5', 'P', 'C')
        self.g_p.adicionaAresta('a6', 'T', 'C')
        self.g_p.adicionaAresta('a7', 'M', 'C')
        self.g_p.adicionaAresta('a8', 'M', 'T')
        self.g_p.adicionaAresta('a9', 'T', 'Z')

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
        self.g_p_sem_paralelas.adicionaAresta('a1', 'J', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a2', 'C', 'E')
        self.g_p_sem_paralelas.adicionaAresta('a3', 'P', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a4', 'T', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a5', 'M', 'C')
        self.g_p_sem_paralelas.adicionaAresta('a6', 'M', 'T')
        self.g_p_sem_paralelas.adicionaAresta('a7', 'T', 'Z')

        # Grafos completos
        self.g_c = MeuGrafo(['J', 'C', 'E', 'P'])
        self.g_c.adicionaAresta('a1','J','C')
        self.g_c.adicionaAresta('a2', 'J', 'E')
        self.g_c.adicionaAresta('a3', 'J', 'P')
        self.g_c.adicionaAresta('a4', 'E', 'C')
        self.g_c.adicionaAresta('a5', 'P', 'C')
        self.g_c.adicionaAresta('a6', 'P', 'E')

        self.g_c2 = MeuGrafo(['Nina', 'Maria'])
        self.g_c2.adicionaAresta('amiga', 'Nina', 'Maria')

        self.g_c3 = MeuGrafo(['J'])

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

        # Grafo com ciclos e laços
        self.g_e = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
        self.g_e.adicionaAresta('1', 'A', 'B')
        self.g_e.adicionaAresta('2', 'A', 'C')
        self.g_e.adicionaAresta('3', 'C', 'A')
        self.g_e.adicionaAresta('4', 'C', 'B')
        self.g_e.adicionaAresta('10', 'C', 'B')
        self.g_e.adicionaAresta('5', 'C', 'D')
        self.g_e.adicionaAresta('6', 'D', 'D')
        self.g_e.adicionaAresta('7', 'D', 'B')
        self.g_e.adicionaAresta('8', 'D', 'E')
        self.g_e.adicionaAresta('9', 'E', 'A')
        self.g_e.adicionaAresta('11', 'E', 'B')

        #Grafo testado na aula
        self.grafo = MeuGrafo(["A", "B", "C", "D"])
        self.grafo.adicionaAresta('1', 'A', 'A')
        self.grafo.adicionaAresta('2', 'A', 'C')
        self.grafo.adicionaAresta('3', 'C', 'B')
        self.grafo.adicionaAresta('4', 'B', 'B')
        self.grafo.adicionaAresta('5', 'C', 'D')


        # Matrizes para teste do algoritmo de Warshall
        self.grafo_aula = self.constroi_matriz(self.grafo)
        self.grafo_aula[0][0] = 1
        self.grafo_aula[0][1] = 1
        self.grafo_aula[0][2] = 1
        self.grafo_aula[0][3] = 1
        self.grafo_aula[1][1] = 1
        self.grafo_aula[2][1] = 1
        self.grafo_aula[2][3] = 1


        self.g_p_m = self.constroi_matriz(self.g_p)
        self.g_p_m[0][1] = 1
        self.g_p_m[0][2] = 1
        self.g_p_m[1][2] = 1
        self.g_p_m[3][1] = 1
        self.g_p_m[3][2] = 1
        self.g_p_m[4][1] = 1
        self.g_p_m[4][2] = 1
        self.g_p_m[4][5] = 1
        self.g_p_m[4][6] = 1
        self.g_p_m[5][1] = 1
        self.g_p_m[5][2] = 1
        self.g_p_m[5][6] = 1

        self.g_e_m = self.constroi_matriz(self.g_e)
        for i in range(0, len(self.g_e_m)):
            self.g_e_m[0][i] = 1
            self.g_e_m[2][i] = 1
            self.g_e_m[3][i] = 1
            self.g_e_m[4][i] = 1
        #GRAFOS PARA TESTES DO ALGORITMO djarkstra - ROTEIRO 7
        self.grafo_djarkstra_1 = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z', 'X'])
        self.grafo_djarkstra_1.adicionaAresta('a1', 'J', 'C')
        self.grafo_djarkstra_1.adicionaAresta('a2', 'C', 'E')
        self.grafo_djarkstra_1.adicionaAresta('a3', 'E', 'C')
        self.grafo_djarkstra_1.adicionaAresta('a4', 'C', 'P')
        self.grafo_djarkstra_1.adicionaAresta('a5', 'P', 'C')
        self.grafo_djarkstra_1.adicionaAresta('a6', 'C', 'M')
        self.grafo_djarkstra_1.adicionaAresta('a7', 'C', 'T')
        self.grafo_djarkstra_1.adicionaAresta('a8', 'M', 'T')
        self.grafo_djarkstra_1.adicionaAresta('a9', 'T', 'Z')
        self.grafo_djarkstra_1.adicionaAresta('a10', 'Z', 'C')

        self.grafo_djarkstra_2 = MeuGrafo(["A", "B", "C", "D"])
        self.grafo_djarkstra_2.adicionaAresta('1', 'A', 'A', 2)
        self.grafo_djarkstra_2.adicionaAresta('2', 'A', 'C', 1)
        self.grafo_djarkstra_2.adicionaAresta('3', 'C', 'B', 4)
        self.grafo_djarkstra_2.adicionaAresta('4', 'B', 'B', 7)
        self.grafo_djarkstra_2.adicionaAresta('5', 'C', 'D', 9)

        self.grafo_djarkstra_3 = MeuGrafo(['A', 'B', 'C', 'D', 'E'])
        self.grafo_djarkstra_3.adicionaAresta('1', 'A', 'B', 1)
        self.grafo_djarkstra_3.adicionaAresta('2', 'A', 'C', 2)
        self.grafo_djarkstra_3.adicionaAresta('3', 'C', 'B', 1)
        self.grafo_djarkstra_3.adicionaAresta('4', 'B', 'C', 1)
        self.grafo_djarkstra_3.adicionaAresta('5', 'C', 'D', 1)
        self.grafo_djarkstra_3.adicionaAresta('6', 'D', 'E', 4)


    def constroi_matriz(self, g: MeuGrafo):
        ordem = len(g.N)
        m = list()
        for i in range(ordem):
            m.append(list())
            for j in range(ordem):
                m[i].append(0)
        return m

    def test_warshall(self):
        self.assertEqual(self.grafo.warshall(), self.grafo_aula)
        self.assertEqual(self.g_p.warshall(), self.g_p_m)
        self.assertEqual(self.g_e.warshall(), self.g_e_m)


    def test_djarkstra(self):
        self.assertEqual(self.grafo_djarkstra_1.djarkstra("J",'Z',3,4,['C','M','Z','E']),['J', 'C', 'T', 'Z'])
        self.assertEqual(self.grafo_djarkstra_2.djarkstra('A', 'D', 3, 4, ['C']),"Não Existe Caminho Para o Vertice D !")
        self.assertEqual(self.grafo_djarkstra_3.djarkstra('A', 'E', 3, 4, ['D']),['A', 'C', 'D', 'E'])
        self.assertEqual(self.grafo_djarkstra_2.djarkstra('A', 'D', 2, 12, ['C']),['A', 'C', 'D'])



    def test_Ordenacao_topologica(self):
        self.assertEqual(self.Letras.ordenacao_topologica(),['11', '12', '13', '14', '15', '16', '17', '24', '27', '36', '37', '45', '65', '66', '81', '82', '85', '86', '21', '22', '23', '25', '26', '34', '47', '53', '54', '57', '67', '76', '83', '31', '32', '33', '35', '43', '44', '56', '64', '68', '77', '41', '42', '46', '51', '52', '55', '61', '62', '63', '71', '72', '73', '74', '75', '78', '87', '84', '88'])
        self.assertEqual(self.telematica.ordenacao_topologica(),['11', '12', '13', '14', '15', '16', '17', '25', '27', '37', '47', '56', '57', '63', '64', '65', '66', '21', '22', '23', '24', '26', '34', '35', '31', '32', '33', '36', '46', '41','42','43','44','45','51','52','53','54','55','61','62'])
        self.assertEqual(self.Fisica.ordenacao_topologica(),['11', '12', '13', '14', '15', '16', '17', '26', '27', '34', '35', '36', '37', '43', '44', '56', '65', '75', '86', '21', '22', '23', '24', '25', '55', '66', '81', '31', '32', '33', '73', '85', '41', '42', '45', '46', '54', '74', '83', '51', '52', '53', '72', '82', '61', '62', '63', '64', '71', '84'])
        self.assertEqual(self.Matematica.ordenacao_topologica(),['11', '12', '13', '14', '15', '16', '22', '24', '25', '41', '42', '43', '44', '45', '46', '47', '51', '55', '63', '66', '76', '21', '23', '34', '35', '36', '52', '54', '56', '57', '61', '62', '65', '71', '72', '31', '32', '33', '64', '67', '75', '53', '73', '74', '77'])
        self.assertEqual(self.Const_Edificios.ordenacao_topologica(),['11', '12', '13', '14', '15', '16', '17', '18', '22', '31', '58', '61', '63', '68', '71', '72', '73', '21', '23', '24', '25', '26', '27', '34', '66', '67', '32', '33', '35', '36', '37', '38', '41', '42', '43', '44', '45', '46', '47', '53', '55', '57', '62', '64', '51', '52', '54', '56', '65'])
        self.assertEqual(self.Eng_computacao.ordenacao_topologica(),['11', '12', '13', '14', '15', '16', '17', '22', '23', '27', '32', '42', '56', '71', '74', '91', '95', '101', '102', '21', '24', '25', '26','34', '35', '83', '31', '33', '36', '41', '43', '53', '54', '63', '72', '92', '44', '45', '51', '52', '62', '64', '73','81', '103', '55', '61', '75', '82', '93', '65', '84', '85', '94'])
        self.assertEqual(self.ordenacao_topo.ordenacao_topologica(),['3', '5', '7', '8', '11', '2', '9', '10'])