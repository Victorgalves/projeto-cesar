import Cadastro.cadastro as c
def menu_principal():
        cadastro= c.Cadastro()
        opcoes_do_primeiro_menu = ["Sou professor", "Sou aluno"]
        print('[CTRL + D] - FINALIZAR O PROGRAMA')
        print("\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("\t\t\t         Menu")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")
        print("Digite o número da ação que deseja realizar: \n[1]Sou professor \n[2]Sou aluno \n")
        primeira_escolha_do_usuario = int(input())

        if primeira_escolha_do_usuario == 1:
            cadastro.criar_cadastroProf()
            cadastro.cadastro_turma()
        elif primeira_escolha_do_usuario == 2:
            cadastro.verificar_codigo_turma()
