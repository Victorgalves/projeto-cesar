import Cadastro.cadastro as c
import Quizz.quizz as q
import menu as m

while True:
    try:
        cadastro = c.Cadastro()
        quizz = q.Quizz()
        menu = m.menu_principal()
    except ValueError:
        continue
    except:
        break

    opcoes = {
        'Cadastro': [
            cadastro.criar_cadastroProf,
            cadastro.cadastro_turma,
        ],
        'Quizz': [
            quizz.quizz_inicial,
        ]
    }