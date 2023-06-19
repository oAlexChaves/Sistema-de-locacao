import login
#exibi a agenda na tela 
def exibir_agenda():
    with open('agenda.txt', 'r') as arquivo:
        agenda = arquivo.read()
        if agenda:
            print("Agenda:")
            print(agenda)
        else:
            print("Agenda vazia.")
#verifica a disponibilidade da sala para o agendamento
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
#agenda na sala o horario desejado
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

#exclui o horario da agenda 
def remover_agendamento():
    sala = input("Digite o número da sala do agendamento que deseja remover: ")
    horario = input("Digite o horário do agendamento que deseja remover (hh:mm): ")

    with open('agenda.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

    with open('agenda.txt', 'w') as arquivo:
        remover_linha = False
        for i, linha in enumerate(linhas):
            if sala in linha:
                remover_linha = True
            elif remover_linha and horario in linha:
                remover_linha = False
                continue
            arquivo.write(linha)

    print("Agendamento removido com sucesso!")


# Exibe menu de opções
while login.login():
    while True:
        print("\nMenu:")
        print("1. Exibir agenda")
        print("2. Agendar horário")
        print("3. Remover agendamento")
        print("4. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            exibir_agenda()
        elif opcao == "2":
            agendar_horario()
        elif opcao == "3":
            remover_agendamento()
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Digite novamente.")

print("Programa encerrado.")
