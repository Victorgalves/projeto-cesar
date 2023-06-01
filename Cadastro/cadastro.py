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
            self.salvar_cadastro()

    def salvar_cadastro(self):
        with open("cadastro_data.txt", "a") as arquivo:
            arquivo.write(f"Email: {self.email}\tSenha: {senha}\n")

    def carregar_cadastros(self):
        with open("cadastro_data.txt", "r") as arquivo:
            for linha in arquivo:
                email, senha = linha.strip().split("\t")
                self.items[email] = []
        
    def cadastro_turma(self):
        qnt_alunos = int(input("Quantos alunos vão participar da turma? "))
        codigo = input("Digite o código da turma: ")
        self.items[self.email] = [qnt_alunos, codigo]
        print("Código criado com sucesso!")
        self.salvar_cadastro()

    def verificar_codigo(self):
        codigo_digitado = ""
        while codigo_digitado != self.items[self.email][1]:
            codigo_digitado = input("Digite o código da turma: ")
            if codigo_digitado != self.items[self.email][1]:
                print("Código inválido!")
        print("Entrada com sucesso!")

cadastro = Cadastro()
cadastro.carregar_cadastros()
cadastro.criar_cadastroProf()

            