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
            self.salvar_cadastro(senha)

    def salvar_cadastro(self, senha):
        with open("cadastro_data.txt", "a") as arquivo:
            arquivo.write(f"Email: {self.email}\tSenha: {senha}\n")

    def carregar_cadastros(self):
        try:
            with open("cadastro_data.txt", "r") as arquivo:
                for linha in arquivo:
                    values = linha.strip().split("\t")
                    if len(values) == 2:
                        email, senha = values
                        self.items[email] = []
                        print("Cadastro carregado com sucesso!")       
        except FileNotFoundError:
            # Caso o arquivo não exista, cria um novo arquivo vazio
            with open("cadastro_data.txt", "w") as arquivo:
                pass


    def cadastro_turma(self):
        qnt_alunos = int(input("Quantos alunos vão participar da turma? "))
        codigo = input("Digite o código da turma: ")
        self.items[self.email] = [qnt_alunos, codigo]
        print("Código criado com sucesso!")
        self.salvar_cadastro_turma(qnt_alunos, codigo)

    def salvar_cadastro_turma(self, qnt_alunos, codigo):
        with open("cadastro_data.txt", "a") as arquivo:
            arquivo.write(f"Email: {self.email}\tQuantidade de Alunos: {qnt_alunos}\tCódigo: {codigo}\n")

    def verificar_codigo(self):
        codigo_digitado = ""
        while codigo_digitado != self.items[self.email][1]:
            codigo_digitado = input("Digite o código da turma: ")
            if codigo_digitado != self.items[self.email][1]:
                print("Código inválido!")
        print("Entrada com sucesso!")


    

            