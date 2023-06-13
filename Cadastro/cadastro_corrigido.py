import csv

class Cadastro:
    def __init__(self):
        self.items = {}

    def criar_cadastroProf(self):
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        
        if email in self.items:
            print("Email já existe")
        else:
            self.items[email] = [senha, None, None]
            print("Email cadastrado com sucesso")
            try:
                self.salvar_cadastro()
            except Exception as e:
                print("Erro ao salvar cadastro:", str(e))

    def salvar_cadastro(self):
        try:
            with open("cadastro_data.csv", "w", newline="") as arquivo:
                writer = csv.writer(arquivo)
                for email, dados in self.items.items():
                    writer.writerow([email] + dados)
        except Exception as e:
            print("Erro ao salvar cadastro:", str(e))

    def carregar_cadastros(self):
        try:
            with open("cadastro_data.csv", "r") as arquivo:
                reader = csv.reader(arquivo)
                for linha in reader:
                    email = linha[0]
                    dados = linha[1:]
                    self.items[email] = dados
                    print("Cadastro carregado com sucesso!")
        except FileNotFoundError:
            with open("cadastro_data.csv", "w", newline="") as arquivo:
                pass

    def cadastro_turma(self):
        try:
            email = input("Digite seu email: ")
            if email not in self.items:
                print("Email não encontrado.")
                return

            qnt_alunos = int(input("Quantos alunos vão participar da turma? "))
            codigo = input("Digite o código da turma: ")
            self.items[email][1] = qnt_alunos
            self.items[email][2] = codigo
            print("Código criado com sucesso!")
            try:
                self.salvar_cadastro()
            except Exception as e:
                print("Erro ao salvar cadastro da turma:", str(e))
        except ValueError:
            print("Quantidade de alunos inválida. Digite um número inteiro.")
            return

    def verificar_codigo(self):
        email = input("Digite seu email: ")
        if email not in self.items:
            print("Email não encontrado.")
            return

        codigo_digitado = ""
        while codigo_digitado != self.items[email][2]:
            codigo_digitado = input("Digite o código da turma: ")
            if codigo_digitado != self.items[email][2]:
                print("Código inválido!")
        print("Entrada com sucesso!")


# Exemplo de uso:
while True:
    cadastro = Cadastro()
    cadastro.carregar_cadastros()
    cadastro.criar_cadastroProf()
    cadastro.cadastro_turma()
    cadastro.verificar_codigo()


            
