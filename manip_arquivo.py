def receber_login_senha():
    login = input('Entre com seu login: ')
    senha = input('Digite sua senha: ')
    return login, senha


def abrir_arquivo():
    with open('./banco_dados.txt', 'w') as arquivo:
        for i in arquivo:
            lista = arquivo.readlines()
            print(lista.strip())


def salvar_login_senha():
    with open('./banco_dados.txt', 'a') as arquivo:
        dados_entrada = receber_login_senha()
        arquivo.write(dados_entrada + '\n')

receber_login_senha()
salvar_login_senha()

# def collect_login_password():
    # login = input("Enter your login: ")
    # password = input("Enter your password: ")
    # return login, password
# 
# def save_login_password(login, password):
    # with open("login_data.txt", "w") as file:
        # file.write(f"Login: {login}\nPassword: {password}")
    # print("Login and password saved successfully.")
# 
# def main():
    # login, password = receber_login_senha()
    # save_login_password(login, password)
# 
# if __name__ == "__main__":
    # main()
