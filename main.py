import login
import agendamento
# Programa principal

#verifica o login para iniciar o  codigo 
if login.login(login.verificar_credenciais() == True ):
    agendamento
else:
  print("Login invalido")