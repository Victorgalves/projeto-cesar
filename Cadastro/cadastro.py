class Cadastro:
    def __init__(self):
        self.items = {}
        self.email = ""

    def criar_cadastroProf(self):
        self.email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        if self.email in self.items:
            print("Email já existe")
        else:
            self.items[self.email] = []
            print("Email cadastrado com sucesso")

    def cadastro_turma(self):
        qnt_alunos = int(input("Quantos alunos vão participar da turma? "))
        codigo = input("Digite o código da turma: ")
        self.items[self.email] = [qnt_alunos, codigo]
        
