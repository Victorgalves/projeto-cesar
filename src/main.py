import Cadastro.cadastro as c
import menu as m

while True:
    try:
        cadastro = c.Cadastro()
        menu = m.menu_principal()
    except ValueError:
        continue
    except EOFError:
        break

    opcao = {
        'Cadastro': [
            cadastro.criar_cadastroProf,
            cadastro.cadastro_turma,
        ]
    }