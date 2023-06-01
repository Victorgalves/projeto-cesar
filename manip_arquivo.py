def check_login(login):
    with open("login_data.txt", "r") as arquivo:
        for linha in arquivo:
            if linha.startswith("Login:") and login == linha.split(":")[1].strip():
                return True
    return False


def armazenar_login_senha():
    login = input("Login: ")
    senha = input("Senha: ")
    return login, senha

def salvar_login_senha(login, senha):
    with open("login_data.txt", "w") as arquivo:
        arquivo.write(f"Login: {login}\nSenha: {senha}")
    print("Login e senha salvos com sucesso.")

def main():
    login, senha = armazenar_login_senha()
    if check_login(login):
        print("E-mail de login já existe.")
    else:
        salvar_login_senha(login, senha)

if __name__ == "__main__":
    main()
