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
            return self.email


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
        codigo = input("Digite o código da turma: ")
        self.items[self.email].append(codigo)  # Usamos append() para adicionar o código à lista existente
        print("Código criado com sucesso!")
        self.salvar_cadastro_turma(codigo)



    def salvar_cadastro_turma(self, codigo):
        with open("cadastro_data.txt", "a") as arquivo:
            arquivo.write(f"Email: {self.email}\tCódigo: {codigo}\n")

    def verificar_codigo_turma(cadastro):
        codigo_turma = input("Digite o código da turma: ")
        if codigo_turma in cadastro.items.get(cadastro.email, []):
            print("Acesso permitido!")
        else:
            print("Código inválido!")



    

            