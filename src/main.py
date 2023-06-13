import Cadastro.cadastro as c
import Quizz.quizz as q
import menu as m

cadastro = c.Cadastro()
quizz = q.Quizz()
menu = m.menu_principal()

opcoes = {
    'Cadastro': [
        cadastro.criar_cadastroProf,
        cadastro.cadastro_turma,
    ],
    'Quizz': [
        quizz.quizz_inicial,
    ]
}
