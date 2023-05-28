from getpass import getpass

def login():
    print("Bem-vindo! Por favor, faça login:")
    usuario = input("Usuário: ")
    senha = getpass("Senha: ")
    
    if verificar_credenciais(usuario, senha):
        print("Login bem-sucedido!")
    else:
        print("Credenciais inválidas.")

def verificar_credenciais(usuario, senha):
    try:
        with open("credenciais.txt", "r") as arquivo:
            for linha in arquivo:
                credenciais = linha.strip().split(":")
                if len(credenciais) == 2:
                    usuario_arquivo, senha_arquivo = credenciais
                    if usuario == usuario_arquivo and senha == senha_arquivo:
                        return True
    except FileNotFoundError:
        print("Arquivo de credenciais não encontrado.")
    
    return False
