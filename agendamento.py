import login

def exibir_agenda():
    with open('agenda.txt', 'r') as arquivo:
        agenda = arquivo.read()
        if agenda:
            print("Agenda:")
            print(agenda)
        else:
            print("Agenda vazia.")

def verificar_disponibilidade(sala, horario):
    with open('agenda.txt', 'r') as arquivo:
        agenda = arquivo.readlines()
        for i, linha in enumerate(agenda):
            if sala in linha:
                horarios = agenda[i + 1].strip() if i + 1 < len(agenda) else ''
                if horario in horarios:
                    print(f"A Sala {sala} está ocupada nesse horário.")
                    return False
        return True

def agendar_horario():
    sala = input("Digite o número da sala que deseja agendar: ")
    nome = input("Digite o seu nome: ")
    horario = input("Digite o horário que deseja agendar (hh:mm): ")

    if verificar_disponibilidade(sala, horario):
        with open('agenda.txt', 'r+') as arquivo:
            linhas = arquivo.readlines()
            arquivo.seek(0)
            for linha in linhas:
                arquivo.write(linha)
                if sala in linha:
                    arquivo.write(f"{horario} - {nome}\n")
            arquivo.truncate()
        print("Horário agendado com sucesso!")

# Exibindo menu de opções
while login.login():
    while True:
        print("\nMenu:")
        print("1. Exibir agenda")
        print("2. Age3ndar horário")
        print("3. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            exibir_agenda()
        elif opcao == "2":
            agendar_horario()
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Digite novamente.")

print("Programa encerrado.")
