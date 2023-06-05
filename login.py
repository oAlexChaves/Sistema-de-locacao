from getpass import getpass
import json

def login():
    print("Bem-vindo! Por favor, faça login:")
    usuario = input("Usuário: ")
    senha = getpass("Senha: ")
    
    if verificar_credenciais(usuario, senha):
        print("Login bem-sucedido!")
        return True
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

def cadastrar_usuario(usuario, senha):
  try:
    arquivo_credenciais = open("credenciais.txt", "r+")
    credenciais = arquivo_credenciais.readlines()
  except:
    print("Erro no arquivo de credenciais")
    return False

  for cr in credenciais:
    js = json.loads(cr)
    if js["Login"]==usuario:
      arquivo_credenciais.close()
      print("Usuário já existe")
      return False
  
  dict_credencial = {"Login": usuario, "Senha": senha}
  arquivo_credenciais.writelines("\n"+json.dumps(dict_credencial))

  arquivo_credenciais.close()
  print("Usuário foi cadastrado com successo!")
  return True


def remover_usuario(usuario):
  try:
    arquivo_credenciais = open("credenciais.txt", "r")
    credenciais = arquivo_credenciais.readlines()
    arquivo_credenciais.close()
  except:
    print("Erro ao ler arquivo de credenciais")
    return False

  for cr in credenciais:
    js = json.loads(cr)
    if js["Login"]==usuario:
      credenciais.remove(cr)
  try:
    arquivo_credenciais = open("credenciais.txt", "w")
    arquivo_credenciais.writelines(credenciais)
    arquivo_credenciais.close()
    print("Usuário removido com sucesso!")
    return True
  except:
    print("Erro ao modificar arquivo de credenciais")
    return False

def alterar_senha(usuario, senha):

  try:
    arquivo_credenciais = open("credenciais.txt", "r")
    credenciais = arquivo_credenciais.readlines()
    arquivo_credenciais.close()
  except:
    print("Erro ao ler o arquivo de credenciais")
    return False


  usuario_existe = False

 
  for index, cr in enumerate(credenciais):
    js = json.loads(cr)
    if js["Login"]==usuario:
      js["Senha"]=senha
      credenciais[index]=(json.dumps(js)+"\n")
      usuario_existe = True
  

  if usuario_existe:
    try:
      arquivo_credenciais = open("credenciais.txt", "w")
      arquivo_credenciais.writelines(credenciais)
      arquivo_credenciais.close()
      print("Senha alterada com sucesso!")
      return True
    except:
      print("Erro ao modificar o arquivo de credenciais")
      return False

  else:
    print("Usuário não encontrado.")
    return False
